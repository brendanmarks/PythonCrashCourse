with open('pi_digits.txt') as file_object:
    #with open('text_files\filename.txt') as file_object: for longer path/ file in different directory
        #or
    #file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
    #with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

filename = 'pi_digits.txt' #to print line by line
with open(filename) as file_object:
    lines = file_object.readLines() #making list of lines
    for line in file_object:
        print(line)

filename = 'pi_million_digits.txt' #this file doesnt exist
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...") #limit numbers printed
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ") #checking if your birthday appears in the million digits of pi 
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
