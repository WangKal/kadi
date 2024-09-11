from web_flask import app
from models import init_app as init_models
from api import init_app as init_api

# Initialize models and API
init_models(app)
init_api(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5005',debug=True)

