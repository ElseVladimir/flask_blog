from flask import Blueprint, request, redirect, url_for
#тут хранятся изолированный кусок кода(blueprint), не забыть зарегестрировать блуприн в app.py
from flask import render_template
from models import Post, Tag
from .forms import PostForm
from app import db


posts = Blueprint('posts', __name__, template_folder='templates')
#создаем экземпляр класса, передаем название блупринта, __name__, и папку где хранятся хтмл шаблоны

#обработчик формы создания поста, лежит сверху других роутеров, что бы они не искали create в постах, methods= списком
#указываем методы которые вьюха обработает
@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title'] #забираем содержание из формы в переменные
        body = request.form['body']
        try:
            if title and body:
                #проверка на наличие title и body, если они пустые вызывает эксепшн, нужно потом переделать на валидатор
                post = Post(title=title, body=body)
                db.session.add(post)
                db.session.commit()
                return redirect(url_for('posts.index'))
            else:
                raise
        except:
            print('Smth wrong')

    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/<slug>/edit/',methods=['POST','GET'])
def edit_post(slug):
    """
    Редактирование постов
    """
    post = Post.query.filter(Post.slug==slug).first()
    if request.method == 'POST':
        form = PostForm(formdata=request.form,obj=post) #formdata - то чно приложение получает из пользователських input,
        #request.form - обращаемся к словарю form и берем оттуда данные, obj параметр проверяет есть ли у обьекта,
        #который в него передается соответсвующие полям формы аттрибуты
        form.populate_obj(post) #populate_obj() перезаписывает отредактированные данные
        db.session.commit() #записываем в базу
        return redirect(url_for('posts.post_detail', slug=post.slug))
    form = PostForm(obj=post)
    return render_template('posts/edit_post.html',post=post,form=form)


@posts.route('/')
def index():
    query = request.args.get('query') #сюда приходит пользовательский ввод из формы поиска
    page = request.args.get('page') #приходит get параметр localhost/blog/?page=номер страницы для пагинации
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if query:
        posts = Post.query.filter(Post.title.contains(query) | Post.body.contains(query)) #.all() комментируем .all что бы
        #корректно работал posts.paginate()
        #если что-то в query, то найдет значение в title или body по значению query, | - или, or не работает
    else:
        posts = Post.query.order_by(Post.created.desc()) # сортировка по дате создания(desc() - по убыванию
    # переменная posts уходит в шаблон
    pages = posts.paginate(page=page,per_page=5) #вызываем метод ПАГИНАЦИИ, три аргумента:номер страницы,количество постов
    #на одной страницу,error_out=True по дефолту включен(выводит ошибку если что-то не так)
    return render_template('posts/index.html',posts=posts,pages=pages,query=query) #передав в шаблон pages используем pages.items()
    #для пагинации, posts можно удалить


#http://localhost:5000/blog/<slug>
@posts.route('/<slug>') #в угловых скобках имя параметра, в переменную slug записываеться все что после '/'
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    #переменная post уходит в шаблон
    tags = post.tags #получаем закрепленные за постами тэги
    return render_template('posts/post_detail.html',post=post, tags=tags)


#http://localhost:5000/blog/tag/python
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all() #получаем список а не обьект basequery
    return render_template('posts/tag_detail.html', tag=tag, posts=posts)