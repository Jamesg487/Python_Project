class Pet:

    def __init__(self, name, vet, owner, date_of_birth, species, treatment_notes, nervous, id = None):
        self.name = name
        self.vet = vet
        self.owner = owner
        self.date_of_birth = date_of_birth
        self.species = species
        self.treatment_notes = treatment_notes
        self.nervous = nervous
        self.id = id