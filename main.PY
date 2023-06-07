from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>My Life is a Lie'

if __name__ == '__main__':
    app.run(debug=True)