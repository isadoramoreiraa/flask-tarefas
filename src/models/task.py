from src.extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    status = db.Column(db.String(20), default="pendente")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
