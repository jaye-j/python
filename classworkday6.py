class Person: 
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1
    
    def print_contact_info(self):
        print(f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def num_friends(self):
        print(f'{self.name} has {len(self.friends)} friend(s).')

    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)



sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)
sonny.add_friend('Joe')
print(f'Sonny\'s contact info: {sonny.email}, {sonny.phone}')
print(f'Jordan\'s contact info: {jordan.email}, {jordan.phone}')
sonny.print_contact_info()
sonny.friends.append(jordan)
jordan.friends.append(sonny)
print(f'{jordan.name} has {len(jordan.friends)} friend(s).')
sonny.num_friends()

sonny.greet(jordan)
print(sonny.greeting_count)
print(sonny)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.make, self.model, self.year)
    

car = Vehicle('Mazda', 'Mazda3', 2011)
print(car.make, car.model, car.year)
car.print_info()


