from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, ValidationError



# Form for the visitor to send in a message from the site
class CustomerMessageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired("Please enter your name")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address"), Email()])
    phone = StringField('Phone Number')
    message = TextAreaField('Message', validators=[DataRequired("Please enter your message")])

    submit = SubmitField('Send Message')
