# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db = SQLAlchemy(app)
#
# # Register the blueprints (routes)
# from routes.user_routes import user_routes
# app.register_blueprint(user_routes, url_prefix='/users')
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask
from config import db

from routes.user_routes import user_routes

app = Flask(__name__)

# app.config.from_object('config')
db.init_app(app)

app.register_blueprint(user_routes, url_prefix='/user')

if __name__ == '__main__':
    app.debug = True
    app.run()