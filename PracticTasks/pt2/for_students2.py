"""
Данные, которые у нас имеются в начале работы:
1. Список пользователей нашего бота
"""
users = [{
		   "user_id":777,
		   "username": "Freg",
		   "user_level":2
		  },
		  {
		  	"user_id":383,
		  	"username": "Oleg",
		 	"user_level":1},
		  {
		  	"user_id":918,
		  	"username": "Anna",
		  	"user_level":3
		  }]

# 2. Набор предложений
sentences = [
	{"text": "When my time comes \n Forget the wrong that I’ve done.", 
	"level": 1},
	{"text": "In a hole in the ground there lived a hobbit.", 
	"level": 2},
	{"text": "The sky the port was the color of television, tuned to a dead channel.", 
	"level": 1},
	{"text": "I love the smell of napalm in the morning.", 
	"level": 0},
	{"text": "The man in black fled across the desert, and the gunslinger followed.", 
	"level": 0},
	{"text": "The Consul watched as Kassad raised the death wand.", 
	"level": 1},
	{"text": "If you want to make enemies, try to change something.", 
	"level": 2},
	{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2}
]

# 3. Сообщение с сервера, где указано от юзера с каким ID прилетел запрос и какое слово он ищет
req_from_server = {"user_id":383, "text":"in"}

def get_user(id):
	"""
	@param id: int, ...
	@return: dict, ...
	"""	
	for user in users:
		if id == user.get("user_id"):
			return user
	return {}	


# user_dict = {}

# for user in users:
# 	if req_from_server.get("user_id") == user.get("user_id"):
# 		user_dict = user
# 		break

def get_list_sentence(lvl,text):
	list_sentence = []

	for sentence in sentences:
		sentence_text = sentence.get("text")
		if lvl == sentence.get("level"):
			if text in sentence_text:
				list_sentence.append(sentence_text)
	return list_sentence
				

# for sentence in sentences:
# 	sentence_text = sentence.get("text")
# 	if user_dict.get("user_level") == sentence.get("level"):
# 		if req_from_server.get("text") in sentence_text:
# 			list_sentence.append(sentence_text)

def create_message (list_sentence):

	if len(list_sentence) == 0:
		return "No result"

	if len(list_sentence) == 1:
		return list_sentence[0]

	message = ''
	for x in list_sentence:
		message += f"{x}\n ... \n"
	
	return message


""" 
Здесь ваш код. 
Используйте наработки предущей практической и последних занятий, чтоб завернуть его в функции


На выходе мы должны получить словарь вида
{user_id: 123, text: "blah-blah-blah \n ... \n anothe blah-blah-blah"}, 
где:
text - это одна большая строка, в которой содержаться английские предложения (либо сообщение, что результат не найден)
user_id - это id юзера, от которого нам прилетело сообщение, и на который мы же отправляем ответ
"""


def prepare_message(req_from_server):
	"""
	@param req_from_server: dict[int,str]
	@return: dict[int,str]
	"""	

	user_dict = get_user(req_from_server.get("user_id"))

	list_sentence = get_list_sentence(user_dict.get("user_level"),req_from_server.get("text"))

	message = create_message (list_sentence)

	return {"user_id": user_dict.get("user_id"), "text": message}

# Результирующее сообщение должно готовиться функций типа prepare_message (название можете выбрать сами)


# Завершаем вот здесь
def send_message(message):
	# Вместо принта, а будущем ,у нас бreq_from_serverудет логика отправки сообщения на сервера Телеграм
	print(message)



message = prepare_message(req_from_server)

send_message(message)


