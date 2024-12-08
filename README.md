# Блог об автомобилях

Использовались следующие технологии: 

- Python
- Django v4.0.4

## О блоге

Здесь можно посмотреть интересные записи об автомобилях и оставить свои отзывы

## Развертывание проекта

- Клонируем репозиторий

```plaintext
git clone git@github.com:x-dev1/blog.git
```

- Создаем виртуальное окружение
```plaintext
python3 -m venv venv
. venv/bin/activate
```

- Устанавливаем зависимости
```plaintext
pip install --upgrade pip
pip install -r requirements.txt
```

- Переходим в сам проект
```plaintext
cd blog_app
```

- Создаем и применяем миграции
```plaintext
python3 manage.py makemigrations
python3 manage.py migrate
```

- Собираем статику
```plaintext
python3 manage.py collectstatic
```

- Создаем супер-юзера
```plaintext
python3 manage.py createsuperuser
```

- Запускаем проект
```plaintext
python3 manage.py runserver
```

## Роуты

- Главная страница - http://127.0.0.1:8000/posts/
- О проекте - http://127.0.0.1:8000/about/
- Отзывы - http://127.0.0.1:8000/reviews/

Добавлять посты можно из админки, переходим туда по адресу - http://127.0.0.1:8000/admin/
Там мы можем добавить посты, которые будут отображаться на главной странице, а также валидировать
отзывы, осталенные пользователями, выставляя галочки в чек-боксах, расположенных напротив отзыва.
