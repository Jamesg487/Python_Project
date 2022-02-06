import unittest
from models.vet import Vet

class TestVet(unittest.TestCase):
    
    def setUp(self):
        self.vet = Vet("Bradley Jiles", "Dogs")

    def test_vet_has_name(self):
        self.assertEqual("Bradley Jiles", self.vet.name)

    def test_vet_has_species_specialism(self):
        self.assertEqual("Dogs", self.vet.species_specialism)