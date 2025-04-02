import requests
import pandas as pd
from time import sleep

def get_vacancies(keyword: str, max_pages: int = 10):
    base_url = "https://api.hh.ru/vacancies"
    vacancies = []
    
    for page in range(max_pages):
        params = {
            "text": keyword,
            "area": 1,  # 1 = Москва
            "per_page": 100,  # Максимум на странице
            "page": page
        }
        
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"Ошибка {response.status_code}")
            break
            
        data = response.json()
        vacancies.extend(data["items"])
        
        # Проверка на последнюю страницу
        if (data["pages"] - page) <= 1:
            break
        
        sleep(1)  # Чтобы не нагружать сервер
    
    return vacancies

def save_to_csv(vacancies, filename="data/vacancies.csv"):
    df = pd.json_normalize(vacancies)
    df.to_csv(filename, index=False)
    print(f"Данные сохранены в {filename}")

if __name__ == "__main__":
    vacancies = get_vacancies("Data Analyst", max_pages=5)
    save_to_csv(vacancies)
