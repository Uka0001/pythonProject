'''
Task5 (lection 19/05/2022)
'''
user_dict {	"user_pic" : user.jpg, #user avatar
			"tel_user" : 380997777777, #tel number
			"user_number" : 1, #user number in our database
			"name" : "name of the user",  #name of the user
			"studyEngBefore" : True|False, #Boolean (Yes|No), have the user ever before study english, if no > level_sentence = Easy
			"user_level" : "Beginner", #["Beginner", "Elementary", "Intermediate", "Upper-Intermediate", "Advanced", "Proficiency"], #массив значений
			"sentence_dict" : {"text_sentence" : "user sentence input", #sentence that user send to the bot
							"user_word" : "lawyer", #the world in the sentence that user send to the bot
							"level_sentence" : "Hard", # Hard => 20 words, Middle > 10 & 20 <, Easy =< 10
							"teme_sentence" : "Sience", # Sience, Life, Travel, Commerce, IT, Money, Music, News
							}}

word = user_dict["sentence_dict"]["user_word"] #get word from dict

sentence [  {"easyLevel1" : "Working as a legal aid " + word +  " satisfies both these things."}, #word "lawyer" - https://www.collinsdictionary.com/sentences/english
			{"easyLevel2" : "These reforms are less about " + word +  "s and more about consumers."},
			{"easyLevel3" : "Anything involving courts and " + word +  "s cannot be free."},
			{"mediumLevel1" : "This prompted deliberations between the judge and the trial " + word +  "s about a potential conflict of interest."},
			{"mediumLevel2" : "Look in the upper right-hand corner of the prints, he told the defense " + word +  "s."},
			{"mediumLevel3" : "One of those involved is also understood to have contacted " + word +  "s about a possible claim."},
			{"hardLevel1" : "Crown Prosecution Service " + word +  "s are studying an interim report into a new investigation and cops hope to bring charges next year."},
			{"hardLevel2" : "I am amazed how this can be overturned by " + word +  "s and money people because it is not in their interest."},
			{"hardLevel3" : "Some " + word +  "s and academics say that the Army should no longer have the power to convict soldiers for criminal offences."},
			]

