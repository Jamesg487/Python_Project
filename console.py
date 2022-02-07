import pdb
import datetime
from models.vet import Vet
from models.pet import Pet
from models.owner import Owner
from models.appointment import Appointment

import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository
import repositories.appointment_repository as appointment_repository

appointment_repository.delete_all()
pet_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()


vet1 = Vet("Bradley Jiles", "Dogs")
vet_repository.save(vet1)

vet2 = Vet("Philipa Bronhime", "Cats")
vet_repository.save(vet2)

owner1 = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")
owner_repository.save(owner1)

owner2 = Owner("Bob Hope", "17 Mosley Close, AB16 9JO", "Bob@gmail.com", "07794609239")
owner_repository.save(owner2)

pet1 = Pet("Sir Bites a lot", vet1, owner1, datetime.date(2003, 6, 17), "Dog", "Cute boi, can't stop biting, came in for tummy bug", False)
pet_repository.save(pet1)

pet2 = Pet("Clifford", vet2, owner2, datetime.date(2015, 8, 3), "Badger", "Diabetic, regular blood suger check, insulin prescribed monthly", True)
pet_repository.save(pet2)

appointment1 = Appointment(pet1, vet1, datetime.date(2022, 2, 6), datetime.time(14, 0).strftime('%H:%M'), 60, "teeth checking and general health check")
appointment_repository.save(appointment1)

appointment2 = Appointment(pet2, vet2, datetime.date(2022, 4, 12), datetime.time(11, 30).strftime('%H:%M'), 30, "blood check")
appointment_repository.save(appointment2)

vet1_appointment_times = appointment_repository.get_vet_appointment_times(vet1.id)

pdb.set_trace()