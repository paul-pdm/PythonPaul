from sys import argv
# this inports a function from a python library
script, filename = argv
# I don't really understand this syntax, but I get
# the concept of what it does.  It assigns the filename
# the user inputs into a variable
txt = open(filename)
#the variable/file is then opened

print(f"Here's your file {filename}:")
print(txt.read())
# and here the "file" is opened.. This can probable be done 
# in one line of code 
txt.close()

print("Type the filename again:")
file_again = input(">")
# This is just another way of inputting and opening the
# file

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
