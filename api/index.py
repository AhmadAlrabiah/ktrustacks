from app import app

with app.app_context():
    from app import db
    db.create_all()
