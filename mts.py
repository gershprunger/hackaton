import picle

def save(sost, user):
	picle.dump(sost, "user/"+user)

def load(user):
	return picle.load(file)
	
def get_sost(user, pole):
	return load(user)[pole] 
	
def set_sost(user, pole, sost):
	h = load(user)
	h[pole] = sost
	save(h, user)
	
def aut_set_sost(user, name, sost):
	h = load(user)
	h["aut"][name] = sost
	save(h, user)

def aut_get_sost(user, name):
	h = load(user)["aut"]
	if name in h:
		return h[name]
	else:
		return -1	
		
def qu_set_sost(user, name, sost):
	h = load(user)
	h["qu"][name] = sost
	save(h, user)

def qu_get_sost(user, name):
	h = load(user)["qu"]
	if name in h:
		return h[name]
	else:
		return -1

def first_aut(user):
	h = get_sost(user, "aut")
	for i in range(len(h)):
		h[i] = 0
	set_sost(user, "aut", h)
	set_sost(user, "last_name", 0)
	return "Скажите своё имя"
	
def aut(user, s):
	ln = get_sost(user, "last_name")
	if ln == 0:
		h = get_sost(user, "aut")
		if s in h:
			ln = s
			
	if sost_now == "unknow":
		set_sost(user, pole, "who")
		return "Скажите своё имя"
	elif sost_now == "who":
		if 
		return "Скажите своё имя"
	