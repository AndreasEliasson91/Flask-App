from app.persistance.models.sub_models import User


def get_all_users():
    return User.all()
