from flask import Blueprint, request, jsonify, render_template, redirect
from helpers import token_required
from models import db, User, Contact, contact_schema, contacts_schema
from forms import PostCar

api = Blueprint('api',__name__, url_prefix='/api')
@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

@api.route('/contacts', methods = ['POST'])
@token_required
def create_contact(current_user_token):
    name = request.json['name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    address = request.json['address']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    contact = Contact(name, email, phone_number, address, user_token = user_token )

    db.session.add(contact)
    db.session.commit()

    response = contact_schema.dump(contact)
    return jsonify(response)

@api.route("post/new", methods = ['GET', 'POST'])
def add_car():
    form = PostCar()
    return render_template('car_form.html', title = 'New_Car', form=form)
    return redirect("{{ url_for('site.profile') }}")
