class Appointment:

    def __init__(self, pet, vet, date, start_time, duration, appointment_notes, id = None):
        self.pet = pet
        self.vet = vet
        self.date = date
        self.start_time = start_time
        self.duration = duration
        self.appointment_notes = appointment_notes
        self.id = id