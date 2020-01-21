
# class greeting:
#     def say_Hello(self):
#         print('Hello')

# class person:
#     def __init__ (self, name):
#         self.name = name
#         self.count = 0

# newGreetingObj = greeting()

# newGreetingObj.say_Hello()

# class student:
#     def __init__(self):
#         print('constructor called')

#     def morningGreet(self):
#         print('Good morning.')

# Jaye = student()

# Jaye.morningGreet()

# myname = str("jaye")

# capName = myname.capitalize()
# print(capName)

# class Animal:
#   def __init__ (self, name):
#     self.name = name

# dog = Animal("Lucy")

# cat = Animal("Puppy")

# horse = Animal("Stallion")

# print(dog.name)
# print(cat.name)
# print(horse.name)

# class student:
#     def __init__ (self, fname, lname):
#         self.fname = fname
#         self.lname = lname

# Jaye = student("Jaye", "Jensen")

# Austin = student("Austin", "Denny")

# Daniel = student("Daniel", "Dolan")

# print(Jaye.fname)
# print(Austin.fname)
# print(Daniel.fname)


# class Warrior:
#     def __init__(self, classname, weapon):
#         self.classname = classname
#         self.weapon = weapon

# class Mage:
#     def __init__(self, classname, element):
#         self.classname = classname
#         self.element = element

# class Warlock:
#     def __init__(self, classname):
#         self.classname = classname

# class Bard:
#     def __init__(self, classname):
#         self.classname = classname


# Player1 = Warrior("Warrior", input("What weapon will you weild? "))
# Player2 = Mage("Mage", "Fire")
# Player3 = Warlock("Warlock")

# print(f"Player One is a {Player1.classname} weilding a {Player1.weapon}")
# print(f"Player Two is a {Player2.element} {Player2.classname}")
# print(f"Player Three is a {Player3.classname}")

# import datetime

# class Person:
#     def __init__(self, fname, lname, birthdate, address, email):
#         self.fname = fname
#         self.lname = lname
#         self.birthdate = birthdate
#         self.address = address
#         self.email = email

#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year

#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1

#         return age


# sammy = Person("Sammy", "Kry", datetime.date(1998, 8, 21),"123 street", "sammy@gmail.com")

# print(sammy.fname)
# print(sammy.birthdate)
# print(f'{sammy.fname} {sammy.lname}')

# age = sammy.age()

# print(f'{sammy.fname} {sammy.lname} is {age}')


# def greeting(name):
#     count = 0
#     print(f"Hello {name}")
#     count += 1
#     print(count)

# greeting("Jaye")
# greeting("Austin")
# greeting("Daniel")
# greeting("Sammy")

# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.count = 0

#     def greeting(self):
#         print(f"hello {self.name}")
#         self.count += 1

#     def printCount(self):
#         print(self.count)

# Jaye = Person("Jaye")

# Jaye.greeting()
# Jaye.printCount()
# Jaye.greeting()
# Jaye.printCount()

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

# class JString(str):

#     def reverse(self, name):
#         rstring = ""

#         for char in name:
#             rstring = char + rstring

#         return rstring

# myString = JString("hello")
# print(myString.capitalize())

# reversed = myString.reverse("hello")

# print(reversed)

# *******************************************

# class Character:
#     def __init__(self, name, power, health):
#         self.name = name
#         self.power = power
#         self.health = health

# class Hero(Character):
#     def __init__(self, weapon, name, power, health):
#         self.weapon = weapon
#         super(Hero, self).__init__(name, power, health)

# jaye = Hero("Excalibur", "Sir Jaye", 80, 100)

# print(jaye.name)
