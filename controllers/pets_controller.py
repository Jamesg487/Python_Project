from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
from datetime import datetime
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets=pets)

@pets_blueprint.route("/pets/new")
def new_pet():
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    todays_date = datetime.today().strftime('%Y-%m-%d')
    return render_template("pets/new.html", vets=vets, owners=owners, todays_date=todays_date)

@pets_blueprint.route("/pets",  methods=['POST'])
def create_pet():
    name = request.form['name']
    vet = vet_repository.select(request.form['vet_id'])
    owner = owner_repository.select(request.form['owner_id'])
    date_of_birth = request.form['date_of_birth']
    species = request.form['species']
    treatment_notes = request.form['treatment_notes']
    nervous = request.form['nervous']
    pet = Pet(name, vet, owner, date_of_birth, species, treatment_notes, nervous)
    pet_repository.save(pet)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>")
def show_pet(id):
    pet = pet_repository.select(id)
    age = int(datetime.today().strftime('%Y')) - int(pet.date_of_birth.strftime('%Y'))
    return render_template('pets/show.html', pet=pet, age=age)

@pets_blueprint.route("/pets/<id>/edit")
def edit_pet(id):
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    pet = pet_repository.select(id)
    return render_template('pets/edit.html', pet=pet, vets=vets, owners=owners)

@pets_blueprint.route("/pets/<id>",  methods=['POST'])
def update_pet(id):
    name = request.form['name']
    vet = vet_repository.select(request.form['vet_id'])
    owner = owner_repository.select(request.form['owner_id'])
    date_of_birth = request.form['date_of_birth']
    species = request.form['species']
    treatment_notes = request.form['treatment_notes']
    nervous = request.form['nervous']
    pet = Pet(name, vet, owner, date_of_birth, species, treatment_notes, nervous, id)
    pet_repository.update(pet)
    return redirect('/pets')



@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete(id):
    pet_repository.delete(id)
    return redirect('/pets')