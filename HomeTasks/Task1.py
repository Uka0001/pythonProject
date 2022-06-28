#Task 1 - English bot:

name = "name of the user" 
studyEngBefore = True|False #Boolean
user_level = "Beginner" #["Beginner", "Elementary", "Intermediate", "Upper-Intermediate", "Advanced", "Proficiency"] #массив значений
word = "asset"
wordDescription = "Word description from dictionary"

#Task 2 – message:
name = "name"
adress = "adress"
month = [1,2,3,4,5,6,7,8,9,10,11,12]
gasVolume = float #в кубических метрах
message = "Уважаемый {name} по адресу {adress} объем использованного газа за {month}:  {gasVolume}____".format(name = name, adress = adress, month = month, gasVolume = gasVolume)
print(message)


""" print("Hello! I am your English language bot")

name = input("What is your name?")
print("Your name: {name}".format(name = name))

studyEngBefore = True|False #Boolean

studyEngBefore = input("Tell me, have you study English before? (True or False): ")
print("Your answer: {studyEngBefore}".format(studyEngBefore = studyEngBefore)

print("What is your English level?")

from array import *

array_user_level = array(str("u"),["Beginner", "Elementary", "Intermediate", "Upper-Intermediate", "Advanced", "Proficiency"]) #массив значений

if studyEngBefore == True: user_level = input("What is your English level?")
print("Your level is: {user_level}".format(user_level = user_level)
else: print("Your level is: Beginner")
user level = "Beginner"

word = input("What word do you want to know?")
print(f"Your answer: {word}".format(word = word)

wordDescription = "Word description from dictionary"
print(wordDescription) """