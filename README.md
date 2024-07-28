# Django Веб-Приложение

Это веб-приложение на Django, которое предоставляет API для получения и отображения данных о рекламе.

## Основные Пакеты

- **Django**: Высокоуровневый Python веб-фреймворк.
- **Django REST Framework**: Инструментарий для создания веб-API.
- **Gunicorn**: HTTP-сервер WSGI для UNIX на Python.
- **django-allauth**: Набор Django приложений для аутентификации, регистрации, управления учетными записями и аутентификации через сторонние сервисы.
- **django-rest-auth**: Набор REST API конечных точек для аутентификации и регистрации.
- **djangorestframework-simplejwt**: Плагин аутентификации JSON Web Token для Django REST Framework.


## Функционал

- Регистрация и вход пользователей с использованием JWT.
- Получение и отображение данных о рекламе.
- API конечные точки защищены аутентификацией JWT(1 из 2х).
- Автоматически сгенерированная документация API (Swagger и ReDoc).

## Как Запустить Приложение

### Необходимые Условия
- Без Docker
  - Python + pip
- С Docker
  - Docker
  - Docker Compose

### Шаги

1. **Клонировать Репозиторий**:
    ```bash
    git clone https://github.com/atomsis/Farpost-API-for-advertisement-.git
    cd farpost
    ```

2. **Собрать и Запустить Docker Контейнер**:
    ```bash
    docker-compose up --build -d
    ```

3. **Запустить Миграции и Собрать Статические Файлы**:
    ```bash
    python manage.py migrate
    python manage.py collectstatic --noinput
    ```

4. **Доступ к Приложению**:
    Откройте браузер и перейдите по адресу `http://localhost:8000/api/ad/`.

### Использование Приложения

- **Регистрация**:
    Для регистрации нового пользователя отправьте POST запрос на `/auth/registration/` с полями `username`, `email` и `password`. Пример запроса:
    ```json
    {
        "username": "your_username",
        "email": "your_email@example.com",
        "password1": "your_password",
        "password2": "your_password"
    }
    ```

- **Вход**:
    Для входа пользователя отправьте POST запрос на `/auth/login/` с полями `username` и `password`. Пример запроса:
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
    В ответе будет предоставлен токен JWT, который необходимо включать в заголовок `Authorization` всех последующих запросов в формате `Bearer <token>`.

- **API Конечные Точки**:
    - `/api/ad/` - Список реклам (не требуется аутентификация).
    - `/api/ad/<id>/` - Подробная информация о рекламе (требуется аутентификация).

- **Документация API**:
    - Swagger: `http://localhost:8000/swagger/`
    - ReDoc: `http://localhost:8000/redoc/`
### Запуск Тестов

Для запуска тестов используйте следующую команду:
```bash
python manage.py test
```

### Структура Проекта
```bash
├── api_parse_data         # Django приложение для парсинга и отображения данных
├── farpost                # Настройки проекта Django
├── staticfiles            # Статические файлы
├── manage.py              # Скрипт управления Django
├── requirements.txt       # Зависимости Python
├── Dockerfile             # Dockerfile для сборки контейнера
├── docker-compose.yml     # Конфигурация Docker Compose
└── README.md              # Документация проекта
```


