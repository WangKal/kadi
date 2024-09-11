from flask import Flask, request, jsonify, session
from sqlalchemy.orm import Session
from models.user import User
from models.engine.db import get_db

api_bp = Flask(__name__)
api_bp.secret_key = 'your_secret_key'  # Ensure you set a secret key for sessions

@api_bp.route('/set_cookies', methods=['POST'])
def set_cookies():
    db = next(get_db())
    user_id = create_user(db)
    
    # Set user info in the session
    session['userID'] = user_id
    
    return jsonify({'user_cookie': user_id})

@api_bp.route('/fetch_cookies', methods=['POST'])
def fetch_cookies():
    user_id = request.json.get('user_id')
    db = next(get_db())
    user = fetch_user_by_id(db, user_id)
    
    if user:
        session['userID'] = user_id
        return jsonify({
            'status': True,
            'userID': user.userID,
            'full_name': user.full_name
        })
    else:
        return jsonify({'status': False})

@api_bp.route('/check_session', methods=['GET'])
def check_session():
    if 'userID' in session:
        return jsonify({'user_id': session['userID'], 'status': True})
    else:
        return jsonify({'status': False})
