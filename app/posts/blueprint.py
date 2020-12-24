from flask import Blueprint
#тут хранятся изолированный кусок кода(blueprint), не забыть зарегестрировать блуприн в app.py
from flask import render_template
from models import Post


posts = Blueprint('posts', __name__, template_folder='templates')
#создаем экземпляр класса, передаем название блупринта, __name__, и папку где хранятся хтмл шаблоны

@posts.route('/')
def index():
    posts = Post.query.all()
    # переменная posts уходит в шаблон
    return render_template('posts/index.html',posts=posts)

#http://localhost:5000/blog/<slug>
@posts.route('/<slug>') #в угловых скобках имя параметра, в переменную slug записываеться все что после '/'
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    #переменная post уходит в шаблон
    return render_template('posts/post_detail.html',post=post)