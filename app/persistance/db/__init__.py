from pymongo import MongoClient

client = None
db = None


def init_db(app):
    """
    Set environment variables for database in
    the .env file in the projects root folder.
    :param app: Flask app object
    :return: None
    """
    global client, db

    username = app.config['DB_USER']
    password = app.config['DB_PASSWORD']
    host = app.config['DB_HOST']
    port = app.config['DB_PORT']
    database = app.config['DB_NAME']

    client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}')
    db = client[database]
