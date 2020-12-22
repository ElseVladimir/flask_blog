from flask import Flask
from config import Configuration

from posts.blueprint import posts
#импорт экземпляра класса нашего блупринта

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(posts, url_prefix='/blog')
#регистрируем блупринт, вторым аргументом указываем куда регистрируем( по какому урлу)