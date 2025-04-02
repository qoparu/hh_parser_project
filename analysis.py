import pandas as pd
from collections import Counter
import sqlite3
import matplotlib.pyplot as plt

def analyze_skills():
    conn = sqlite3.connect("data/vacancies.db")
    df = pd.read_sql_query("SELECT * FROM vacancies", conn)
    
    # Топ-10 навыков из требований
    skills = []
    for req in df["skills"].dropna():
        req_lower = req.lower()
        if "python" in req_lower:
            skills.append("Python")
        if "sql" in req_lower:
            skills.append("SQL")
        if "tableau" in req_lower or "power bi" in req_lower:
            skills.append("BI Tools")
        # Добавьте другие навыки по аналогии...
    
    top_skills = Counter(skills).most_common(10)
    print("Топ-10 навыков:")
    for skill, count in top_skills:
        print(f"{skill}: {count}")
    
    # Визуализация
    plt.barh([s[0] for s in top_skills], [s[1] for s in top_skills])
    plt.title("Топ навыков для Data Analyst")
    plt.savefig("data/skills_plot.png")
    plt.show()

if __name__ == "__main__":
    analyze_skills()
