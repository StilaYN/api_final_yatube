# API FINAL YATUBE

## Описание проекта

API для социальной сети yatube. 
Для реализации проекта был использован фреймворк Django и DRF.

## Как запустить 

Склонировать репозиторий с github

```
git clone https://github.com/StilaYN/api_final_yatube
```

Создать и активировать виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```

Установить зависимости
``` 
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры запросов

Полное описание запросов доступно по http://127.0.0.1:8000/redoc/ 

### POST

Создание публикации: добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

http://127.0.0.1:8000/api/v1/posts/


Результат:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

### GET

Список сообществ: получение списка доступных сообществ.

http://127.0.0.1:8000/api/v1/groups/ 


Результат:

```
[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```


### PATCH

Частичное обновление публикации: частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.

http://127.0.0.1:8000/api/v1/posts/{id}/ 

Результат:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
