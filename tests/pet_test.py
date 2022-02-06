import unittest
import datetime
from models.owner import Owner
from models.pet import Pet
from models.vet import Vet

class TestPet(unittest.TestCase):
    
    def setUp(self):
        self.owner = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")
        self.vet = Vet("Bradley Jiles", "Dogs")
        self.date_of_birth = datetime.date(2015, 8, 3)
        self.pet = Pet("Sir Bites a lot", self.vet, self.owner, self.date_of_birth, "Dog", "Cute boi, can't stop biting, came in for tummy bug", False)

    def test_pet_has_name(self):
        self.assertEqual("Sir Bites a lot", self.pet.name)

    def test_pet_has_vet(self):
        self.assertEqual(self.vet, self.pet.vet)

    def test_pet_has_owner(self):
        self.assertEqual(self.owner, self.pet.owner)

    def test_pet_has_dob(self):
        self.assertEqual(self.date_of_birth, self.pet.date_of_birth)

    def test_pet_has_species(self):
        self.assertEqual("Dog", self.pet.species)

    def test_pet_has_treatment_notes(self):
        self.assertEqual("Cute boi, can't stop biting, came in for tummy bug", self.pet.treatment_notes)

    def test_pet_is_nervous(self):
        self.assertEqual(False, self.pet.nervous)