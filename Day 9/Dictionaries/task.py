programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    123: "Numbers"
}


# print(programming_dictionary['Bug'])
# print(programming_dictionary[123])

programming_dictionary['Loop'] = 'The action of doing something over and over agian.'
# print(programming_dictionary)

# empty_dictionary = {}
# empty_dictionary[]

# wipe an existing dictionary
colors = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

colors = {}
# print(colors)

# edit an item in a dictionary
programming_dictionary['Bug'] = "A moth in your computer."
# print(programming_dictionary)


# loop through a dictionary
# gives you only the keys in the dictionary
for key in programming_dictionary:
    print(key)  #to get the key
    print(programming_dictionary[key]) #to get the value
