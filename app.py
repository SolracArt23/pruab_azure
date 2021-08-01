from flask import Flask,render_template

vent = Flask(__name__)

@vent.route('/')
def Index():
    
    return render_template('index.html')

if __name__ == '__main__':
    vent.run()