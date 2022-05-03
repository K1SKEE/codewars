'''Description:
Move all exclamation marks to the end of the sentence

Examples
remove("Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!!"
remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"'''


def remove(s):
    return s.replace('!', '') + '!'*s.count('!')


print(remove("Hi!"))
print(remove("Hi! Hi!"))
print(remove("Hi! Hi! Hi!"))
print(remove("Hi! !Hi Hi!"))
print(remove("Hi! Hi!! Hi!"))