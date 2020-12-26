#вьюхи являются и контроллерами, а шаблоны хранятся в папке templates
from app import app
from flask import render_template
#render_template позволяет использовать html шаблоны из папки templates


@app.route('/')
def index():
    return render_template('index.html')