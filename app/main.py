from app import app,db #импортируем экземпляр app,db

from posts.blueprint import posts
#импорт экземпляра класса нашего блупринта

import view

#регистрируем блупринт, вторым аргументом указываем куда регистрируем( по какому урлу)
app.register_blueprint(posts, url_prefix='/blog')

if __name__ == "__main__":
	app.run()