from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy # импортируем orm sqlalchemy



app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


#регистрируем блупринт, вторым аргументом указываем куда регистрируем( по какому урлу)