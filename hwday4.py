
#Homework day 4 Thursday January 16th 2020


# Small

#1 Madlib function

# def madlib(name, subject):
#     result = (f"{name}\'s favorite subject is {subject}.")
#     return result

# print(madlib("Jaye", "Science"))


#2 Celsius to Farenheit conversion

# def convertTemp(C):
#     F = (C * 9/5) + 32
#     return F

# print(convertTemp(24))


#3 Farenheit to Celsius conversion

# def convertTemp(F):
#     C = (F - 32) * 5/9
#     return C

# print(convertTemp(70))


# #4 is_even

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(13))

# #5 is_odd

# def is_odd(is_even):
#     if is_even == True:
#         return False
#     else:
#         return True
# print(is_odd(is_even))

#6 only_evens

# def only_evens(list_of_numbers):
#     even_numbers = []
#     for i in list_of_numbers:
#         if (i % 2) == 0:
#             even_numbers.append(i)
#     return(even_numbers)

# print(only_evens([23, 454, 32, 35, 122, 334, 5]))


#7 only_odds

# def only_odds(list_of_numbers):
#     odd_numbers = []
#     for i in list_of_numbers:
#         if (i % 2) != 0:
#             odd_numbers.append(i)
#     return(odd_numbers)

# print(only_odds([23, 454, 32, 35, 122, 334, 5]))

# Medium


#1 Find the smallest number

# def smallest(list_nums):
#     return min(list_nums)
# print(smallest([2, 45, 6, 7, 89]))


#2 find the largest number

# def largest(list_nums):
#     return max(list_nums)
# print(largest([2, 45, 6, 7, 89]))


#3 Find the shortest String

# def shortest(string):
#     return (min(string, key=len))
# print(shortest(['cat', 'jack', 'it']))


#4 Find the longest string

# def longest(string):
#     return (max(string, key=len))
# print(longest(['cat', 'jack', 'it']))