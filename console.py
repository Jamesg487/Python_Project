import pdb
from models.vet import Vet
from models.pet import Pet
from models.owner import Owner

import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository


vet1 = Vet("Bradley Jiles", "Dogs")
vet_repository.save(vet1)

vet2 = Vet("Philipa Bronhime", "Cats")
vet_repository.save(vet2)


pdb.set_trace()