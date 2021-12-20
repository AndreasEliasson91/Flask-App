from flask import Flask

app = Flask(__name__)


# end points (routes)
@app.route('/')
def index():
    raise ValueError
    return '<h1>Main</h1><p>Fun site!</p> <p>Good stuff!</p>'


if __name__ == '__main__':
    app.run(port=7788)
