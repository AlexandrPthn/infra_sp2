### **Проект YaMDb**
### Описание
Проект YamDB - это база отзывов о фильмах, книгах и музыке. Здесь пользователь может оставить отзыв (Review) и выставить рейтинг произведению (Title). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». При этом список категорий (Category) может быть расширен администратором. Сами произведения в YamDB не хранятся. Произведению может быть присвоен жанр (Genre) из списка предустановленных, новые жанры может создавать только администратор.
Посмотреть отзывы могут любые пользователи. Для написания собственных отзывов, комментирования и оценки необходима регистрация.

### Стек
![python version](https://camo.githubusercontent.com/6e7b83ff04ff922842607025b466445569c2b79e7521df5b651a0d76ff7ef71e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e372d677265656e) ![django version](https://camo.githubusercontent.com/3b24766753d4fce1d8876ec3a6a3f6f76814ff796af79022f9e69115f609a662/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2d322e322d677265656e) [![sorl-thumbnail version](https://camo.githubusercontent.com/dce6018a2e8e17837a2627b35fe1eaa83373c24754ea01d8ce30e995f4de0f31/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f253230524553542532304672616d65776f726b2d253230332e31322e342d677265656e)](https://camo.githubusercontent.com/a4603e990037d36b43920e28f0f67ee679bbaaecc9faf58851494b8838f959c7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50696c6c6f772d382e332d677265656e) [![pytest version](https://camo.githubusercontent.com/f4cfb62ef31f50735a09fa9612bc5a32f6cb08bdff1fd08d1af3e162d1b9cda7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7079746573742d362e322d677265656e)](https://camo.githubusercontent.com/f4cfb62ef31f50735a09fa9612bc5a32f6cb08bdff1fd08d1af3e162d1b9cda7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7079746573742d362e322d677265656e) [![requests version](https://camo.githubusercontent.com/9ca7d43200b6212b4603b428a19734d31f663b5cc8d1f1b801e41723eb5c814c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72657175657374732d322e32362d677265656e)](https://camo.githubusercontent.com/9ca7d43200b6212b4603b428a19734d31f663b5cc8d1f1b801e41723eb5c814c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72657175657374732d322e32362d677265656e) ![python version](https://camo.githubusercontent.com/453c91c0e32caa1af3c7d6d9f76e9ac6d5764c338a5fd170d2778a0bd1f28de3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d332e332d677265656e) ![python version](https://camo.githubusercontent.com/680fad3b72a041897b28ea7198d180bb59152cbd5bf47aadf73f8f69d116d782/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e67696e782d253230312e31382d677265656e)
### Как запустить проект:
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/AlexandrPthn/infra_sp2.git
cd infra_sp2/infra/
``` 
- Запуск приложения с помощь контейнеризации Docker:

Если Docker еще не установлен скачайте и установите его по ссылке:
*https://www.docker.com/products/docker-desktop*
Так как переменные базы данных подгружаются из скрытого файла .env, переименуйте файл .env.example в .env и в нем же установите свой пароль для доступа к БД.
```
cp .env.example .env
```
Для запуска проекта выполните команду из корневой директории проекта. Будет проведена сборка образа по Dockerfile и запуск проекта в трех контейнерах.
```
docker-compose up -d
```
Примените миграции:
```
docker-compose exec web python manage.py migrate
```
Для создания суперпользователя выполните команду:
```
docker-compose exec web python manage.py createsuperuser
```
Cупер-пользователь позволяет быстро и удобно создавать пользователей, посты, комментарии и другие сущности.

Выполните команду для создания статики:
```
docker-compose exec web python manage.py collectstatic --no-input 
```
Теперь проект доступен по адресу http://127.0.0.1/admin/. Описание API проекта доступно по адресу http://127.0.0.1/redoc/

Начальные данные хранятся в файле fixtures.json. Для заполнения базы этими данными выполните команду:
```
docker-compose exec web python manage.py loaddata fixtures.json
```
В админке http://127.0.0.1/admin/ в разделах Categories Genres и Titles появятся тестовые данные.

-  Рекомендации при сворачивании проекта

Остановка и удаление контейнеров:
```
docker-compose down
```
Удаление образов (!команда удалит все неиспользуемые образы! если есть нужные образы лучше удалять по id):
```
docker system prune -a
```
Удаление всех неиспользуемых томов:
```
docker volume prune
```

### REST API
REST API для примера описан ниже.
- ### Регистрация нового пользователя:

Получить код подтверждения на переданный email. Права доступа: Доступно без токена.

### Request
    POST /api/v1/auth/signup/
```
application/json
{
  "email": "string",
  "username": "string"
}
```
### Response 
```
application/json
{
  "email": "string",
  "username": "string"
}
```
- ### Получение JWT-токена:

Получение JWT-токена в обмен на username и confirmation code. Права доступа: Доступно без токена.

### Request
    POST /api/v1/auth/token/
```
application/json
{
  "username": "string",
  "confirmation_code": "string"
}
```
### Response 
```
application/json
{
  "token": "string"
}
```
- ###  Получение списка всех категорий:

Получить список всех категорий. Права доступа: Доступно без токена.

### Request
    GET /api/v1/categories/

### Response 
```
application/json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```
- ### Добавление новой категории:

Создать категорию. Права доступа: Администратор.

### Request
    POST /api/v1/categories/
``` 
application/json
{
  "name": "string",
  "slug": "string"
}
```
### Response 
```
application/json
{
  "name": "string",
  "slug": "string"
}
```
- ### Удаление категории:

Удалить категорию. Права доступа: Администратор.

### Request
    DELETE /api/v1/categories/{slug}/

- ### Получение списка всех жанров:

Получить список всех жанров. Права доступа: Доступно без токена.

### Request
    GET /api/v1/genres/
    
### Response 
```
application/json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "name": "string",
        "slug": "string"
      }
    ]
  }
]
```
- ### Добавление жанра:

Добавить жанр. Права доступа: Администратор.

### Request
    POST /api/v1/genres/
```
application/json
{
  "name": "string",
  "slug": "string"
}
```
### Response 
```
application/json
{
  "name": "string",
  "slug": "string"
}
```
- ### Удаление категории:

Удалить категорию. Права доступа: Администратор.

### Request
    DELETE /api/v1/genres/{slug}/

- ### Получение списка всех произведений:

Получить список всех объектов. Права доступа: Доступно без токена.

### Request
    GET /api/v1/titles/

### Response 
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]
```
- ### Добавление произведения:

