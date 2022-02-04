from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets)

@pets_blueprint.route("/pets/new")
def new_pet():
    return render_template("pets/new.html")

@pets_blueprint.route("/pets",  methods=['POST'])
def create_pet():
    name = request.form['name']
    species_specialism = request.form['species_specialism']
    pet = Pet(name, species_specialism)
    pet_repository.save(pet)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>", methods=['GET'])
def show_pet(id):
    pet = pet_repository.select(id)
    return render_template('pets/show.html', pet = pet)

@pets_blueprint.route("/pets/<id>/edit")
def edit_pet(id):
    pet = pet_repository.select(id)
    return render_template('pets/edit.html', pet = pet)

@pets_blueprint.route("/pets/<id>",  methods=['POST'])
def update_pet(id):
    name = request.form['name']
    species_specialism = request.form['species_specialism']
    pet = Pet(name, species_specialism, id)
    pet_repository.update(pet)
    return redirect('/pets')



@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete(id):
    pet_repository.delete(id)
    return redirect('/pets')