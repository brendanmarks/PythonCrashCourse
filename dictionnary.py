person = {'skin colour':'white', 'GPA':'3.7', 'Wants to kill himself':'yes'}

for att in person:
    print(att + " " + person[att])

person['SO MAD']= 'true'

del person['skin colour']

for att in person:
    print(att + " " + person[att])

#better print method

for key, value in person.items():
    print( "\n" + key )
    print(value)
for key in person.keys():
    print(key.title())

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in sorted(favorite_languages.keys()):
     print(name)

for language in favorite_languages.values():
    print(language)

#to not print duplicates
for language in set(favorite_languages.values()):
    print(language)
