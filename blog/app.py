from flask import Flask, request


app = Flask(__name__)
@app.route('/<int:numbers>')
def index(numbers:int):
    name = request.args.get('name', None)
    return f'Hellow world!{numbers},{name}'