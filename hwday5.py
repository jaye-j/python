
#Homework day 5 Friday January 17th 2020

#Small

#1


#2 Nested dictionaries

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print(ramit['email'])
# print(ramit['interests'][0])
# print(ramit['friends'][0]['email'])
# print(ramit['friends'][1]['interests'][1])


#Medium


#1 Letter Summary 

# user_input = input("Please enter a word: ")

# empty_dict = {}

# for letters in user_input:
#     if letters not in empty_dict:
#         empty_dict[letters] = 0
#     empty_dict[letters] += 1
# print(empty_dict)


#2 Word Summary

# histogram = {}
# user_input = input("Please enter a sentence: ")
# words = user_input.split()
# for repeats in words:
#     if repeats not in histogram:
#         histogram[repeats] = 0
#     histogram[repeats] += 1
# print(histogram)



#3 Sorting a histogram

# sent_histogram = {}
# entered_sentence = input("Please enter a sentence... ")
# sent_to_words = entered_sentence.split()
# for repeats in sent_to_words:
#     if repeats not in sent_histogram:
#         sent_histogram[repeats] = 0
#     sent_histogram[repeats] += 1
# for key, value in sorted(sent_histogram.items(), key=lambda kv: kv[1], reverse=True):
#     print("%s: %s" % (key, value))