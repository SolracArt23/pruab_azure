from flask import Flask,render_template
import os
from flask import send_from_directory
vent = Flask(__name__)

@vent.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')
@vent.route('/')
def Index():
    
    return render_template('index.html')

if __name__ == '__main__':
    vent.run(port=8000)
