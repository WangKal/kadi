from web_flask import app
from models import init_app as init_models
from api import init_app as init_api

# Initialize models and API
init_models(app)
init_api(app)
app.secret_key = 'your_secret_key'  # Set the secret key for session management

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

