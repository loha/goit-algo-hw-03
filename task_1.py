from datetime import date

def get_days_from_today(payload_date: str) -> int | str:
    try:
        now = date.today()
        splited_payload_date = payload_date.split('-')
        parse_int_splited_payload_date = list(map(lambda value: int(value) ,splited_payload_date))
        current = date(*parse_int_splited_payload_date)
        days_result_between = (now - current).days
        return days_result_between
    except Exception as e:
        return e

payload_date = str(input("Enter a date in the format of YYYY-MM-DD: "))
result = get_days_from_today(payload_date)

if type(result) == int:
    print(f"The difference between today and the date entered is {result} days.")

if isinstance(result, Exception):
    print("Error:", result)
