# 2. Унікальність результату: усі числа у видачі повинні бути "".

import random
from collections import Counter

def get_numbers_ticket(minimum, maximum, quantity) -> list:
    if not validate(minimum) or not validate(maximum):
      raise ValueError("Invalid values")

    return sorted(random.sample(range(minimum, maximum + 1), quantity))

def validate(value) -> bool:
    return value >= 1 and value <= 1000

def get_ticket_result(ticket: list) -> bool:
    same_numbers_count = Counter(ticket)
    for key in same_numbers_count.keys():
        count = same_numbers_count[key]
        if count > 1:
            return True
    return False

ticket_1 = get_numbers_ticket(1, 49, 6)
ticket_2 = get_numbers_ticket(1, 36, 5)

print("Ваші лотерейні числа(1, 49, 6):", ticket_1)
print("Ваші лотерейні числа(1, 36, 5):", ticket_2)

