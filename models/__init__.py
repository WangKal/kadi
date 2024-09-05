from .engine import db_session, Base

def init_app(app):
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    from .engine import init_db
    init_db()

