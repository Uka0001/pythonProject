def process_message(user_id, message_text, user_level):
	# Process text - message_text
	print(f"Try add to DB message from user. User ID: {user_id}, message_text: {message_text}")

# process_message(1923434, "describe", 2)
# process_message("describe", 2, 1923434)

def signup(username, email, password):
	# write new user into DB
	print(f"Adding new user to DB : User Username: {username}, user_email: {email}, password:{password}")

# signup("egor", "egor@gmail.com", "wbr^dsd_55")
# signup("egor", "wbr^dsd_55", "egor@gmail.com")


def process_message(user_id=None, message_text=None, user_level=None):
	print(f"Try add to DB message from user. User ID: {user_id}, message_text: {message_text}")

# process_message(user_id=1923434, message_text="describe", user_level=2)
# process_message(message_text="describe", user_level=2, user_id=1923434)


def signup(username="Egor", email="egor@gmail.com", password=None):
	print(f"Adding new user to DB : User ID: {username}, user_email: {email}, password:{password}")

# signup()
# signup(email="str@gmail.com")
# signup(email="str@gmail.com", password=81212)

def signup(username:str="Egor", email:str="egor@gmail.com", password:str=None):
	print(f"Adding new user to DB : User ID: {username}, user_email: {email}, password:{password}")

# signup()


def signup(username:str="Egor", email="egor@gmail.com", password=None)->None:
	print(f"Adding new user to DB : User ID: {username}, user_email: {email}, password:{password}")

# signup()


def signup(username:dict="Egor", email:None="egor@gmail.com", password=None)->str:
	print(f"Adding new user to DB : User ID: {username}, user_email: {email}, password:{password}")



# signup()
signup("Zero", None)


#positional, named - structs?


def signup(**kwargs):
	print(type(kwargs))

# signup()
# signup("str@gmail.com", password=81212, vabababa=True, aaa=False)
# ** email="str@gmail.com", password=81212, vabababa=True, aaa=False
# {"email":"str@gmail.com", "password":81212, "vabababa":True}
# signup("Zero", None)



# ------------- PACK/UNPACK --------------

user = {"username": "Myname",
		"user_id": "fie12nrd1212vle;njbvrR",
		"user_level": 2}

# print(**user)
# print({**user})
# print({**user, "email":"testemail@gmail.com", "password": "qwerty"})





def infinite_args(arg):
	print(arg)

# infinite_args(1,2,3)

# infinite_args("Egor", "egor@gmail.com", 12345)


# def infinite_args(*args):
# 	print(type(args))

# infinite_args("Egor", "egor@gmail.com", 12345)


def process_message(user, *args, **kwargs):
	print("position arg:",user)
	print("args:", args)
	print("kwargs:", kwargs)

process_message(user, 1,2,3,55,44,333, prioritet=0)