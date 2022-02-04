from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners = owners)

@owners_blueprint.route("/owners/new")
def new_owner():
    return render_template("owners/new.html")

@owners_blueprint.route("/owners",  methods=['POST'])
def create_owner():
    name = request.form['name']
    address = request.form['address']
    email = request.form['email']
    telephone = request.form['telephone']
    owner = Owner(name, address, email, telephone)
    owner_repository.save(owner)
    return redirect('/owners')

@owners_blueprint.route("/owners/<id>", methods=['GET'])
def show_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/show.html', owner = owner)

@owners_blueprint.route("/owners/<id>/edit")
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/edit.html', owner = owner)

@owners_blueprint.route("/owners/<id>",  methods=['POST'])
def update_owner(id):
    name = request.form['name']
    address = request.form['address']
    email = request.form['email']
    telephone = request.form['telephone']
    owner = Owner(name, address, email, telephone, id)
    owner_repository.update(owner)
    return redirect('/owners')

@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete(id):
    owner_repository.delete(id)
    return redirect('/owners')