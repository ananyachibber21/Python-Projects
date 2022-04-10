# Creating a Dictionary using python

import json
from difflib import get_close_matches

#converting json file to python
data = json.load(open("data.json"))

print("--------------- Welcome to My Dictionary ---------------")

def func(word):
    word = word.lower()
    if(word in data):
        return data[word]
    elif(word.title() in data):
        return data[word.title()]
    elif(word.upper() in data):
        return data[word.upper()]
    elif(len(get_close_matches(word, data.keys()))>0):
        print("Do you mean %s ?" %get_close_matches(word, data.keys())[0])
        choice = input("yes/no?")
        if(choice == "yes"):
            return data[get_close_matches(word, data.keys())[0]]
        elif(choice == "no"):
            print("Sorry the data is not present in the dictionary. Please try again!")
        else:
            print("You have entered a wrong input. Please enter yes or no!")        
    else:
        print("Sorry the data is not present in the dictionary. Please try again!")

word = input("Enter a word you want to search: ")
dictionary = func(word)
if(type(dictionary) == list):
    for i in dictionary:
        print(i)
else:
    print(dictionary)

