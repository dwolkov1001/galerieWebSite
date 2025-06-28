# Галерея изображений

Веб-приложение для загрузки, просмотра и удаления изображений. Поддерживает регистрацию пользователей, вход, восстановление пароля, светлую/тёмную тему и пагинацию.

## Технологии
- Python (Flask)
- HTML/CSS
- SQLite
- Jinja2
- Pillow
- python-dotenv
- itsdangerous

## Функционал
- Регистрация и вход пользователей (пароли хранятся в виде хэша)
- Email (необязателен, нужен для восстановления пароля)
- Восстановление пароля по email (если указан)
- Загрузка, просмотр и удаление только своих изображений
- Подписи к изображениям
- Пагинация
- Светлая/тёмная тема с переключателем
- Адаптивный дизайн (для мобильных)

## Установка и запуск

1. Создайте и активируйте виртуальное окружение (рекомендуется):
```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate в Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` в корне проекта (пример ниже).

4. Запустите приложение:
```bash
python app.py
```

5. Откройте в браузере: http://localhost:5000

## Пример .env
```
SECRET_KEY=your-very-secret-key
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
EMAIL_FROM=your@email.com
```

## Структура проекта
```
galerieWebSite/
├── app.py
├── database.py
├── requirements.txt
├── .env.example
├── README.md
├── TDD_SPEC.md
├── TECHNICAL_PLAN.md
├── templates/
│   ├── index.html
│   ├── image.html
│   ├── login.html
│   ├── register.html
│   ├── forgot.html
│   ├── reset.html
│   └── upload.html
├── static/
│   ├── style.css
│   ├── theme.js
│   └── uploads/
└── database.db
```

## Лицензия
MIT
