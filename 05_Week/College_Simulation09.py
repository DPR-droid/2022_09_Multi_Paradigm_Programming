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

class CollegeProgramme:

    def __init__(self, name, level, university):
        self.name = name
        self.level = level
        self.university = university
        self.modules = []

    def __repr__(self):
        return f'CollegeProgramme({self.name}, {self.level}, {self.university})'

    def add_module(self, new_module):
        self.modules.append(new_module)

    def is_module_on_programme(self, search_term):
        for module in self.modules:
            if (module.name == search_term):
                return True
            return False

class CollegeModule:

    def __init__(self, name, level, numcredits):
        self.name = name
        self.level = level
        self.numcredits = numcredits

    def __repr__(self):
        return f'CollegeModule({self.name}, {self.level}, {self.numcredits})'


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

hdipda = CollegeProgramme("HDiP in DA", 8, "ATU")
module1 = ("MPP", 8, 5)
module2 = ("MLS", 8, 5)

hdipda.add_module(module1)
hdipda.add_module(module2)

print(hdipda.is_module_on_programme("MPP"))
print(hdipda.is_module_on_programme("No Life"))

