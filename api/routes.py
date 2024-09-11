from flask import Blueprint, request, jsonify, session
from sqlalchemy.orm import Session
from models.user import User
from models.engine.db import get_db
import uuid
from datetime import datetime

# Define the Blueprint
api_bp = Blueprint('api_bp', __name__)

# Ensure you have these methods defined in your user model
def create_user(db: Session) -> str:
    unique_id = uuid.uuid4().hex
    current_time = datetime.now()

    user = User(
        user_id=unique_id,
        register_since=current_time
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user.user_id

def fetch_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.user_id == user_id).first()

def update_user_name(user_id, new_name):
    db.query(User).filter(User.userID == user_id).update({
        User.userName: new_name
    })
    db.commit()
    return true

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

@api_bp.route('/register_challenge', methods=['POST'])
def register_challenge():
    try:
        data = request.get_json()
        user_id =  session['userID']  # Example: Assume we get the user ID from session or token
        player_name = data.get('name')

        # Update the user's name in the database
        if update_user_name(user_id, player_name):
            # Prepare the payload for the external API
            payload = {
                'name': player_name,
                'user_id': user_id
            }

            # Send a request to the external API
            response = requests.post('https://challengetrain.xyz/challenge/kadi_setup', json=payload)
            response_data = response.json()

            # Check if the external API call was successful
            if response.status_code == 200 and response_data.get('status') == 'success':
                sharing_url = response_data.get('sharing_url')

                # Return a successful response with the sharing URL and redirect link
                return jsonify({
                    'status': True,
                    'message': 'Challenge setup successful!',
                    'sharing_url': sharing_url,
                    'redirect': url_for('waiting_bay', sharing_url=sharing_url)
                })

            else:
                return jsonify({
                    'status': False,
                    'message': 'Failed to setup challenge.'
                }), 400

        else:
            return jsonify({
                'status': False,
                'message': 'Failed to update user information.'
            }), 400

    except Exception as e:
        return jsonify({
            'status': False,
            'message': f'Error: {str(e)}'
        }), 500
