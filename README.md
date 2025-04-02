# Парсинг вакансий Data Analyst с HeadHunter 🕵️‍♂️

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-✓-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Проект для сбора и анализа вакансий с HH.ru по ключевому слову "Data Analyst". Включает ETL-пайплайн, визуализацию данных и Docker-контейнер для воспроизводимости.

---

## 📌 Особенности
- **Парсинг через API HH.ru** с пагинацией и обработкой ошибок
- **Сохранение данных** в CSV и SQLite
- **Анализ топ-10 навыков** из требований вакансий
- **Готовый Docker-контейнер** для запуска
- Визуализация результатов (графики в Matplotlib)

---

## 🛠 Технологии
- **Python**: `requests`, `pandas`, `sqlite3`, `matplotlib`
- **Базы данных**: SQLite
- **Инфраструктура**: Docker
- **Анализ**: Статистика, NLP (базовый)

---

## 🚀 Быстрый старт

### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/hh-parser-project.git
   cd hh-parser-project
   ### Установка зависимости:
pip install -r requirements.txt

# Сборка и запуск Docker-контейнера
docker build -t hh_parser -f docker/Dockerfile .
docker run -v $(pwd)/data:/app/data hh_parser

---

##   🔮 Возможные улучшения
Парсинг через BeautifulSoup для сайтов без API
Добавление Airflow для оркестрации задач
Анализ динамики зарплат по городам
Интеграция с Telegram-ботом для уведомлений

💻 Код писался с любовью к данным и кофе.
