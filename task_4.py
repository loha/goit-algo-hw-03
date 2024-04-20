import datetime
import calendar

users = [
    {"name": "John Doe", "birthday": "1985.04.25"},
    {"name": "Jane Smith", "birthday": "1990.04.27"}
]

def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = []
    today = datetime.date.today()
    # today = datetime.date(2024, 4, 24)
    year = today.year

    for user in users:
        splited_birthday = user["birthday"].split(".")
        next_birthday = datetime.date(year, int(splited_birthday[1]), int(splited_birthday[2]))

        if is_in_next_7_days(next_birthday, today):
            if is_weekday(next_birthday):
                next_work_day = get_next_work_day(next_birthday)
                recursive_result = get_upcoming_birthdays(
                    [{
                        "name": user["name"],
                        "birthday": next_work_day.strftime("%Y.%m.%d")
                    }])
                if len(recursive_result) > 0:
                    upcoming_birthdays.extend(recursive_result)
            else:
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": next_birthday.strftime("%Y.%m.%d")
                })


    return upcoming_birthdays

def is_in_next_7_days(date_to_check, today) -> bool:
    return date_to_check >= today and date_to_check <= today + datetime.timedelta(days=7)

def is_weekday(date):
    return  date.weekday() in [calendar.SATURDAY, calendar.SUNDAY]

def get_next_work_day(date):
    days_to_monday = (calendar.MONDAY - date.weekday()) % 7
    next_monday = date + datetime.timedelta(days=days_to_monday)
    return next_monday

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)