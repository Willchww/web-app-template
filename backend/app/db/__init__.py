from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    db.create_all()
