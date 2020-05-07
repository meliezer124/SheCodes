## Formatting
#Usual way :
variable = "string"
print("{}".format(variable))
#Using fstring:
print(f"{variable}") # the fstring allows you to remove the .format() and insert variables directly into their spot

#To look at what actions you can take with a type, use help(TYPE). For example:
help(str)

#Can access fields from dictionaries directly from placeholders:
    #Instead of:
person = {'name': 'Jenn', 'age' : 23}
sentence = "My name is {0}, and I am {1} years old".format(person['name'], person['age'])
    #Can do:
print(sentence)
sentence = "My name is {0[name]}, and I am {0[age]} years old".format(person)
print(sentence)
    #Because you're accessing the fields directly, you only need to call the dictionary once in the .format()
#Can access values of a list in the exact same way.
l = ['Jenn', 23]
sentence = "my name is {0[0]}, and I am {0[1]} years old".format(l)
print(sentence)

#Formatting using keywords
sentence = "My name is {name}, and I am {age} years old.".format(name="Jenn", age="30")
print(sentence)

#Can unpack dictionaries directly in string formatting:
sentence = "My name is {name}, and I am {age} years old".format(**person)
print(sentence)

#adding formatting to formatting-- : specifies formatting
for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i) #pads with 0s to reach 2 places
    print(sentence)

#padding to certain number of decimal places
pi = 3.14159266
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

# formatting and printing out dates
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
sentence = '{:%B %d, %Y}'.format(my_date) # look @ documentation to see proper signs
print(sentence)

#when formatting 0 before : is index. Ex:
potatoes = 3
example = "Potatoes {0:02}".format(potatoes)
print(example)
