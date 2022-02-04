import unittest
from models.owner import Owner
from models.pet import Pet
from models.vet import Vet

class TestOwner(unittest.TestCase):
    
    def setUp(self):
        self.owner = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")
        self.vet = Vet("Bradley Jiles", "Dogs")
        self.pet = Pet("Sir Bites a lot", self.vet, self.owner, "23/03/2003", "Dog", "Cute boi, can't stop biting, came in for tummy bug", False)

    def test_owner_has_name(self):
        self.assertEqual("Clive Boggs", self.owner.name)

    def test_owner_has_address(self):
        self.assertEqual("23 lonely lane, LL12 6BG", self.owner.address)
        

    def test_owner_has_email(self):
        self.assertEqual("clive@gmail.com", self.owner.email)

    def test_owner_has_telephone(self):
        self.assertEqual("07898533267", self.owner.telephone)

    def test_owner_has_pets(self):
        self.assertEqual([], self.owner.pets)

    def test_add_pet(self):
        self.owner.add_pet(self.pet)
        self.assertEqual([self.pet], self.owner.pets)

    

    