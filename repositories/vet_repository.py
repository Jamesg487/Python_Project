from db.run_sql import run_sql

from models.vet import Vet


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