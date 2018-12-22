pizzas = ['hawaiian', 'pepperoni', 'cheese', 'yellow', 'blue']

for pizza in pizzas:
    print("I like " + pizza + " pizza")

print("I really like pizza")

#for pizza in pizzas[:3]:
    #print(pizza)

i = int(len(pizzas)/2)

for pizza in pizzas[i:i+3]:
    print(pizza)
