from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Render!'

if __name__ == '__main__':
    app.run()


