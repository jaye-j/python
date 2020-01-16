#Homework day 3 Wednesday January 15th 2020


#1 Sum the Numbers

# numbers = [1, 2, 3, 4, 5 ,6]

# print("Sum of numbers is: " + str(sum(numbers)))


#2 Largest Number

# numbers = [1, 2, 4, 43, 5 ,16]

# numbers.sort()

# print(numbers[-1])


#3 Smallest Number

# numbers = [13, 2, 4, 43, 5 ,16]

# numbers.sort()

# print(numbers[0])


#4 Even Numbers

# numbers = [13, 2, 4, 43, 5 ,16]

# for index in numbers :
#     if index % 2 == 0 :
#         print(index)


#5 Positive Numbers

# numbers = [-1, -4, -5, -69, 4, 420, 69, 1337]

# for index in numbers :
#     if index > 0 :
#         print(index)


#6 Positive Numbers II

# numbers = [-1, -4, -5, -69, 4, 420, 69, 1337]
# new_list = []
# for index in numbers :
#     if index > 0 :
#         new_list.append(index)
# print(new_list)


#7 Multiply a list

# numbers = [1, 2, 3 ,420, 69, 1337]
# n = 2
# new_list = []

# for i in numbers :
#     new_list.append(i * n)

# print(new_list)


#8 Reverse a String

# string = "racecar backwards"
# print(string[::-1])

# string = "digital crafts"
# rstring = ""
# for index in range(1,len(string) + 1) :
#     rstring += string[-index]
# print(rstring)


# Medium


#1 Multiply Vectors

# list_1 = [2, 4, 5]
# list_2 = [2, 3, 6]
# newlist = []


# for index in range(len(list_2)) :
#     product = list_1[index] * list_2[index]
#     newlist.append(product)
# print(newlist)


#2 Matrix Addition

# dim1 = [[2, 4], [3, 5]]
# dim2 = [[3, 7], [8, 3]]
# results = []

# for d1_index in range(len(dim1)) :
#     for d2_index in range(len(dim2)) :
#         if d1_index == d2_index:
#             working_list = []
#             sum1 = dim1[d1_index][0] + dim2[d2_index][0]
#             sum2 = dim1[d1_index][1] + dim2[d2_index][1]
#             working_list.append(sum1)
#             working_list.append(sum2)
#             results.append(working_list)
# print(results)

#3 Matrix Addition II

# dim1 = [[12, 44], [33, 65]]
# dim2 = [[43, 67], [89, 33]]
# results = []

# for d1_index in range(len(dim1)) :
#     for d2_index in range(len(dim2)) :
#         if d1_index == d2_index:
#             working_list = []
#             sum1 = dim1[d1_index][0] + dim2[d2_index][0]
#             sum2 = dim1[d1_index][1] + dim2[d2_index][1]
#             working_list.append(sum1)
#             working_list.append(sum2)
#             results.append(working_list)
# print(results)


#4 De-dup

# my_list = [1, 2, 3, 4, 5, 4, 3]
# new_list = []
# for i in my_list :
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


#5 Leetspeak

# paragraph = """What were they eating? It didn't taste like anything she had ever eaten before and
#  although she was famished, she didn't dare ask. She knew the answer would be one she didn't want to hear."""
# paragraph_upper = paragraph.upper()
# para_list = list(paragraph_upper)
# leet_para = []
# leet = {"A" : "4", "E" : "3", "G" : "6", "I" : "1", "O" : "0", "S" : "5", "T" : "7"}

# for letter in paragraph_upper :
#     if letter in leet:
#         letter = leet[letter]
#         leet_para.append(letter)
#     else:
#         leet_para.append(letter)
# result = "".join(leet_para).lower()
# print(result)


#6 Long Vowels

# word = input("Please enter a word: ")
# converted_word = list(word.lower())
# long_word = []

# long_vowels = {"a" : "aaa", "e" : "eee", "i" : "iii", "o" : "ooo", "u" : "uuu"}
# for letter in converted_word:
#     if letter in long_vowels:
#         letter = long_vowels[letter]
#         long_word.append(letter)
#     else:
#         long_word.append(letter)
# result = "".join(long_word)
# print(result)


#7 Caesar Cipher

# def caesar_encrypt(realText, step):
#     outText = []
#     cryptText = []

#     uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#     for eachLetter in realText:
#         if eachLetter in uppercase:
#             index = uppercase.index(eachLetter)
#             crypting = (index + step) % 26
#             cryptText.append(crypting)
#             newLetter = uppercase[crypting]
#             outText.append(newLetter)
#         elif eachLetter in lowercase:
#             index = lowercase.index(eachLetter)
#             crypting = (index + step) % 26
#             cryptText.append(crypting)
#             newLetter = lowercase[crypting]
#             outText.append(newLetter)
#         else:
#             outText.append(" ")

#     return "".join(outText)

# code = caesar_encrypt('lbh zhfg hayrnea jung lbh unir yrnearq', 13)

# print(code)





