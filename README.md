# Job parsing for hh 

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
- **Databases**: SQLite
- **Infrastructure**: Docker
- **Analyse**: Статистика, NLP (базовый)

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
   ```
   
<div align="center">
  
  <h3>✨ Crafted with ❤️ by <a href="https://github.com/qoparu">qoparu</a> ✨</h3>
  
  <p>For the <b>Special Project</b> | Learning Journey | Open Source Contribution</p>
  
  <blockquote>
  <i>"I am not afraid of ignorance. I'm afraid to stay the same."</i>
  </blockquote>
  
  <div>
    <img src="https://img.shields.io/badge/Java-Expert-important?logo=java" alt="Java Expert">
    <img src="https://img.shields.io/badge/Coding-Passion-blueviolet" alt="Coding Passion">
    <img src="https://img.shields.io/badge/Quality-100%25-brightgreen" alt="Quality Focus">
  </div>
  
  <pre>
ദ്ദി ≽^⎚˕⎚^≼
  </pre>
</div>
