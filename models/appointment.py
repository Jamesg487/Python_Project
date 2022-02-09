class Appointment:

    def __init__(self, pet, vet, date_time_start, date_time_end, appointment_notes, id = None):
        self.pet = pet
        self.vet = vet
        self.date_time_start = date_time_start
        self.date_time_end = date_time_end
        self.appointment_notes = appointment_notes
        self.id = id

def appointment_time_check(start, end, date_time_start):
    if start <= end:
        return start <= date_time_start <= end
    else:
        return start <= date_time_start or date_time_start <= end