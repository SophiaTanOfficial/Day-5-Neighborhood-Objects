# Level 1:
# Create a class called Student that has two attributes: a name, and a grade.

class Student:
    def __init__(self, thisName, thisGrade):
        self.name = thisName
        self.grade = thisGrade
        self.account = 0

# Now create instances of three different students (student1, student2, and student3).
student1 = Student("Sara", "11")
student1.account = 400000
student2 = Student("Larry", "12")
student3 = Student("Catherine", "10")


# Confirm that the class works by printing out the first student's name.

students = [student1, student2, student3]
for student in students:
    print(student.name)

# Level 2:
# Create a class called School that has three attributes: a name, a type, and a size.

class School:
    def __init__(self, thisName, thisType, thisSize):
        self.name = thisName
        self.type = thisType
        self.size = thisSize
    

# Create instances of three individual schools.

school1 = School("Edison High", "Public High School", "Medium" )
school2 = School("Lincoln Elementary", "Public Elementary School", "Small")
school3 = School("Timothy Christian", "Private", "Large")

# Confirm that the class works by printing out the name and size of the third school.

print(school3.name, school3.size)


# Level 3:
# Create a class called House that has four attributes: an address, a size, a price, and a number of bedrooms.

class House:
    def __init__(self, thisAddress, thisSize, thisPrice, thisRooms):
        self.address = thisAddress
        self.size = thisSize
        self.price = thisPrice
        self.rooms = thisRooms



# Create instances of at least three individual houses using.

house1 = House("78 Lincoln Highway", "Large", 400000, "5")
house2 = House("139 Justice Street", "Small", 100000, "3")
house3 = House("89 Tingley Lane", "Medium", 70000, "4")


# Confirm that the class works by printing out the address and size of the second house.
print(house2.address, house2.size)


# Level 4: (Stretch)
# Put your three students in a list called my_students, your houses in a list for houses, and your schools in a list for schools.

myStudents = [student1, student2, student3]
myHouses = [house1, house2, house3]
mySchools = [school1, school2, school3]

# Iterate over the student list, printing out "_____ is in grade __." For each of the students.
for student in myStudents:
    print(f'{student.name} is in grade {student.grade}.')


# Iterate over the houses list and print out a description for each one. Do the same for your schools lists.
for house in myHouses:
    print(f'This {house.size.lower()} house has {house.rooms} rooms, is located at {house.address}, and costs {house.price}.')


# Level 5: (Stretch)
# Modify your student class above to include a savings_account value for each student. Change your initializers so that the code still runs. 




# Write some code that compares a student and a house, and determines whether or not the student can afford to buy the house. 
for student in myStudents:
    for house in myHouses:
        if student.account >= house.price:
            print("You can afford this house!")
        else:
            print("You can't afford this house.")