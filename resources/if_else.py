person = {
  "name": "Alon",
  "gender": "M",
   "age": 27
  # "age": None
}

# person = {}
if person: 
  print("Person exists!")
else: 
  print("Person doesn't exist!")

#if elif else
if person["age"] > 25: 
  print("Age is greater than 25")
elif person["age"] == 25: 
  print("Age is 25")
else: 
  print("Age is less than 25")

# nested conditions
if "age" in person.keys() and "gender" in person.keys():
  if person["age"] > 18 and person["gender"] == "M": 
    print("Eligible for race")
  else: 
    print("Not eligible for race")
else: 
  print("Age and gender was not provided")

