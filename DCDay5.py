
# phone_book = {
#     "Jacob" : "281-444-5555",
#     "Police" : "911",
#     "Austin" : "713-456-9873"
# }

# print(phone_book["Austin"])

# isItThere = "Police" in phone_book
# print(isItThere)

# phone_book["Austin"] = "713-432-4566" #changes austin value
# print(phone_book["Austin"])

# keys = phone_book.keys()
# # print(keys)

# for key in keys :
#     print(f"{key}'s phone number is {phone_book[key]}")

# print(phone_book["Police"])
# # del phone_book["Police"]
# print(phone_book["Police"])

# items = phone_book.items() #.items makes a list of tuples

# for key, value in phone_book.items(): #iterating
#     print(f"{key}: {value}")

# contacts = [{
#     "firstname": "Jaye",
#     "lastname": "Jensen", 
#     "phone": {
#         "cell" : "281-444-5555",
#         "home" : "713-555-6666"
#         }
#     }, {
#     "firstname": "Austin",
#     "lastname": "Denny"
#     }, {
#     "firstname": "Daniel",
#     "lastname": "Dolan"
#     }]


# fullname = (contacts[0]["firstname"] + " " + contacts[0]["lastname"])

# print(fullname)


# print(contacts[0]["phone"]["cell"])


# contact = [
#     {
#         'first_name': 'Phillip',
#         'last_name': 'Guo',
#         'email': 'phillip.guo@gmail.com',
#         'phone':{
#             'work':'837-494-3948',
#             'cell': '234-897-4933'
#         }
#     },
#     {
#         'first_name': 'Mark',
#         'last_name': 'Guzdial',
#         'email': 'mark.guzdial@gatech.edu',
#         'phone':{
#             'work':'484-569-3466',
#             'cell': '493-485-9845'
#         }
#     }
# ]

# print(contact[0]['phone']['work'])