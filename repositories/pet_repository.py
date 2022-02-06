from db.run_sql import run_sql

from models.pet import Pet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

def save(pet):
    sql = "INSERT INTO pets (name, vet_id, owner_id, date_of_birth, species, treatment_notes, nervous) VALUES ( %s, %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [pet.name, pet.vet.id, pet.owner.id, pet.date_of_birth, pet.species, pet.treatment_notes, pet.nervous]
    results = run_sql( sql, values )
    pet.id = results[0]['id']
    return pet


def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        owner = owner_repository.select(row['owner_id'])
        pet = Pet(row['name'], vet, owner, row['date_of_birth'], row['species'], row['treatment_notes'], row['nervous'], row['id'])
        pets.append(pet)
    return pets

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        owner = owner_repository.select(result['owner_id'])
        pet = Pet(result['name'], vet, owner, result['date_of_birth'], result['species'], result['treatment_notes'], result['nervous'], result['id'] )
    return pet

def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET (name, vet_id, owner_id, date_of_birth, species, treatment_notes, nervous) = ( %s, %s, %s, %s, %s, %s, %s ) WHERE id = %s"
    values = [pet.name, pet.vet.id, pet.owner.id, pet.date_of_birth, pet.species, pet.treatment_notes, pet.nervous, pet.id]
    run_sql(sql, values)