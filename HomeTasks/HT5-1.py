user = {"username": "Egor",
        "level": 1}

message = {"user": user,
           "text": "th"}

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
    {"text": "The Consul watched as Kass-ad raised the death wand.",
     "level": 1},
    {"text": "If you want to make enemies, try to change something.",
     "level": 2},
    {"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore",
     "level": 1},
    {"text": "I learned very early the difference between knowing the name of something and knowing something.",
     "level": 2}
]

matched_sentences = []
result_message = ""


def print_answer(message: dict):
    for i in sentences:
        user_lvl = message.get("user").get("level")
        sentences_lvl = i.get("level")
        user_message = message.get("text")
        sentences_txt = i.get("text")
        if sentences_lvl == user_lvl:
            if user_message in sentences_txt:
                matched_sentences.append(sentences_txt)


print_answer(message)


def get_matches(message: dict):
    result_sentences = []
    user_level = message.get(user).get("level")
    word = message.get("text")

    for sentence in sentences:
        if user_level >= sentence.get("level"):
            if word in sentence.get("text"):
                result_sentences.append(sentence.get("text"))
                return result_sentences


get_matches(message)

if not matched_sentences:
    result_message = "None result"
if len(matched_sentences) == 1:
    result_message = matched_sentences[0]
if len(matched_sentences) > 1:
    for x in matched_sentences:
        result_message += x + "\n...\n"

print(result_message)
