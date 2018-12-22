try:
    print(5/0)
except ZeroDivisionError: #ZeroDivisionError is what's written in traceback
    print("You can't divide by zero!")



print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try: #avoid error by trying and throwing error
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError: #you could also fail quietly by simply writing "pass"
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
#Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
