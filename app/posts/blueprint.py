from flask import Blueprint
#тут хранятся изолированный кусок кода(blueprint), не забыть зарегестрировать блуприн в app.py
from flask import render_template

posts = Blueprint('posts', __name__, template_folder='templates')
#создаем экземпляр класса, передаем название блупринта, __name__, и папку где хранятся хтмл шаблоны

@posts.route('/')
def index():
    return render_template('posts/index.html')