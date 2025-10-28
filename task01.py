from datetime import datetime


date = input("Введіть дату:")

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
       return("Невірний формат дати. Використовуйте формат РРРР-ММ-ДД.")
        
    delta = datetime.today() - date_obj
    return delta.days

print(get_days_from_today(date))   