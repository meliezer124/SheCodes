# write a function that accepts a string and produces a dictionary that connects
# between an alphabet letter to the number of times it appears in the string
# Ex: string_to_dictionary("abzz") will return: freq = {'a':1, 'b':1, 'z':2}

# Read the string
# Separate the characters
# Count repetitions of each character
# Create a dictionary to accept characters and repetitions
#     # use a loop.

def string_to_dictionary(string):
    frequency = {}
    for letter in string:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return frequency


print(string_to_dictionary('potato'))
print(string_to_dictionary('poopookaka'))
