from flask import Flask,render_template

vent = Flask(__name__)

@vent.route('/')
def Index():
    
    return 'hola mundo'

if __name__ == '__main__':
    vent.run(port=8000)