Добавить новое произведение. Права доступа: Администратор.

### Request
    POST /api/v1/titles/
```
application/json
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
### Response 
```
application/json
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
- ### Получение информации о произведении:

Информация о произведении. Права доступа: Доступно без токена

### Request
    GET /api/v1/titles/{titles_id}/

### Response 
```
application/json
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
- ### Частичное обновление информации о произведении:

Обновить информацию о произведении. Права доступа: Администратор.

### Request
    PATCH /api/v1/titles/{titles_id}/
```
application/json
{
  "name": "string",
  "year": 0,
  "description": "string",
  "genre": [
    "string"
  ],
  "category": "string"
}
```
### Response 
```
application/json
{
  "id": 0,
  "name": "string",
  "year": 0,
  "rating": 0,
  "description": "string",
  "genre": [
    {
      "name": "string",
      "slug": "string"
    }
  ],
  "category": {
    "name": "string",
    "slug": "string"
  }
}
```
- ### Удаление произведения по id:

Удалить произведение. Права доступа: Администратор.

### Request
    DELETE /api/v1/titles/{titles_id}/

- ### Получение списка всех отзывов:

Получить список всех отзывов. Права доступа: Доступно без токена.

### Request
    GET /api/v1/titles/{title_id}/reviews/

### Response 
```
application/json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "score": 1,
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```
- ### Добавление нового отзыва:

Добавить новый отзыв. Пользователь может оставить только один отзыв на произведение. Права доступа: Аутентифицированные пользователи.

### Request
    POST /api/v1/titles/{title_id}/reviews/
```
application/json
{
  "text": "string",
  "score": 1
}
```
### Response 
```
application/json
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- ### Получение отзыва по id:

Получить отзыв по id для указанного произведения. Права доступа: Доступно без токена

### Request
    GET /api/v1/titles/{title_id}/reviews/{review_id}/

### Response 
```
application/json
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- ### Частичное обновление отзыва по id:

Частично обновить отзыв по id. Права доступа: Автор отзыва, модератор или администратор.

### Request
    PATCH /api/v1/titles/{title_id}/reviews/{review_id}/
```
application/json
{
  "text": "string",
  "score": 1
}
```
### Response 
```
application/json
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- ### Удаление отзыва по id:

Удалить отзыв. Права доступа: Автор отзыва, модератор или администратор.

### Request
    DELETE /api/v1/titles/{title_id}/reviews/{review_id}/

- ### Получение списка всех комментариев к отзыву:

Получить список всех комментариев к отзыву по id. Права доступа: Доступно без токена.

### Request
    GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/

### Response 
```
application/json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "text": "string",
        "author": "string",
        "pub_date": "2019-08-24T14:15:22Z"
      }
    ]
  }
]
```
- ### Добавление комментария к отзыву:

Добавить новый комментарий для отзыва. Права доступа: Аутентифицированные пользователи.

### Request
    POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
```
application/json
{
  "text": "string"
}
```
### Response 
```
application/json
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- ### Получение комментария к отзыву:

Получить комментарий для отзыва по id. Права доступа: Доступно без токена

### Request
    GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

### Response 
```
application/json
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- ### Частичное обновление комментария к отзыву:

Частично обновить комментарий к отзыву по id. Права доступа: Автор комментария, модератор или администратор.

### Request
    PATCH /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
application/json
{
  "text": "string"
}
```
### Response
```
application/json
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```
- ### Удаление комментария к отзыву:

Удалить комментарий к отзыву по id. Автор комментария, модератор или администратор.

### Request
    DELETE /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/

- ### Получение списка всех пользователей:

Получить список всех пользователей. Права доступа: Администратор.

### Request
    GET /api/v1/users/

### Response 
```
application/json
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "bio": "string",
        "role": "user"
      }
    ]
  }
]
```
- ### Добавление пользователя:

Добавить нового пользователя. Права доступа: Администратор.

### Request
    POST /api/v1/users/
```
application/json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
### Response 
```
application/json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
- ### Получение пользователя по username:

Получить пользователя по username. Права доступа: Администратор.

### Request
    GET /api/v1/users/{username}/

### Response 
```
application/json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
- ### Изменение данных пользователя по username:

Изменить данные пользователя по username. Права доступа: Администратор.

### Request
    PATCH /api/v1/users/{username}/
```
application/json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
### Response 
```
application/json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
- ### Удаление пользователя по username:

Удалить пользователя по username. Права доступа: Администратор.

### Request
    DELETE /api/v1/users/{username}/

- ### Получение данных своей учетной записи:

Получить данные своей учетной записи. Права доступа: Любой авторизованный пользователь.

### Request
    GET /api/v1/users/me/
    
### Response 
```
application/json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
- ### Изменение данных своей учетной записи:

Изменить данные своей учетной записи. Права доступа: Любой авторизованный пользователь.

### Request
    PATCH /api/v1/users/me/
```
application/json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string"
}
```
### Response 
```
application/json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "role": "user"
}
```
