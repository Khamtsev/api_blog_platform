### О проекте
Api для сервиса YATUBE - платформы для блогов.
Есть возможность зарегистрироваться, создать, отредактировать или удалить собственный пост,
прокомментировать пост другого автора и подписаться на него.
Автор: Денис Хамцев, [GitHub](https://github.com/Khamtsev).
Реализовано с помощью Django REST Framework.

### Как запустить проект
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Khamtsev/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры использования
**Получение списка постов с лимитом выдачи постов, равным 10, начиная с 20 поста**
```
GET /api/v1/posts/?limit=10&offset=20
```
```
Response: 200
Content type: application/json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?limit=10&offset=30",
  "previous": "http://api.example.org/accounts/?limit=10&offset=10",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

**Удаление комментария (необходимо быть автором комментария)**
```
DELETE /api/v1/posts/{post_id}/comments/{id}/
```
```
Response: 404
Content type: application/json
{
  "detail": "Страница не найдена."
}
```

**Подписаться на пользователя (необходимо быть авторизованным)**
```
POST /api/v1/follow/
```
```
Response: 201
Content type: application/json
{
  "user": "string",
  "following": "string"
}
```

Полная документация по api будет доступна по адресу `/redoc/`