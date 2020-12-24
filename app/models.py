from app import db
from datetime import datetime
import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-',s)
    #заменяем все пробелы в заголовке на приемлемые для url-a,дабы потом использовать это в slug

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post,self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
            #генерируем человекочитаемые uri

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)
        #__repr__ отвечает за представление,
        # сама же функция выводит информацию в читаемом вдие

#db.create_all()