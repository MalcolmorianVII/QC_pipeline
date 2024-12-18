from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['OUTPUT_FOLDER'] = 'outputs'
    app.config['SECRET_KEY'] = 'test hard secret key'
    
    with app.app_context():
        from . import routes
        return app
