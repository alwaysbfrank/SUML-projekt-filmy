from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    data = request.form
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

