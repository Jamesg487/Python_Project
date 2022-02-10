from datetime import datetime
from models.appointment import appointment_time_check



def check_vet_appointment_times(vet_appointment_times, date_time_start):
    """
    This function checks vet appointment times and if a date and time are already taken
    the user is taken back to create appointment page with warning message 

    If date and time are not taken it creates the appointment
    """
    for vet_appointment_time in vet_appointment_times:
        start = datetime.strptime(vet_appointment_time[11:19], '%H:%M:%S').time()
        end = datetime.strptime(vet_appointment_time[31:], '%H:%M:%S').time()
        booking_time = datetime.strptime(f"{date_time_start[11:]}:00", '%H:%M:%S').time()
        if f"{vet_appointment_time[:-29]}" == f"{date_time_start[:-6]}" and appointment_time_check(start, end, booking_time) == True:
            return True