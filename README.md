# Job parsing 🕵️‍♂️

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-✓-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A project for collecting and analyzing vacancies with HH.ru by the keyword "Data Analyst". It includes an ETL pipeline, data visualization, and a Docker container for reproducibility.

---

## 📌 Features
- **Parsing via API HH.ru** with pagination and error handling
- **Saving data** to CSV and SQLite
- **Analysis of the top 10 skills** from job requirements
- **Ready-made Docker container** for launch
- **Visualization of results** (graphs in Matplotlib)

---

## 🛠 Technologies
- **Python**: `requests`, `pandas`, `sqlite3`, `matplotlib`
- **Базы данных**: SQLite
- **Инфраструктура**: Docker
- **Анализ**: Статистика, NLP (базовый)

---

## 🚀 Start

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ваш-username/hh-parser-project.git
   cd hh-parser-project
   
2. Install dependency:
   ```bash
   pip install -r requirements.txt

3. Building and launching a Docker container
   ```bash
   docker build -t hh_parser -f docker/Dockerfile .
   docker run -v $(pwd)/data:/app/data hh_parser
