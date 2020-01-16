

# count = 0
# while count < 3 :
#     print("hello")
#     break



#for variable in sequence (list, range, or string):

# for index in range(11) :
#     print(index)


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# new_list = alphabet[9:16]
# for letter in new_list :
#     print(letter)


# for variable in range(5,10,2):
#     square = (variable + 1) * (variable + 1)
#     print(square)

# students = ["Matt", "Foorkan", "Alex", "Mary"]
# for name in students:
#     print(name)



# for outer_variable in range(1, 11) :
#     for inner_variable in range(1,11) :
#         print(str(outer_variable) + " X " + str(inner_variable) + " = " + str(outer_variable * inner_variable))


# weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
# weekDays = [" Monday", " Tuesday", " Wednesday", " Thursday", " Friday"]
# todo = ["  -Lectures", "  -Homework", "  -Solutions"]

# for outer in weeks :
#     print(outer)
#     for inner in weekDays :
#         print(inner)
#         for innerinner in todo:
#             print(innerinner)


# ---------------------------------------------------------------------------

# def greeting():
#     print("hello world")

# greeting()

# def names():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")


# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# names()

# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# names()

# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# names()

# def cal_avg(param1, param2, param3, param4):
#     sum = param1 + param2 + param3 + param4
#     avg = sum / 4
#     return avg

# result = cal_avg(4, 6, 9, 0)
# print(result)
# print(cal_avg(6, 8, 22, 11))

def cal_avg(num):
    avg = sum(num) / len(num)
    return avg

print("The average is ", cal_avg([1, 2, 3, 4, 5, 6, 7, 8, 9]))

