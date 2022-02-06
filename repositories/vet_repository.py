from db.run_sql import run_sql

from models.vet import Vet
from models.pet import Pet
from models.appointment import Appointment
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository



def save(vet):
    sql = "INSERT INTO vets (name, species_specialism) VALUES (%s, %s) RETURNING *"
    values = [vet.name, vet.species_specialism]
    results = run_sql( sql, values )
    vet.id = results[0]['id']
    return vet

def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['species_specialism'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result['name'], result['species_specialism'], result['id'] )
    return vet

def delete_all():
    sql = "DELETE  FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(vet):
    sql = "UPDATE vets SET (name, species_specialism) = (%s, %s) WHERE id = %s"
    values = [vet.name, vet.species_specialism, vet.id]
    run_sql(sql, values)

def pets_registered(vet):
    pets = []

    sql = "SELECT * FROM pets WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql, values)

    for row in results:
        owner = owner_repository.select(row['owner_id'])
        pet = Pet(row['name'], vet, owner, row['date_of_birth'], row['species'], row['treatment_notes'], row['nervous'], row['id'] )
        pets.append(pet)
    return pets



def appointments(vet):
    appointments = []

    sql = "SELECT * FROM appointments WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql, values)

    for row in results:
        pet = pet_repository.select(row['pet_id'])
        appointment = Appointment(pet, vet, row['date'], row['start_time'], row['duration'], row['appointment_notes'], row['id'])
        appointments.append(appointment)
    return appointments

    
# # INNER JOIN TO GET PET APPOINTMENTS FOR VET
# def pet_appointments(vet):
#     pets = []

#     sql = "SELECT pets.* FROM pets INNER JOIN appointments ON appointments.pet_id = pets.id WHERE appointments.vet_id = %s"
#     values = [vet.id]
#     results = run_sql(sql, values)

#     for row in results:
#         owner = owner_repository.select(row['owner_id'])
#         pet = Pet(row['name'], vet, owner, row['date_of_birth'], row['species'], row['treatment_notes'], row['nervous'], row['id'] )
#         pets.append(pet)

#     return pets