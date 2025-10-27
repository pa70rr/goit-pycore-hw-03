import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    # Видаляємо всі небажані символи, залишаючи лише цифри
    digits = re.sub(r'\D', '', phone_number)
    
    # Перевіряємо довжину та формат номера
    if len(digits) == 10 and digits.startswith('0'):
        return '+38' + digits
    elif len(digits) == 12 and digits.startswith('380'):
        return '+' + digits
    elif len(digits) == 13 and digits.startswith('+'):
        return digits
    else:
        return 'Invalid number'
    
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)