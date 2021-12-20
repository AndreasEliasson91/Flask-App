from app.persistance.db import init_db
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    init_db(app)

    @app.get('/')
    def index():
        from app.persistance.models import User
        user = User({'username': 'test_user', 'password': 'testing123', 'email': 'test@testmail.com'})
        user.save()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
