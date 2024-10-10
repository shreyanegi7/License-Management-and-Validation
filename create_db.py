from models import db, app  # Import db and app from models

# Create the database and the table
with app.app_context():
    db.create_all()  # This will create all tables defined in models.py
