from flask import Blueprint,render_template, jsonify, request

api_bp = Blueprint('api_bp', __name__)

@api_bp.route('/')
def home():
    return render_template('index.html')


