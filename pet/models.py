from application import db

from store.models import Store

class Species(db.Document):
    name = db.StringField(db_field="n")

class Breed(db.Document):
    name = db.StringField(db_field="n")
    species = db.ReferenceField(Species, db_field="s")

class Pet(db.Document):
    name = db.StringField(db_field="n")
    species = db.ReferenceField(Species, db_field="s")
    breed = db.ReferenceField(Breed, db_field="b")
    age = db.IntField(db_field="a")
    price = db.DecimalField(db_field="p", precision=2, rounding='ROUND_HALF_UP')
    sold = db.BooleanField(db_field="sl", default=False)
    received_date = db.DateTimeField(db_field="rd")
    sold_date = db.DateTimeField(db_field="sd")
