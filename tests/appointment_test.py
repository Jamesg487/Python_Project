import unittest
from models.appointment import Appointment
from models.pet import Pet
from models.owner import Owner
from models.vet import Vet
import datetime

class TestAppointment(unittest.TestCase):
    
    def setUp(self):
        self.vet1 = Vet("Bradley Jiles", "Dogs")
        self.owner1 = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")
        self.pet1 = Pet("Clifford", self.vet1, self.owner1, datetime.date(2015, 8, 3), "Badger", "Diabetic, regular blood suger check, insulin prescribed monthly", True)
        self.appointment = Appointment(self.pet1, self.vet1, datetime.datetime(2022, 4, 12, 11, 30), datetime.datetime(2022, 4, 12, 12, 00), "blood check") 

    def test_appointment_has_pet(self):
        self.assertEqual(self.pet1, self.appointment.pet)

    def test_appointment_has_vet(self):
        self.assertEqual(self.vet1, self.appointment.vet)

    def test_appointment_has_start_time(self):
        self.assertEqual(datetime.datetime(2022, 4, 12, 11, 30), self.appointment.date_time_start)

    def test_appointment_has_end_time(self):
        self.assertEqual(datetime.datetime(2022, 4, 12, 12, 00), self.appointment.date_time_end)

    def test_appointment_has_appointment_notes(self):
        self.assertEqual("blood check", self.appointment.appointment_notes)