
#Homework day 5 Friday January 17th 2020

#Medium


#1 Letter Summary 

user_input = input("Please enter a word: ")

empty_dict = {}

for letters in user_input:
    if letters not in empty_dict:
        empty_dict[letters] = 0
    empty_dict[letters] += 1
print(empty_dict)