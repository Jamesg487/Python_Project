class Owner:

    def __init__(self, name, address, email, telephone, id = None):
        self.name = name 
        self.address = address
        self.email = email
        self.telephone = telephone
        self.id = id
        self.pets = []


    def add_pet(self, pet):
        self.pets.append(pet)