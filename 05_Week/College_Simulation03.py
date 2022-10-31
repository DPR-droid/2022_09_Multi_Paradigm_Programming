# Modify the program such that the Student has methods to access their home address and college
# address. This should use the list from the parent class. If there is only 1 address then the college
# address will be the same as the home address.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.__list_of_addresses = []

    def __repr__(self):
        return f'Person("{self.name}",{self.age})\nADDRESS:{self.address}'
        #return str(self)

class Address:
    def __init__(self, house_number, street, town, county,
        eircode, country="Ireland"):
        self.house_number = house_number
        self.street = street
        self.town = town
        self.county = county
        self.eircode = eircode
        self.country = country

    def __repr__(self):
        string = "\n"
        string += f'{self.house_number} {self.street},\n{self.town},\n{self.county},\n{self.eircode},\n{self.country}'
        return string

class Student(Person):
    def __init__(self, name, age ,college_course):
    
        Person.__init__(self, name, age)
        self.college_course = college_course

    def __repr__(self):
        return f'Student({self.name}, {self.age}, {self.college_course})'


#######################################################################################################
# # Modify the Person class, from the lecture notes, such that a person can have multiple addresses. You
# # can use a list for this purpose. Add a method to the Person class to add a new address.
# myaddress1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
# myaddress2 = Address("104", "enchcourt", "randale", "alway", "91K7P1")

# p1 = Person("John", 36, [myaddress1,myaddress2])
# print(p1)
#######################################################################################################

#######################################################################################################
# # Modify the Student class to extend the Person class which has been modified above. This means the
# # student should send an address to the parent class
# class Student(Person):
#     def __init__(self, name, age, address ,college_course):
    
#         Person.__init__(self, name, age, address)
#         self.college_course = college_course

#     def __repr__(self):
#         return f'Student({self.name}, {self.age}, {self.college_course}, {self.address})'

# myaddress1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
# myaddress2 = Address("104", "enchcourt", "randale", "alway", "91K7P1")

# p1 = Student("John", 36, [myaddress1,myaddress2] ,"Computer Science")

# print(p1)
#######################################################################################################

#######################################################################################################
# Modify the program such that the Student has methods to access their home address and college
# address. This should use the list from the parent class. If there is only 1 address then the college
# address will be the same as the home address.

p1 = Student("John", 36, "Computer Science")

p1.homeaddress = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
p1.studentaddress = Address("104", "enchcourt", "randale", "alway", "91K7P1")

print(p1)
print(p1.homeaddress)
print(p1.studentaddress)
#######################################################################################################