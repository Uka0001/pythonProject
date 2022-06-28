
user = {"username": "oleksii",
		"city": "Kharkiv",
		"birthdate": "20.10.1990",
		"phones": {"sim1": {"operator": "MTC", "phone_number": "+38099"},
					"sim2": {"operator": "Life", "phone_number": "+38099"},
					"sim3": {"operator": "Life", "phone_number": "+38099"}
		}}

print(type("username"))

del user["phones"]["sim3"]

user["phones"]["sim2"]["operator"] = "New operator"
