users = [
    {
        "user_id": 777,
        "username": "Freg",
        "user_level": 2
    },
    {
        "user_id": 383,
        "username": "Oleg",
        "user_level": 1
    },
    {
        "user_id": 918,
        "username": "Anna",
        "user_level": 3
    }
]

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
req_from_server = {"user_id": 383, "text": "change"}


# prepare_message(req_from_server) - так не комельфо

def prepare_message(usr):
    level = search_user_lvl(usr)
    text_list = search_text(level, usr)
    if len(text_list) == 0:
        return None
    return '\n'.join(text_list)


def search_text(level, usr):
    output = []
    for sentence in sentences:
        if level == sentence.get('level'):
            if usr.get('text') in sentence.get('text'):
                output.append(sentence.get('text'))
    return output


def search_user_lvl(user):
    for i in users:
        u_id = i.get("user_id")
        if user.get('user_id') == u_id:
            return i.get('user_level')


# Завершаем вот здесь
def send_message(message):
    # Вместо принта, а будущем ,у нас будет логика отправки сообщения на сервера Телеграм
    print(message)

message = prepare_message(req_from_server)
send_message(message)