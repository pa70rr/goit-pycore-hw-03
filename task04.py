from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.11.01"},
    {"name": "Jane Smith", "birthday": "1990.10.29"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    congratulation_date = []
    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_this_year.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if today <= birthday_this_year < today + timedelta(days=7):
            congratulation_date.append(user["name"])
    return congratulation_date


congratulation_date = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", congratulation_date)