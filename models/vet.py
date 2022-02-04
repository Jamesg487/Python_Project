class Vet:

    def __init__(self, name, species_specialism, id = None):
        self.name = name
        self.species_specialism = species_specialism
        self.id = id
        self.pets = []


    def add_pet(self, pet):
        self.pets.append(pet)