import os
basedir = os.path.abspath(os.path.dirname(__file__))
project_dir=os.path.join(basedir, 'app')
class Config(object):
    ADMINS = ["rimgro.mail@gmail.com"]
    MAIL_SERVER="smtp.googlemail.com"
    MAIL_PORT=587
    MAIL_USE_TLS = 1
    MAIL_USERNAME="microblog"
    MAIL_PASSWORD="sedilcrvbpxkkrju"

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-key -_-'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 25
    TEMPLATES_DIR= os.path.join(project_dir, 'Templates')
