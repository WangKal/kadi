from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

# Create engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# Define SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session
db_session = scoped_session(SessionLocal)

# Create a declarative base
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models  # Import all models here to ensure they are registered properly on the metadata
    Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db
    finally:
        db.close()  # Close the session
