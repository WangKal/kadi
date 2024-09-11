from flask import Flask, request, jsonify, session, make_response
from models.user import insert_user, update_user, fetch_user_by_id
import hashlib, random

api_bp = Flask(__name__)
api_bp.secret_key = 'your_secret_key'  # Used for Flask sessions

# Utility to create a unique string (similar to PHP's uniqid)
def generate_unique_id():
    return hashlib.md5(str(random.randint(100000, 999999)).encode()).hexdigest()

# Setting cookies and user session
@api_bp.route('/set_cookies', methods=['POST'])
def set_cookies():
    con_password = request.form.get('con_password', '')
    salt = 'SALT'  # Use your defined salt here
    
    # Insert new user into the database
    user_id_db = insert_user(con_password, salt)
    
    # Generate unique user_id and update the user
    unique_id = generate_unique_id() + str(user_id_db)
    update_user(user_id_db, unique_id)

    # Set session data
    session['userID'] = user_id_db
    session['full_name'] = ''

    # Set cookies in response
    response = make_response(jsonify({'user_cookie': unique_id}))
    response.set_cookie('user_id', unique_id, max_age=60 * 60 * 24 * 365)  # 1 year
    return response

# Fetch cookies and verify user session
@api_bp.route('/fetch_cookies', methods=['POST'])
def fetch_cookies():
    # Get the user_id from request or cookie
    user_id = request.form.get('user_id', request.cookies.get('user_id'))

    if not user_id:
        return jsonify({'status': False, 'error': 'User ID not found'}), 400

    # Fetch the user from the database
    user = fetch_user_by_id(user_id)

    if not user:
        return jsonify({'status': False, 'error': 'Invalid user ID'}), 400

    # Set session data
    session['userID'] = user['userID']
    session['full_name'] = user['full_name']

    # Return the user data
    return jsonify({
        'status': True,
        'userID': user['userID'],
        'full_name': user['full_name']
    })

if __name__ == '__main__':
    api_bp.run(debug=True)


