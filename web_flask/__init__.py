from flask import Flask
from web_flask.routes import web_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(web_bp)

if __name__ == '__main__':
    app.run(debug=True)

