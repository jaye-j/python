# class Person: 
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#     def greet(self, other_person):
#         print('Hello {}, I am {}!'.format(other_person.name, self.name))

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

# sonny.greet(jordan)
# jordan.greet(sonny)

# print(f'Sonny\'s contact info: {sonny.email}, {sonny.phone}')
# print(f'Jordan\'s contact info: {jordan.email}, {jordan.phone}')

# class Person:
#   def __init__ (self, name):
#     self.name = name
#     self.count = 0

#   def greet (self):
#     self._greet()

#   def _greet (self):
#     self.count += 1
#     if self.count > 1:
#       print("Stop being so nice")
#       self.__reset_count()
#     else:
#       print("Hello", self.name)

#   def __reset_count(self):
#     self.count = 0

# alex = Person("alex")
# alex._greet()
# alex._greet()
# alex._greet()

# class Animal:
#     def __init__ (self, name):
#         self.name = name
# class Dog (Animal):
#     def woof (self):
#         print("Woof")
# class Cat (Animal):
#     def meow (self):
#         print("Meow")

class JString(str):

    def reverse(self, name):
        rstring = ""

        for char in name:
            rstring = char + rstring

        return rstring

myString = JString("hello")
print(myString.capitalize())

reversed = myString.reverse("hello")

print(reversed)

