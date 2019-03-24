def MTCFit(ask):
    Sovet="Алиса дай совет"
    tren="Алиса я молодец"
    if(ask==Sovet):
        return 1
    if(ask==tren):
        return 2
    else:
       return 3
	   
def MTCSovet(ask):
    print("A: Чем вам помочь?")
    diet="Хочу похудеть"
    tren="tren"    
    if(ask==diet):
        return 1
    if(ask==tren):
        return 2	
    else:
        return 3
def MTCJob(ask):
    print("A: Чем вы хотите поделиться")
    diet="Диета"
    tren="Тренировка"
    if(ask==diet):
        return 1
    if(ask==tren):
        return 2
    else:
       return 3

def MTC(hello):
    print("П:",hello)
    print("А: Привет, что вы хотите?")
    
    while(1):
        #ask="Алиса дай совет"
        ask="Алиса я молодец" 
        res=MTCFit(ask)
        print("p:",ask)
        if (res==1):
            answ="Хочу похудеть"
            print("p:",answ)
            r=MTCSovet(answ)
            if(r==1):
                print("A:Могу предложить следующие диеты")
            if(r==2):
                print("A:Могу предложить следующме тренировки")
        if (res==2):
            answ="Диета"
            r=MTCJob(answ)
            print("p:",answ)
            if(r==1):
                print("A:Сколько калорий вы съели")
                num=5567
                print("A:Сохранила ",num)
                return 0
            if(r==2):
                print("A:Как вы потренировалиль?")
                num=5567
                print("A:Записала ",num)
                return 0
        else:
            print("повторите запрос")
    
hello="Алиса включи МТС Фитнес"
MTC(hello)
