from app import db
from datetime import datetime
import re

#заменяем все пробелы в заголовке на приемлемые для url-a,дабы потом использовать это в slug
def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-',s)

#создаст таблицу связи много-к-многим
post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                     )

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)

    #устанавливаем отношения между двумя моделями, 1й аргумент название класса с которым выстраиваем отношение,
    #вторым аргументом таблица содержащая данные много-к-многим. backref обратная ссылка, тоесть все посты приобретают
    #свойства tags (post1.tags при его чтении получим список ассоциированных с этим постом тэгов).Аргумент
    #lazy dynamic позволяет получить обьет BaseQuery c дополнительными свойствами и методами.
    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, *args, **kwargs):
        super(Post,self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
            #генерируем человекочитаемые uri

    #__repr__ отвечает за представление из консоли,
    # сама же функция выводит информацию в читаемом виде
    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag,self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag id: {}, name: {}>'.format(self.id, self.name)

#db.create_all()