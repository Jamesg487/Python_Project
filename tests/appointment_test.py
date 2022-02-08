import unittest
from models.appointment import Appointment, appointment_time_check
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
import datetime

class TestAppointment(unittest.TestCase):
    
    def setUp(self):
        vet1 = Vet("Bradley Jiles", "Dogs")
        owner1 = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")
        pet1 = Pet("Clifford", vet1, owner1, datetime.date(2015, 8, 3), "Badger", "Diabetic, regular blood suger check, insulin prescribed monthly", True)
        self.appointment = Appointment(pet1, vet1, datetime.datetime(2022, 4, 12, 11, 30), datetime.datetime(2022, 4, 12, 12, 00), "blood check") 