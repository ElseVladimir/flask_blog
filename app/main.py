from app import app,db #импортируем экземпляр app,db

from posts.blueprint import posts
#импорт экземпляра класса нашего блупринта

import view

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == "__main__":
	app.run()