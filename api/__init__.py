from flask import Blueprint
from api.routes import api_bp

api = Blueprint('api', __name__)

# Register API blueprint
def init_app(app):
    app.register_blueprint(api_bp, url_prefix='/api')

