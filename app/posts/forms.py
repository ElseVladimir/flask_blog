from wtforms import Form, StringField, TextAreaField

class PostForm(Form):
    title = StringField('Title') #Title - метка поля StringField
    body = TextAreaField('Body') #Body - метка поля TextAreaField