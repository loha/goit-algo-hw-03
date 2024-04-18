from datetime import date # Import the date module

def get_days_from_today(payload_date: str) -> int | str: # Create a function that takes a date as a string and returns an integer or a string
    try:
        now = date.today() # Get the current date
        splited_payload_date = payload_date.split('-') # Split the date by '-'
        parse_int_splited_payload_date = list(map(lambda value: int(value) ,splited_payload_date)) # Parse the date to int
        current = date(*parse_int_splited_payload_date) # Create a date object from the parsed date
        days_result_between = (now - current).days # Get the difference between the current date and the date entered
        return days_result_between # Return the difference
    except Exception as e: # Catch any exception
        return e # Return the exception

payload_date = str(input("Enter a date in the format of YYYY-MM-DD: ")) # Get the date from the user
result = get_days_from_today(payload_date) # Get the result from the function

if type(result) == int: # Check if the result is an integer
    print(f"The difference between today and the date entered is {result} days.") # Print the result

if isinstance(result, Exception): # Check if the result is an exception
    print("Error:", result) # Print the error message
