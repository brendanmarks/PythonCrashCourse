filename = 'programming.txt'
with open(filename, 'w') as file_object: #set to write mode
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

with open(filename, 'a') as file_object: #set to append mode (doesn't write over exiting)
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
