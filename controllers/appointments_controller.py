from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.appointment import Appointment
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
    return render_template("appointments/new.html", pets=pets, vets=vets)