from db import db
from datetime import datetime as date


class TodoModel(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(), nullable=True)
    body = db.Column(db.String(), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    def __init__(self, title, body, user_id):
        self.body = body
        if title is None or title == "":
            line = body.split("\n")[0]
            if len(line) < 30:
                self.title = line[:30]
            else:
                self.title = body[:30]
        else:
            self.title = title
        self.createdAt = date.now()
        if user_id is not None:
            self.user_id = user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, title, body):
        self.title = title
        self.body = body
        db.session.commit()

    def to_dict(self):
        return {
            "title": self.title,
            "body": self.body,
            "createdAt": self.createdAt,
            "user_id": self.user_id,
        }

    def __repr__(self):
        return f"<Todo {self.title}>"
