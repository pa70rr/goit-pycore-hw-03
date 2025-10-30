from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.11.01"},
    {"name": "Jane Smith", "birthday": "1990.11.03"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if today <= birthday_this_year < today + timedelta(days=7):
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})
    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)