# ЦИКЛЫ

########################## FOR #################################
gladiator = {"name":"Gladiator", "year":2000, "actors": ["Russell Crowe", "Joaquin Phoenix"], "sequels":[]}
bladrunner ={"name": "Bladerunner","year":1982, "actors": ["Harrison Ford", "Rutger Hauer"], "sequels": ["Bladerunner 2049"]}
once_in_america = {"name": "Once upon a time in America", "year":1984 , "actors": ["Robert De Niro"," Joe Pesci"], "sequels":[]}
spiderman_2 = {"name": "Spider-Man 2", "actors": ["Tobey Maguire"], "year":2004, "sequels": ["Spider mna 3"]}
nice_guys = {"name":"The Nice Guys", "year":2016, "actors": ["Russell Crowe", "Ryan Gosling"], "sequels":[]}

# Пример списка со словарями
movies = [gladiator, bladrunner, once_in_america, spiderman_2]



"""
Часто нам нужно достать один или несколько элементов из коллекции (последовательности).
И мы можем не знать индекса этого элемента, 
да и задавать в ручную индекс довольно неудобно.
Для этого нам нужен инструмент, позволяющий ПЕРЕБИРАТЬ коллекции.

То есть, если я хочу один за другим напечатать 3 фильма, то сдеаю это так:

print(movies[0])
print(movies[1])
print(movies[2])

Но я ж не могу все время в код руками лазать? 
Мне нужен инструмент автоматизации вот этого вызова элементов одного за другим

Этот инструмент - цикл for 
Он идет по ПОСЛЕДОВАТЕЛЬНОСТЯМ (тупль, список),
и для этого похода использует то, что называется ИТЕРАТОРОМ
ИТЕРАТОР это переменная, которая идет ВНУТРИ цикла 
и принимает значения элементов один за другим.
"""


# for x in [1,2,3]:
# 	# x - это ИТЕРАТОР
# 	print(x)



# for yupyy in movies:
# 	"""
# 	Внутри цикла мы можем то же, что и во всем остальном коде,
# 	только еще и имея доступ к значениям ВНУТРИ цикла.
# 	Например так: 
# 	наш итератор movie принимает последодвательно значения в тупле movies
# 	И каждый новый шаг - movie будет становится одним из словарей-фильмов.
# 	"""
# 	# print(movie)
# 	# Соотетственно мы можем обращаться к переменной как к словарю.
# 	print(yupyy["sequels"])



"""
Соответственно, мы можем использовать цикл for для перебора списка предложений, 
из которых нам нужно выбрать те, которые подохдят по уровню нашему юзеру.
"""



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


# for sentence in sentences:
# 	print(sentence["text"])
# 	print(sentence["level"])

# Но возникает вопрос - а как именно добавить выбор? Не печатать все подряд, а только те ,что удовлетворяют условиям?
# conditions




# Частенько перебор используется для того, чтобы из одних коллекций вытаскивать значения и помещать в другие.

russel_crow_movies = []
for x in movies:
	"""
	Проходимся по существующему списку.
	Делаем проверку на наличие имени актера в списке, содержащемся в словаре.
	Если оно верное, копируюм элемент из стаого списка и добавляем в новый.
	"""
	if "Russell Crowe" in x["actors"]:
		# Добавляем элемент, прошедший проверку в новый список:
		russel_crow_movies.append(x)

# Список был изменен и теперь доступен в обновленном виде
# print("Russel Crow movies:  ",russel_crow_movies)


# Выполнение цикла можно прервать ключевым словом break.

# for x in 1,2,3,4,5,6:
# 	print(x)
# 	if x == 5:
# 		break


user = {"username" : "Egor",
		"id" : 34253234234,
		"level" : "easy"}


# Вот сообщение от него:
message = {"user": user,
		   "message_text": "take"}


sentences = [{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
			  "level": "easy"},
			  {"text":"I learned very early the difference between knowing the name of something and knowing something.", 
			  "level": 2}]



for sentence in sentences:
	if message.get("user").get("level") == sentence.get("level"):
		if message.get("message_text") in sentence.get("text"):
			print(sentence)

