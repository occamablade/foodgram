 <div align=center>

# [Foodgram]


![Python](https://img.shields.io/badge/Python-3.9.10-blue)
![Django](https://img.shields.io/badge/Django-3.2.16-blue)
![Django_REST_framework](https://img.shields.io/badge/Django_REST_framework-3.12.4-blue)
![Nginx](https://img.shields.io/badge/Nginx-1.18.0-blue)
![Gunicorn](https://img.shields.io/badge/Gunicorn-20.1.0-blue)
## Дипломный проект - Продуктовый помощник Foodgram

</div>

## **Стэк технологий**

* [Python 3.9](https://www.python.org/downloads/)
* [Django 3.2.3](https://www.djangoproject.com/download/)
* [djangorestframework 3.12.4](https://pypi.org/project/djangorestframework/#files)
* [djoser 2.1.0](https://pypi.org/project/djoser/#files)
* [webcolors 1.11.1](https://pypi.org/project/webcolors/1.11.1/)
* [gunicorn 20.1.0](https://pypi.org/project/gunicorn/20.1.0/)
* [psycopg2-binary 2.9.6](https://pypi.org/project/psycopg2-binary/#files)
* [PyYAML 6.0](https://pypi.org/project/PyYAML/)
* [python-dotenv 1.0.0](https://pypi.org/project/python-dotenv/)

---

 Foodgram - это сайт, на котором пользователи смогут публиковать свои рецепты, подписываться на других авторов и их рецепты,
 добавлять в избранное и добавлять их в список покупок, который можно скачать в формате txt с перечнем необходимых продуктов и 
 ингредиентов для рецептов в списке покупок.

 * Проект доступен по домену: http://foodgramprojectocc.sytes.net
 * Админ-зона: http://foodgramprojectocc.sytes.net/admin
 * Обычный пользователь: логин: zxcghoul, пароль:zxcghoul, почта:zxcghoul@a.ru
 * Суперпользователь: логин: admin, пароль:admin, почта:admin@a.ru
 
 ***Локальный запуск проекта***

Склонировать репозиторий:
 ```bash
git clone https://github.com/occamablade/foodgram-project-react.git
 ```
Создать и активировать виртуальное окружение:
 ```bash
python3 -m venv venv && \ 
    source venv/scripts/activate && \
 ```
Установить зависимости:
 ```bash
python -m pip install --upgrade pip && \
    pip install -r backend/requirements.txt
 ```
Перейти в директорию infra и создать файл .env со следующим содержимым:
 ```bash
cd foodgram-project-react/infra/
touch .env
nano .env
    ```apache
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432
    SECRET_KEY=django-insecure-mw%u6t#lak9s+*4(-_xuvz(an7n))d8)_su$&_*-2r^7s_$4dy
    ```
 ```
Запустить контейнеры:
```bash
docker compose up --build
```
Сделать миграции, собрать статику, испортировать ингредиенты и создать суперпользователя:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py coolectstatic
docker-compose exec backend python manage.py unloadingcsv
docker-compose exec backend python manage.py createsuperuser
```
# Документация
http://localhost/redoc

<div align=center>

## Контакты

[![Telegram Badge](https://img.shields.io/badge/-vanyshqa-blue?style=social&logo=telegram&link=https://t.me/vanyshqa)](https://t.me/vanyshqa) [![Gmail Badge](https://img.shields.io/badge/-bezborodnikov18@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:bezborodnikov18@gmail.com)](mailto:bezborodnikov18@gmail.com)

</div>
