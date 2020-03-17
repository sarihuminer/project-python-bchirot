import Address


class Person:
    def __init__(self, id, first_name, last_name, numhouse, street, city):
        self.Id = id
        self.first_name = first_name
        self.last_name = last_name
        self.addres = Address.Addres(numhouse, street, city)
