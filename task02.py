
import random

def get_numbers_ticket(min, max, quantity):
    numbers_ticket = set(random.sample(range(min, max), quantity))
    return sorted(numbers_ticket)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)