import random

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <1000 and quantity < (max - min + 1):
        return random.sample(range(min, max), quantity)
    else:
        return []
    

lottery_numbers = get_numbers_ticket(1, 36, 5)
lottery_numbers.sort()

print("Ваші лотерейні числа:", lottery_numbers)


