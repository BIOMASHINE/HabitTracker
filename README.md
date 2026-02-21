# Habit Tracker 🚀

[![Python](https://img.shields.io/badge/python-3.12-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue?logo=postgresql)](https://postgresql.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Habit Tracker** — это веб-приложение, которое помогает формировать полезные привычки и следить за их выполнением. Проект создан в рамках индивидуального проекта ученика 10 класса, но может быть полезен всем, кто хочет сделать свою жизнь более организованной.

> 🎯 **Главная цель** — помочь людям не забывать о важных делах и видеть свой прогресс, что мотивирует продолжать даже в сложные дни.

---

## ✨ Особенности

- ✅ **Управление привычками** — создавайте, редактируйте и удаляйте свои привычки.
- 📅 **Ежедневные отметки** — отмечайте выполнение привычки одним нажатием.
- 🔥 **Подсчёт текущей серии (streak)** — система автоматически считает, сколько дней подряд вы выполняете привычку.
- 📊 **Статистика пользователя** — базовая статистика (общее количество выполнений, максимальная серия).
- 🔐 **Безопасная аутентификация** — регистрация, вход, верификация email и сброс пароля через email (настроено с помощью **FastAPI-Users**).
- 👤 **Личный кабинет** — каждый пользователь видит только свои привычки.
- 📱 **Готов к использованию с любым фронтендом** — чистое API с полной документацией Swagger.

---

## 🛠 Технологический стек

- **Backend**: Python 3.12, FastAPI
- **База данных**: PostgreSQL 17, SQLAlchemy 2.0 (async), Alembic
- **Аутентификация**: FastAPI-Users
- **Отправка писем**: aiosmtplib (для верификации и сброса пароля)
- **Дополнительно**: Docker, Uvicorn, Pydantic v2

---

## 🚀 Быстрый старт (локальный запуск)

### Предварительные требования
- Python 3.12+
- PostgreSQL (или можно использовать Docker-образ)
- Git

### Установка и запуск

1. **Клонируйте репозиторий**
    ```bash
    git clone https://github.com/BIOMASHINE/HabitTracker.git
    cd habit-tracker
2. **Создайте виртуальное окружение и активируйте его**
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/Mac
    venv\Scripts\activate     # для Windows
3. **Установите зависимости**
    ```bash
    poetry install # для poetry
    pip install . # для pip
    uv sync # для uv
4. **Настройте переменные окружения**
   #### Скопируйте .env.template в .env и отредактируйте под себя:
    ```bash
    cp .env.template .env
    ```
    #### Обязательно укажите DATABASE_URL
5. **Примените миграции базы данных**
    ```bash
    alembic upgrade head
6. **Запустите main.py**
7. **Откройте документацию**
    #### Перейдите по адресу http://localhost:8000/docs — вы увидите интерактивную Swagger-документацию вашего API.

**Запуск через Docker**
#### Если вы предпочитаете Docker, используйте docker-compose:
    docker-compose up -d pg maildev
#### Приложение будет доступно на порту 8000
