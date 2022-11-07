# College Simulation

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.addresses = [address]

    def __repr__(self):
        return f'Person("{self.name}",{self.age})\nADDRESS:{self.addresses[0]}'

    def add_address(self, new_address):
        self.addresses.append(new_address)

    def get_all_addresses(self):
        return self.addresses


class Student(Person):
    def __init__(self, name, age, address ,college_course):
        Person.__init__(self, name, age, address)
        self.college_course = college_course

    def __repr__(self):
        return f'Student({self.name}, {self.age}, {self.college_course})'

    def home_address(self):
        return self.addresses[0]

    def college_address(self):
        if (len(self.addresses) == 1):
            return self.home_address()
        else:
            return self.addresses[1]



class Address:
    alladdress = []
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


myaddress1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
myaddress2 = Address("104", "enchcourt", "randale", "alway", "91K7P1")

p1 = Student("John", 36, myaddress1, "Computer Science")

p1.add_address(myaddress2)

print(p1.college_address())

