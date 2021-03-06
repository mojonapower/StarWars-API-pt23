from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
#pipenv run migrate 
#pipenv run upgrade
#-> efectuar cambios en la base de datos
#mysql;  use example; show tables; exit;

class People(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(20), unique=False, nullable=True)
    height = db.Column(db.Integer, unique=False, nullable=True)
    mass = db.Column(db.Float, unique=False, nullable=True)

    def serialize(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass
            # do not serialize the password, its a security breach
        }
