# list1 = []
# list2 = []

# str1 = input("Input a string of characters... ")
# str2 = str1 + input("Enter an additional character... ")

# for i in str1:
#     list1.append(i)
# for i in str2:
#     list2.append(i)

# if  len(list2) > len(list1):
#     print(list2[len(list1)])
str1 = input()
str2 = input()


def difference(str1, str2):
    for char in str2:
        if char in str1:
            pass
        else:
            return char


difference(str1, str2)