types_of_people = 10
x = f"There are {types_of_people} types of people."
# Looks like there's a new way for python to call variables
# in a string.  I like it.  It's more explict compared to
# python 2.xx.  This also takes out the guess work with
# dealing with different data types
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")
# The print statement is also pretty straight forward too
# there's this new 'f';{} notation when calling a variable
# within a string

hilarious = False
joke_evaluation = "Isnt that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "this is the left side of ..."
e = "a string with a right side."

print(w+e)
