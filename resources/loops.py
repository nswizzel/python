persons = [
  {
    "name": "Alice",
    "friends": ["Tom", "Jerry"]
  },
    {
    "name": "Bob",
    "friends": ["Sara", "Lara", "Zara"]
  }
]

for person in persons:
    print('Best friend of ' + person["name"] + ' is:')
    for key, value in person.items():
      if key == "friends":
        for friend in value:
          print(friend)
          break

for person in persons:
    print('Other Friends of ' + person["name"] + ' are:')
    for key, value in person.items():
      if key == "friends":
        for friend in value:
          if(friend == value[0]):
            continue
          print(friend)


i = 1
while(i<=5):
  j = 1
  while(j<=10):
    print(i,' x ', j, ' = ', i*j)
    j+=1
  i+=1