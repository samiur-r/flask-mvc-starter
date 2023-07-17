import os
from flask import Flask
from db import db
from routes.user_routes import user_routes
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)

app.register_blueprint(user_routes, url_prefix='/user')

if __name__ == '__main__':
    app.debug = True
    app.run()