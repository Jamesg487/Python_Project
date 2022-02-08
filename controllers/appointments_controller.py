from pyexpat.errors import messages
from flask import Flask, render_template, request, redirect, flash
from flask import Blueprint
from helper_methods.appointment_helper import check_vet_appointment_times
from models.appointment import Appointment
from datetime import datetime
import repositories.appointment_repository as appointment_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

appointments_blueprint = Blueprint("appointments", __name__)

@appointments_blueprint.route("/appointments")
def appointments():
    appointments = appointment_repository.select_all()
    for appointment in appointments:
        if appointment.date_time_start < datetime.today():
            appointment_repository.delete(appointment.id)
    appointments = appointment_repository.select_all()
    return render_template("appointments/index.html", appointments=appointments)

@appointments_blueprint.route("/appointments/new")
def new_appointment():
    vet = None
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    todays_date = datetime.today().strftime('%Y-%m-%d')
    return render_template("appointments/new.html", pets=pets, vets=vets, todays_date=todays_date, vet_appointment=vet)

@appointments_blueprint.route("/vets/<id>/appointments/new")
def pass_vet_to_appointments(id):
    vet = vet_repository.select(id)
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    todays_date = datetime.today().strftime('%Y-%m-%d')
    return render_template('appointments/new.html', vet_appointment=vet, pets=pets, vets=vets, todays_date=todays_date)


@appointments_blueprint.route("/appointments",  methods=['POST'])
def create_appointment():
    pet = pet_repository.select(request.form['pet_id'])
    vet = vet_repository.select(request.form['vet_id'])
    date_time_start = request.form['date_time_start']
    date_time_end = request.form['date_time_end']
    if pet.nervous:
        adjust_end_time = int(date_time_end[-2:]) + 15
        date_time_end = f"{date_time_end[:-2]}{adjust_end_time}"
    appointment_notes = request.form['appointment_notes']
    vet_appointment_times = appointment_repository.get_vet_appointment_times(vet.id)
    if check_vet_appointment_times(vet_appointment_times, date_time_start):
            flash('This time is taken, please pick another time')
            return redirect('/appointments/new')
    else:
        appointment = Appointment(pet, vet, date_time_start, date_time_end, appointment_notes)
        appointment_repository.save(appointment)
        return redirect('/appointments')

@appointments_blueprint.route("/appointments/<id>")
def show_appointment(id):
    appointment = appointment_repository.select(id)
    return render_template('appointments/show.html', appointment=appointment)

@appointments_blueprint.route("/appointments/<id>/edit")
def edit_appointment(id):
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    todays_date = datetime.today().strftime('%Y-%m-%d')
    appointment = appointment_repository.select(id)
    start = appointment.date_time_start.strftime('%Y-%m-%dT%H:%M')
    end = appointment.date_time_end.strftime('%Y-%m-%dT%H:%M')
    return render_template('appointments/edit.html', appointment=appointment, vets=vets, pets=pets, todays_date=todays_date, start=start, end=end)

@appointments_blueprint.route("/appointments/<id>",  methods=['POST'])
def update_appointment(id):
    pet = pet_repository.select(request.form['pet_id'])
    vet = vet_repository.select(request.form['vet_id'])
    date_time_start = request.form['date_time_start']
    date_time_end = request.form['date_time_end']
    appointment_notes = request.form['appointment_notes']
    appointment = Appointment(pet, vet, date_time_start, date_time_end, appointment_notes, id)
    appointment_repository.update(appointment)
    return redirect('/appointments')

@appointments_blueprint.route("/appointments/<id>/delete", methods=['POST'])
def delete(id):
    appointment_repository.delete(id)
    return redirect('/appointments')