from db.run_sql import run_sql

from models.appointment import Appointment
import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository



def save(appointment):
    sql = "INSERT INTO appointments (pet_id, vet_id, date, start_time, duration, appointment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [appointment.pet.id, appointment.vet.id, appointment.date, appointment.start_time, appointment.duration, appointment.appointment_notes]
    results = run_sql( sql, values )
    appointment.id = results[0]['id']
    return appointment

def select_all():
    appointments = []

    sql = "SELECT * FROM appointments"
    results = run_sql(sql)
    for row in results:
        pet = pet_repository.select(row['pet_id'])
        vet = vet_repository.select(row['vet_id'])
        appointment = Appointment(pet, vet, row['date'], row['start_time'], row['duration'], row['appointment_notes'], row['id'])
        appointments.append(appointment)
    return appointments

def select(id):
    appointment = None
    sql = "SELECT * FROM appointments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        pet = pet_repository.select(result['pet_id'])
        vet = vet_repository.select(result['vet_id'])
        appointment = Appointment(pet, vet, result['date'], result['start_time'], result['duration'], result['appointment_notes'], result['id'])
    return appointment

def delete_all():
    sql = "DELETE  FROM appointments"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM appointments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(appointment):
    sql = "UPDATE appointments SET (pet_id, vet_id, date, start_time, duration, appointment_notes) VALUES (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [appointment.pet.id, appointment.vet.id, appointment.date, appointment.start_time, appointment.duration, appointment.appointment_notes, appointment.id]
    run_sql(sql, values)