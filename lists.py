guests = ['brendan', 'john', 'mark']

print("Come to my dinner " + guests[0].title())

print(guests[1].title() + " can't come")

del guests[1]
guests.insert(1, 'benny blanco')

print(guests[1].title() + " is now coming")

print("I found a bigger table!")

guests.insert(0, 'bob')
guests.insert(2, 'bill')
guests.append('john')
i = 0
for x in guests:
    print("Come to my dinner " + guests[i].title())
    i = i+1
