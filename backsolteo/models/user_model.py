from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    todos = db.relationship(
        "TodoModel", backref="user", lazy=True, cascade="all,delete"
    )

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name):
        self.name = name
        db.session.commit()

    def to_dict(self):
        return {"name": self.name, "todos": [todo.to_dict() for todo in self.todos]}

    def __repr__(self):
        return f"<User {self.name}>"
