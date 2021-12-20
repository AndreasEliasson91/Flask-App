from app.persistance.db import db
from app.persistance.models import Document


class User(Document):
    collection = db.users
