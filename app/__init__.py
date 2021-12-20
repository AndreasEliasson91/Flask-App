from app.persistance.db import init_db
from flask import Flask


def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('settings.py')
    init_db(_app)

    from app.blueprints.open import bp_open
    _app.register_blueprint(bp_open)

    from app.blueprints.user import bp_user
    _app.register_blueprint(bp_user, url_prefix='/user')

    from app.blueprints.admin import bp_admin
    _app.register_blueprint(bp_admin, url_prefix='/admin')

    return _app
