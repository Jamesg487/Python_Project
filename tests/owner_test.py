import unittest
from models.owner import Owner

class TestOwner(unittest.TestCase):
    
    def setUp(self):
        self.owner = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")

    def test_owner_has_name(self):
        self.assertEqual("Clive Boggs", self.owner.name)

    def test_owner_has_address(self):
        self.assertEqual("23 lonely lane, LL12 6BG", self.owner.address)
        

    def test_owner_has_email(self):
        self.assertEqual("clive@gmail.com", self.owner.email)

    def test_owner_has_telephone(self):
        self.assertEqual("07898533267", self.owner.telephone)