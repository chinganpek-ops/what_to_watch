# what_to_watch/opinions_app.py

# Новый импорт.
from datetime import datetime

# Импортировать функцию для выбора случайного значения.
from random import randrange

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Opinion(db.Model):
    # ID — целое число, первичный ключ.
    id = db.Column(db.Integer, primary_key=True)
    # Название фильма — строка длиной 128 символов, не может быть пустым.
    title = db.Column(db.String(128), nullable=False)
    # Мнение о фильме — большая строка, не может быть пустым, 
    # должно быть уникальным.
    text = db.Column(db.Text, unique=True, nullable=False)
    # Ссылка на сторонний источник — строка длиной 256 символов.
    source = db.Column(db.String(256))
    # Дата и время — текущее время,
    # по этому столбцу база данных будет проиндексирована.
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) 

@app.route('/')
def index_view():
    # Определить количество мнений в базе данных.
    quantity = Opinion.query.count()
    # Если мнений нет...
    if not quantity:
        # ...то вернуть сообщение:
        return 'В базе данных мнений о фильмах нет.'
    # Иначе выбрать случайное число в диапазоне от 0 до quantity...
    offset_value = randrange(quantity)
    # ...и определить случайный объект.
    opinion = Opinion.query.offset(offset_value).first()
    return render_template('index.html', opinion=opinion)

@app.route('/add')
def add_opinion_view():
    return 'Страница в разработке!'

if __name__ == '__main__':
    app.run()