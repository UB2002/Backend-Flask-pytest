# app/routes.py
from flask import request, jsonify, current_app as app
from . import db
from .model import User


@app.route('/')
def home():
    return "<h1>home</h1>"


@app.route('/user')
def page():
    return "welcome to user page"


@app.route('/post', methods=['POST'])
def put_data():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'you successfully added the data', 'username': username, 'email': email})


@app.route('/get', methods=['GET'])
def getdata():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
