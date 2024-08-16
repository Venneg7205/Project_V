from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models import User, Question
from flask_login import login_user, current_user, logout_user, login_required
import requests

bp = Blueprint('routes', __name__)

@bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Login failed"}), 401

@bp.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

@bp.route('/api/ask', methods=['POST'])
@login_required
def ask():
    question_text = request.get_json().get('question')
    # Обращение к ИИ API для получения ответа
    response = requests.post('http://localhost:5000/api/ask', json={"question": question_text})
    answer = response.json().get('answer', 'No answer available.')

    question = Question(question_text=question_text, answer_text=answer, user_id=current_user.id)
    db.session.add(question)
    db.session.commit()

    return jsonify({"answer": answer}), 200
