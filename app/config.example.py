class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False # выпиливает deprecated warning
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/test1'
    # указываем какую бд хотим использовать,
    # root:пароль, @localhost адрес сервера/имя базы данных

    SECRET_KEY = 'smth very secret'

    ### Flask-security ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'