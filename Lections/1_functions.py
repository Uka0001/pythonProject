"""
def function_name(arg):
	тело функции, тот код, который срабатывает при вызове функции.

def - ключевое слово, по которому интерпретатор Python понимает, что дальше пойдет имя функции.

function_name - имя функции, которые нужно, чтобы эту функцию можно было звать по имени
и множество раз переиспользовать в коде.

(arg): - в скобках находятся аргументы - те переменные, которые будут использоваться внутри функции

"""

# Cамая примтивная функция, не делающая вообще ничего.


def function():
	pass 
	#ключевое слово pass служит заглушкой, т.к в теле функции должно быть хоть что-то.

def func():
	print("Hello!")


# print()

# Функция может принимать любое коллиество аргументов, а может - ни одного.
def func(arg):
	print(arg)


"""
Аргументы не обязательно должны обрабатываться в функции. 
Смысла задавать аргументы, а затем не использовать их, нет, 
но технически ничто этому не мешает.
"""

def func(one:str, two:bool): 
	print("one")

"""
Но при вызове обязательно задать значения всех аргументов.
Поэтому вот такой вариант сломаеться:
"""
# func("Hello")

# А вот так - сработает:
# func("Hello", False)


def say_hello(name):
	print(f"Hello {name}")

# say_hello("Artem")
# say_hello("Dasha")


"""
При ВЫЗОВЕ функции она превращается в то, что указано после ключевого слова return
Если такого слова нет, функция, по умолчанию ВОЗВРАЩАЕТ ЗНАЧЕНИЕ None:
"""

# result = say_hello("MyName")
# print(result)
# print(type(result))

# А если return есть - то вызванная функция возвращает значение после return:
def say_hello(name):
	return 56
	# print(f"Hello {name}")

# result = say_hello("Egor")
# print(type(result))
# print(print("b"))

# print(type(say_hello))
# print(type(say_hello("Egor")))

# В теле функции может быть несколько return:
def say_hello(name):
	if type(name) == str:
		return f"Hello {name}"
	else:
		return False


# Внутри функции можно объявлять  вызывать другую функцию, вложенность ничем не ограничена.
def say_hello(name):
	def say_goodbye(name):
		result = f"Goodbye {name}"
		return result
	return say_goodbye(name)

result = say_hello("MyName")
# print(result)

"""
Есть несколько правил, которых стараются придерживаться программисты при написании функций. Они не являются обязательными к выполнению, но сильно помогают в работе.

 - Функции стоит выполнять одно конкретное действие. 
   Три маленьких однострочных функции, чаще всего, лучше, чем одна большая.

 - имя функции должно быть глаголом и обозначать то, что она делает.

 - Имена функций стоит писать в одном стиле.
   в Python это либо CamelCase когда неско слов разделяются большими буквами,
   либо использование нижних подчеркиваний - accounts_from_names  /  AccountsFromNames
   Первый вариант распространен гораздо больше.  
   (во многом еще потому, что камелкейс применяется для именования классов в Питоне, о чем мы поговорим позднее)
"""

# res = (lambda x:x*2)(4)
# print(res)

# Попробуем применить функции для того, чтобы сделать наш код с прошлых лекций более гибким

# user = {"username" : "Egor"
# 		"id" : 34253234234
# 		"level" : 1}

# # Вот сообщение от него:
# message = {"user": user,
# 		   "message_text": "hello"}

# sentences = [{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
# 			  "level": 1},
# 			  {"text":"I learned very early the difference between knowing the name of something and knowing something.", 
# 			  "level": 2}]


# def print_answer(message):
# 	user_level = message.get(user).get("level")
# 	word = message.get("text")

# 	for sentence in sentences:
# 		if user_level >= sentence.get("level"):
# 			if word in sentence.get("text"):
# 				print(sentence)


# print_answer(message)

# def get_matches(message:dict):
# 	result_sentences = []
# 	user_level = message.get(user).get("level")
# 	word = message.get("text")

# 	for sentence in sentences:
# 		if user_level >= sentence.get("level"):
# 			if word in sentence.get("text"):
# 				result_sentences.append(sentence.get("text"))

# 	return result_sentences

# get_matches(message)