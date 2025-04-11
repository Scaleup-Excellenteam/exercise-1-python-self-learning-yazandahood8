import random
import datetime

MONDAY = 0  # Constant instead of magic number

def generate_random_date(start_date: str, end_date: str):
    """
    Generates a random date between the given start and end dates (format: YYYY-MM-DD).
    If the date falls on a Monday, prints a special message.
    """
    try:
        start_timestamp = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp())
        end_timestamp = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp())

        if start_timestamp > end_timestamp:
            print("Start date must be before end date.")
            return

        random_timestamp = random.randint(start_timestamp, end_timestamp)
        random_date = datetime.datetime.fromtimestamp(random_timestamp).date()

        print("Generated date:", random_date)

        if random_date.weekday() == MONDAY:
            print("אין לי ויניגרט!")  # Special message for Monday

    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")

def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            # Just validate format
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    start = get_valid_date("Enter start date (YYYY-MM-DD): ")
    end = get_valid_date("Enter end date (YYYY-MM-DD): ")
    generate_random_date(start, end)
