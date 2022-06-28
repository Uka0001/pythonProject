"""
task4-1
"""
user_dict {	"user_pic" : user.jpg,
			"tel_user" : 380997777777,
			"user_number" : 1,
			"name" : "name of the user", 
			"studyEngBefore" : True|False, #Boolean (Yes|No)
			"user_level" : "Beginner", #["Beginner", "Elementary", "Intermediate", "Upper-Intermediate", "Advanced", "Proficiency"], #массив значений
			}

sentence_dict {"user_sentence" : "user sentence input",
				"level_sentence" : "Hard", # Hard > 20 words, Middle > 10 & 20 <, Easy < 10
				"teme_sentence" : "Sience",
				}

"""
Task4-2
"""
armor_dict {"nameArmor" : "Helmet",
			"pictureArmor" : helmet.jpg,
			"defenceInMelee" : "100",
			"defenceInLongRangeBattle" : "100",
			"weight" : 1,
			}

weapons_dict {"nameWeapon" : "Axe",
			"pictureWeapon" : axe.jpg,
			"typeOfWeapon" : True|False #True - magical, False - nonMagical
  			"damageOfWeapon" : 150,
  			"Magic damage" : if "typeOfWeapon" = True then 100 else 0,
  			"weight" : 2,
			}
character_dict {"nameCharacter" : "Nagibator8A:)",
				"race" : {"raceOne" : "Human",
						"raceTwo" : "Ork",
						"raceThree" : "Elf",
						"raceFour" : "Dark"},

				"level" : 30,
				"health" : 400,
				"mana" : 300,
			}
"""
Task4-3
"""
character_dict {"nameCharacter" : "Nagibator8A:)",
				"exampleName" : "ExamleValue",
				"race" : {"raceOne" : "Human",
						"raceTwo" : "Ork",
						"raceThree" : "Elf",
						"raceFour" : "Dark"},

				"level" : 30,
				"health" : 400,
				"mana" : 300,
				"weapons_dict" : {"nameWeapon" : "Axe",
								"pictureWeapon" : axe.jpg,
								"typeOfWeapon" : True|False #True - magical, False - nonMagical
					  			"damageOfWeapon" : 150,
					  			"Magic damage" : if "typeOfWeapon" = True then 100 else 0,
					  			"weight" : 2},
				"armor_dict" : {"nameArmor" : "Helmet",
								"pictureArmor" : helmet.jpg,
								"defenceInMelee" : "100",
								"defenceInLongRangeBattle" : "100",
								"weight" : 1},
			}
nameCharacter = character_dict["nameCharacter"]
print(nameCharacter)
nameCharacter = character_dic.get("weapons_dict")
character_dict["nameCharacter"] = "NagibatorNew9A:)"
print(character_dic.get("nameCharacter"))
del character_dict["exampleName"]

