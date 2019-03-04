from flask import (render_template, request, url_for,
                    flash, redirect, abort, Blueprint)
from FlaskBuild import db, mail
from FlaskBuild.main.forms import CustomerMessageForm
from FlaskBuild.models import UserMessage
from flask_mail import Message



main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')



@main.route("/contact", methods=['GET', 'POST'])
def contact():

    form = CustomerMessageForm()

    if form.validate_on_submit():


        msg = Message('Customer Inquision from Website',
                    sender='info.ecoverdeinc@gmail.com',
                    recipients=['info.ecoverdeinc@gmail.com'])
        msg.body = f'''
From: \n\t{form.name.data}
\nPhone: \n\t{form.phone.data}
\nEmail: \n\t{form.email.data}
\nMessage: \n\t{form.message.data}
'''
        # sending the message
        mail.send(msg)

        customer = UserMessage(name=form.name.data,
                                email=form.email.data,
                                phone=form.phone.data,
                                message=form.message.data)
        db.session.add(customer)
        db.session.commit()



        flash('Message sent thank you. We will be in touch', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html', form=form, title="Contact us")
