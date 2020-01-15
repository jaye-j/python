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

dim1 = [[12, 44], [33, 65]]
dim2 = [[43, 67], [89, 33]]
results = []

for d1_index in range(len(dim1)) :
    for d2_index in range(len(dim2)) :
        if d1_index == d2_index:
            working_list = []
            sum1 = dim1[d1_index][0] + dim2[d2_index][0]
            sum2 = dim1[d1_index][1] + dim2[d2_index][1]
            working_list.append(sum1)
            working_list.append(sum2)
            results.append(working_list)
print(results)







