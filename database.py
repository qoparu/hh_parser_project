import sqlite3
import pandas as pd

def create_db():
    conn = sqlite3.connect("data/vacancies.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vacancies (
            id INTEGER PRIMARY KEY,
            name TEXT,
            salary_from INTEGER,
            salary_to INTEGER,
            currency TEXT,
            employer TEXT,
            experience TEXT,
            skills TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_to_db(filename="data/vacancies.csv"):
    df = pd.read_csv(filename)
    
    # Очистка данных: преобразование salary
    df["salary_from"] = df["salary.from"].fillna(0)
    df["salary_to"] = df["salary.to"].fillna(0)
    df["currency"] = df["salary.currency"].apply(lambda x: x if isinstance(x, str) else "RUR")
    
    conn = sqlite3.connect("data/vacancies.db")
    df[["id", "name", "salary_from", "salary_to", "currency", "employer.name", "experience.name", "snippet.requirement"]].to_sql(
        "vacancies", conn, if_exists="replace", index=False
    )
    conn.close()
    print("Данные сохранены в SQLite")
