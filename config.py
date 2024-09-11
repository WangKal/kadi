import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://wangkal:WangKal2024#@localhost/kadi')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

