people = []

for person in range(0,11):
    newPerson = {'skin colour':'white', 'GPA':'3.7', 'Wants to kill himself':'yes'}
    people.append(newPerson)

for person in people:
    print(person)


pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
 "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
 }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },

 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
