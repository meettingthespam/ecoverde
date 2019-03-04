# from FlaskBuild import db
# from datetime import datetime
#
# # Model for the customer messages sent from
# class UserMessage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=False, nullable=False)
#     email = db.Column(db.String(120), unique=False, nullable=False)
#     phone = db.Column(db.String(12), unique=False, nullable=True)
#     message = db.Column(db.Text, nullable=False)
#     date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f"User('{self.name}', '{self.email}','{self.phone}',\nUTC-{self.date_sent}\n'{self.message}')"
