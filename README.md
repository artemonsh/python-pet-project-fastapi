# Пет-проект на Python - Мини-стартап
Видео: https://www.youtube.com/watch?v=hPQzi8RT7ic

Мини-стартап: FastAPI-сервис проксирует запросы в Gemini и сохраняет историю обращений в базе данных, чтобы видеть, как клиенты общаются с моделью.

API-ключ берётся в AI Studio: https://aistudio.google.com/ (нужен VPN, чтобы получить Gemini API key).

Стек: FastAPI + uvicorn + SQLAlchemy/SQLite на бэке, google-genai для Gemini, чистый HTML/JS на фронте.

## Как запустить
1. Python 3.9+. Установите `uv` и в корне выполните: `uv sync`.
2. Впишите свой ключ вместо `КЛЮЧ_ОТ_GEMINI` в `config.py`.
3. Запустите API: `uv run uvicorn main:app --reload` (порт 8000).
4. Поднимите фронтенд через расширение Live Server в VS Code (порт 5500 должен совпадать с CORS в `index.html`).
