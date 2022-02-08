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
vet3 = Vet("David Hynes", "Badgers")
vet_repository.save(vet3)
vet4 = Vet("Clasandra Winters", "Rats")
vet_repository.save(vet4)
vet5 = Vet("Henry Jones", "Horses")
vet_repository.save(vet5)
vet6 = Vet("Ellen Froggit", "Reptiles")
vet_repository.save(vet6)

owner1 = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")
owner_repository.save(owner1)
owner2 = Owner("Bob Hope", "17 Mosley Close, AB16 9JO", "Bob@gmail.com", "07794609239")
owner_repository.save(owner2)
owner3 = Owner("Helen Knokes", "8 Thurley Close, Southoe, PE19 5YH", "helen@gmail.com", "01480215220")
owner_repository.save(owner3)
owner4 = Owner("Claire Fronthime", "50 Outram Close, Hull, HU2 9JR", "Clair@gmail.com", "07767394239")
owner_repository.save(owner4)
owner5 = Owner("Michael Londonfog", "20 King Charles Close, Buckingham, MK18 1UZ", "mich@gmail.com", "07304683267")
owner_repository.save(owner5)
owner6 = Owner("Gregor MacGregor", "2 Poyais Way, PY16 8PY", "invest@poyais.com", "0000089754")
owner_repository.save(owner6)

pet1 = Pet("Sir Bites a lot", vet1, owner1, datetime.date(2003, 6, 17), "Dog", "Cute boi, can't stop biting, generally no health problems", False)
pet_repository.save(pet1)
pet2 = Pet("Clifford", vet2, owner2, datetime.date(2015, 8, 3), "Badger", "Diabetic, regular blood suger check, insulin prescribed monthly", True)
pet_repository.save(pet2)
pet3 = Pet("Hecuba", vet3, owner3, datetime.date(2003, 6, 17), "Bearded Dragon", "Generally healthy, had measels quite young, now fully recoverd", False)
pet_repository.save(pet3)
pet4 = Pet("Jarrah", vet4, owner4, datetime.date(2015, 8, 3), "Rabbit", "Sheds a lot, taking medication for this", True)
pet_repository.save(pet4)
pet5 = Pet("Zanzi", vet5, owner5, datetime.date(2003, 6, 17), "Chinchilla", "Healthy until partner died, doesnt like his new cage buddy, affecting his mood", False)
pet_repository.save(pet5)
pet6 = Pet("Octo", vet6, owner6, datetime.date(2015, 8, 3), "Octopus", "Had a limb removed due to nasty fight, recovering well", True)
pet_repository.save(pet6)

appointment1 = Appointment(pet1, vet1, datetime.datetime(2022, 2, 6, 14, 0), datetime.datetime(2022, 2, 6, 15, 0), "teeth checking and general health check")
appointment_repository.save(appointment1)
appointment2 = Appointment(pet2, vet2, datetime.datetime(2022, 4, 12, 11, 30), datetime.datetime(2022, 4, 12, 12, 00), "blood check") 
appointment_repository.save(appointment2)
appointment3 = Appointment(pet3, vet3, datetime.datetime(2022, 6, 18, 10, 15), datetime.datetime(2022, 6, 18, 11, 0), "temperature and skin check")
appointment_repository.save(appointment3)
appointment4 = Appointment(pet4, vet4, datetime.datetime(2022, 8, 9, 9, 30), datetime.datetime(2022, 8, 9, 10, 00), "general check up") 
appointment_repository.save(appointment4)
appointment5 = Appointment(pet5, vet5, datetime.datetime(2022, 5, 6, 14, 0), datetime.datetime(2022, 2, 6, 15, 0), "socialising exercise")
appointment_repository.save(appointment5)
appointment6 = Appointment(pet6, vet6, datetime.datetime(2022, 4, 12, 11, 30), datetime.datetime(2022, 4, 12, 12, 30), "agility test to see how they're coping after opp") 
appointment_repository.save(appointment6)


pdb.set_trace()