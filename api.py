# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
from flask import Flask, request
app = Flask(__name__)

###################################################
_sost = {
            "8D7F41C4E7C01050FADA09B6C4035A1F1D6FCD787004DCABED973CD5E115C023":
            {
                "aut":{"Админ":0, "Саша":0, "Паша":0},
                "qu":{"Админ":"Очень сложный пароль","Саша":"Кто сидел в траве?", "Паша":"Сколько ног у кузнечика?"}
                ,"otv":{"Админ":"Админ","Саша":"Кузнечик", "Паша":"7"},
                "last_name":0,
            }
        }

def save(sost, user):
    global _sost
    _sost[user] = sost
    
def load(user):
    global _sost
    return _sost[user]

def first_aut(user):
    global _sost, stop, slon
    if user not in _sost:
        _sost[user] = {
                "aut":{"Админ":0, "Саша":0, "Паша":0},
                "qu":{"Админ":"Очень сложный пароль","Саша":"Кто сидел в траве?", "Паша":"Сколько ног у кузнечика?"}
                ,"otv":{"Админ":"Админ","Саша":"Кузнечик", "Паша":"7"},
                "last_name":0,
            }
    else:
        _sost[user]["last_name"] = 0
        stop = False
        slon = False
    return "Скажите своё имя"
    
def aut(user, s):
    global stop, slon
    #return s
    h = load(user)
    ln = h["last_name"]
    if not ln: 
        if s in h["aut"]:
            h["aut"][s] = 1
            h["last_name"] = s
            return s+", ответьте на вопрос: "+h["qu"][s]
        else:
            return "Нет такого имени.\n"+first_aut(user)
    else:
        name = h["last_name"]
        if s == h["otv"][name]:
            stop = True
            return "Добро пожаловать, "+name
        else:
            h["aut"][name] += 1
            if h["aut"][name]>5:
                slon = True
                return "А теперь купи слона"
            return "Не правильно ("+s+"). "+h["qu"][name]
        

#############################################

logging.basicConfig(level=logging.DEBUG)

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )

# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    user_id = req['session']['user_id']

    if req['session']['new']:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        sessionStorage[user_id] = {
            'suggests': [
                "Не хочу.",
                "Не буду.",
                "Отстань!",
                "Нет",
            ]
        }

        
        #res['response']['text'] = 'Привет! Купи слона!'
        #res['response']['buttons'] = get_suggests(user_id)
        res['response']['text'] = first_aut(user_id)
        return
    
    if stop:
        res['response']['text'] = "Слон продан, возвращайтесь позже!"
        res['response']["end_session"] = True
        return
    if not slon:
        res['response']['text'] = aut(user_id, req['request']['original_utterance'])
        return 
    # Обрабатываем ответ пользователя.
    if req['request']['original_utterance'].lower() in [
        'ладно',
        'куплю',
        'покупаю',
        'хорошо',
    ]:
        # Пользователь согласился, прощаемся.
        res['response']['text'] = 'Слона можно найти на Яндекс.Маркете!\n А чтобы сыграть ещё раз просто скажите: "Алиса, давай поиграем в купить слона"'
        return

    if req['request']['original_utterance'].lower() in [
        'нет',
        'неа',
    ]:
        res['response']['text'] = 'Не нет, а да. Купи слона!'
        return
    
    # Если нет, то убеждаем его купить слона!
    res['response']['text'] = 'Все говорят "%s", а ты купи слона!' % (
        req['request']['original_utterance']
    )
    res['response']['buttons'] = get_suggests(user_id)

# Функция возвращает две подсказки для ответа.
def get_suggests(user_id):
    session = sessionStorage[user_id]

    # Выбираем две первые подсказки из массива.
    suggests = [
        {'title': suggest, 'hide': True}
        for suggest in session['suggests'][:2]
    ]

    # Убираем первую подсказку, чтобы подсказки менялись каждый раз.
    session['suggests'] = session['suggests'][1:]
    sessionStorage[user_id] = session

    # Если осталась только одна подсказка, предлагаем подсказку
    # со ссылкой на Яндекс.Маркет.
    if len(suggests) < 2:
        suggests.append({
            "title": "Ладно",
            "url": "https://market.yandex.ru/search?text=слон",
            "hide": True
        })

    return suggests