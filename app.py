from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

# Register the blueprints (routes)
from routes.user_routes import user_routes
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run()
