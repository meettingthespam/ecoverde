import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)
# config.get
class Config:

    SECRET_KEY = config.get('SECRET_KEY')

    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # using GMAIL for the sending and receiving of email
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('EMAIL_USERNAME')
    MAIL_PASSWORD = config.get('EMAIL_PASSWORD')
