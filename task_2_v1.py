# Щоб виграти головний приз лотереї,
# необхідний "ЗБІГ КІЛЬКОХ НОМЕРІВ" на лотерейному квитку з числами,
# що випали випадковим чином і в певному діапазоні під час чергового тиражу

import random
from collections import Counter

def get_numbers_ticket(minimum, maximum, quantity) -> list:
    if not validate(minimum) or not validate(maximum):
      raise ValueError("Invalid values")

    result = []

    for i in range(quantity):
        result.append(random.randint(minimum, maximum))

    return sorted(result)

def validate(value) -> bool:
    return value >= 1 and value <= 1000

def get_ticket_result(ticket: list) -> bool:
    same_numbers_count = Counter(ticket)
    for key in same_numbers_count.keys():
        count = same_numbers_count[key]
        if count > 1:
            return True
    return False

tries = 0

while True:
    tries = tries + 1
    ticket = get_numbers_ticket(1, 49, 6)
    is_won = get_ticket_result(ticket)
    print("Ваші лотерейні числа:", ticket, "Ви виграли!" if is_won else "Ви програли!")

    if is_won:
        print("Кількість спроб:", tries)
        break
