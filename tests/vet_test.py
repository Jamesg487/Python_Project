import unittest
from models.owner import Owner
from models.pet import Pet
from models.vet import Vet

class TestVet(unittest.TestCase):
    
    def setUp(self):
        self.owner = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")
        self.vet = Vet("Bradley Jiles", "Dogs")
        self.pet = Pet("Sir Bites a lot", self.vet, self.owner, "23/03/2003", "Dog", "Cute boi, can't stop biting, came in for tummy bug", False)

    def test_vet_has_name(self):
        self.assertEqual("Bradley Jiles", self.vet.name)

    def test_vet_has_species_specialism(self):
        self.assertEqual("Dogs", self.vet.species_specialism)

    def test_vet_has_pets(self):
        self.assertEqual([], self.vet.pets)

    def test_add_pet(self):
        self.vet.add_pet(self.pet)
        self.assertEqual([self.pet], self.vet.pets)