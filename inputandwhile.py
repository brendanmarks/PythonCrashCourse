"""
age = input("Enter your age: ")
age = int(age)

print(age)
"""
"""
print("Enter pizza toppings or quit to stop: ")

while True:
    topping = input()
    if topping != "quit":
        print(topping)
    else:
        break
"""
sandwich_orders = []
toppings = []
while True:
    orders = input("Are there anymore orders? ")
    if orders.lower() == "yes":
        customer = input("Whats ur name? ")
        sandwich_orders.append(customer)
        while True:

            topping = input("What u want on it? ")
            toppings.append(topping)
            more = input("Anything else? ")
            if more.lower() == "no":
                sandwich_orders.append(toppings)
                break
    else:
        break

for sandwhich in sandwich_orders:
    print(sandwhich)
    #for topping in toppings:
        #print("\t" + topping)
