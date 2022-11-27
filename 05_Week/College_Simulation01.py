# College Simulation

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        #self.__list_of_addresses = []
        self.address = address

    def __repr__(self):
        return f'Person("{self.name}",{self.age})\nADDRESS:{self.address}'
        #return str(self)

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

#######################################################################################################
# Modify the Person class, from the lecture notes, such that a person can have multiple addresses. You
# can use a list for this purpose. Add a method to the Person class to add a new address.
myaddress1 = Address("94", "Frenchcourt", "Orandale", "Galway", "H91K7P1")
myaddress2 = Address("104", "enchcourt", "randale", "alway", "91K7P1")

p1 = Person("John", 36, [myaddress1,myaddress2])
print(p1)
#######################################################################################################