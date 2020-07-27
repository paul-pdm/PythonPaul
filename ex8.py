formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I don't",
    "exactly know",
    "what the format",
    "function does",
    "but it looks like it can call string variables"
))
