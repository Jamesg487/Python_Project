from db.run_sql import run_sql

from models.vet import Vet
from models.pet import Pet



def save(appointment):
    sql = "INSERT INTO appointments (pet_id, vet_id, date, start_time, duration, appointment_notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [appointment.pet_id, appointment.vet_id, appointment.date, appointment.start_time, appointment.duration, appointment.appointment_notes]
    results = run_sql( sql, values )
    appointment.id = results[0]['id']
    return appointment

def delete_all():
    sql = "DELETE  FROM appointments"
    run_sql(sql)