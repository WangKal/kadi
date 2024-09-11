from models.engine.db import get_db_connection, close_db_connection
import hashlib
from datetime import datetime
import uuid

def insert_user(con_password, salt):
    connection = get_db_connection()
    if not connection:
        return None  # Return None if no connection is established

    cursor = connection.cursor()

    try:
        # Generate unique user_id
        unique_id = uuid.uuid4().hex  # Generate a unique ID

        # Hash the password with salt
        password_hash = hashlib.sha1((con_password + salt).encode()).hexdigest()
        register_since = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert user data into the users table
        query = ("INSERT INTO users (user_id, password, register_since) "
                 "VALUES (%s, %s, %s)")
        cursor.execute(query, (unique_id, password_hash, register_since))

        connection.commit()  # Save changes

        return unique_id  # Return the unique user ID
    except Exception as e:
        print(f"Error inserting user: {e}")
        connection.rollback()  # Rollback changes in case of error
        return None
    finally:
        cursor.close()  # Ensure cursor is closed
        close_db_connection(connection)  # Ensure connection is closed


def update_user(user_id_db):
    connection = get_db_connection()
    if not connection:
        return None  # Return None if no connection is established

    cursor = connection.cursor()

    try:
        # Generate a new unique user_id
        unique_id = uuid.uuid4().hex
        last_login = int(datetime.timestamp(datetime.now()))  # Current timestamp for last login
        user_ip = request.remote_addr  # Get the user's IP address from request

        # Update user data in the database
        query = """UPDATE users SET user_id=%s, userName=%s, email=%s, last_login=%s, user_ip=%s WHERE userID=%s"""
        cursor.execute(query, (unique_id, unique_id, unique_id, last_login, user_ip, user_id_db))

        connection.commit()  # Save changes
        return True
    except Exception as e:
        print(f"Error updating user: {e}")
        connection.rollback()  # Rollback changes in case of error
        return False
    finally:
        cursor.close()  # Ensure cursor is closed
        close_db_connection(connection)  # Ensure connection is closed

def fetch_user_by_id(user_id):
    connection = get_db_connection()
    if not connection:
        return None  # Return None if no connection is established

    cursor = connection.cursor(dictionary=True)

    try:
        # Query the user data by user_id
        query = "SELECT * FROM users WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()

        if user_data:
            return user_data  # Return the user's data as a dictionary
        else:
            return None  # Return None if no user found
    except Exception as e:
        print(f"Error fetching user by ID: {e}")
        return None
    finally:
        cursor.close()  # Ensure cursor is closed
        close_db_connection(connection)  # Ensure connection is closed
