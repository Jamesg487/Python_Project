from db.run_sql import run_sql

from models.owner import Owner


def save(owner):
    sql = "INSERT INTO owners (name, address, email, telephone) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [owner.name, owner.address, owner.email, owner.telephone]
    results = run_sql( sql, values )
    owner.id = results[0]['id']
    return owner

def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['address'], row['email'], row['telephone'], row['id'])
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result['name'], result['address'], result['email'], result['telephone'], result['id'] )
    return owner

def delete_all():
    sql = "DELETE  FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (name, address, email, telephone) = (%s, %s, %s, %s) WHERE id = %s"
    values = [owner.name, owner.address, owner.email, owner.telephone, owner.id]
    run_sql(sql, values)