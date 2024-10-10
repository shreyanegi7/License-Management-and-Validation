from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Set the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///licenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional to avoid warnings

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the License model
class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_key = db.Column(db.String(128), unique=True, nullable=False)
    status = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f'<License {self.license_key}>'
