from app import db


class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=False, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '%r %r' % (self.subject, self.number)
