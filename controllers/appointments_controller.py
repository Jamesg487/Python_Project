from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.appointment import Appointment
from datetime import datetime
import time
import repositories.appointment_repository as appointment_repository
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

appointments_blueprint = Blueprint("appointments", __name__)

@appointments_blueprint.route("/appointments")
def appointments():
    appointments = appointment_repository.select_all()
    return render_template("appointments/index.html", appointments=appointments)

@appointments_blueprint.route("/appointments/new")
def new_appointment():
    pets = pet_repository.select_all()
    vets = vet_repository.select_all()
    todays_date = datetime.today().strftime('%Y-%m-%d')
    return render_template("appointments/new.html", pets=pets, vets=vets, todays_date=todays_date)

@appointments_blueprint.route("/appointments",  methods=['POST'])
def create_appointment():
    pet = pet_repository.select(request.form['pet_id'])
    vet = vet_repository.select(request.form['vet_id'])
    date = request.form['date']
    start_time = time.strftime(request.form['start_time'])
    duration = int(request.form['duration'])
    if pet.nervous == True:
        duration += 15
    appointment_notes = request.form['appointment_notes']
    appointment = Appointment(pet, vet, date, start_time, duration, appointment_notes)
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
    return render_template('appointments/edit.html', appointment=appointment, vets=vets, pets=pets, todays_date=todays_date)

@appointments_blueprint.route("/appointments/<id>",  methods=['POST'])
def update_appointment(id):
    pet = pet_repository.select(request.form['pet_id'])
    vet = vet_repository.select(request.form['vet_id'])
    date = request.form['date']
    start_time = time.strftime(request.form['start_time'])
    duration = request.form['duration']
    appointment_notes = request.form['appointment_notes']
    appointment = Appointment(pet, vet, date, start_time, duration, appointment_notes, id)
    appointment_repository.update(appointment)
    return redirect('/appointments')

@appointments_blueprint.route("/appointments/<id>/delete", methods=['POST'])
def delete(id):
    appointment_repository.delete(id)
    return redirect('/appointments')