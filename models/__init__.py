from .engine import db_session, Base
from models.engine.db import engine
from models.user import User

# Create all tables in the database (if not already created)
User.metadata.create_all(bind=engine)

def init_app(app):
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    from .engine import init_db
    init_db()

