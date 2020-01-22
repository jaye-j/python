class Student():
    def __init__(self, firstName, lastName, campus):
        self.firstName = firstName
        self.lastName = lastName
        self.campus = campus

    def printStudent(self):
        print(f"{self.firstName} {self.lastName} campus: {self.campus}")

class Campus():
    def __init__(self):
        self.students = []

    def addStudent(self, firstName, lastName, campus):
        temp  = Student(firstName, lastName, campus)
        self.students.append(temp)

    def showCurrentStudent(self):
        for studentObject in self.students :
            print(f"{studentObject.firstName} {studentObject.lastName}\'s campus: {studentObject.campus}")

jaye = Student("Jaye", "Jensen", "Houston")
austin = Student("Austin", "Denny", "Houston")
sean = Student("Sean", "Page", "Chicago")
daniel = Student("Daniel", "Dolan", "Dallas")
sammy = Student("Sammy", "Kry", "Houston")

houston = Campus()
houston.addStudent("Jaye", "Jensen", "Houston")
houston.addStudent("Austin", "Denny", "Houston")
houston.addStudent("Sammy", "Kry", "Houston")

chicago = Campus()
chicago.addStudent("Sean", "Page", "Chicago")

dallas = Campus()
dallas.addStudent("Daniel", "Dolan", "Dallas")

houston.showCurrentStudent()
chicago.showCurrentStudent()
dallas.showCurrentStudent()
