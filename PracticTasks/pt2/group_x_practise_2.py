"""
Данные, которые у нас имеются в начале работы:
1. Список пользователей нашего бота
"""
users = [{
    "user_id": 777,
    "username": "Freg",
    "user_level": 2
},
    {
        "user_id": 383,
        "username": "Oleg",
        "user_level": 1},
    {
        "user_id": 918,
        "username": "Anna",
        "user_level": 3
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
    {"text": "I learned very early the difference between knowing the name of something and knowing something.",
     "level": 2}
]

# 3. Сообщение с сервера, где указано от юзера с каким ID прилетел запрос и какое слово он ищет
req_from_server = {"user_id": 777, "text": "change"}


def find_user_lvl(user_id):
    user_lvl = 1
    for user in users:
        if user_id == user.get("user_id"):
            user_lvl = (user.get("user_level"))
    return user_lvl


def find_sentences(text, user_lvl):
    results = []
    for sentence in sentences:
        if sentence.get("level") <= user_lvl:
            if text in sentence.get("text"):
                results.append(sentence["text"])
    return results


def process_message(req_from_server):
    user_id = req_from_server["user_id"]
    text = req_from_server["text"]
    user_lvl = find_user_lvl(user_id)
    sentence_result = find_sentences(text, user_lvl)
    print(sentence_result)


process_message(req_from_server)
