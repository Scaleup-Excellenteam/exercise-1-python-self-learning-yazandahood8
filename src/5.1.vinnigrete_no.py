import random
import datetime

def generate_random_date(start_date: str, end_date: str):
    """
    Generates a random date between the given start and end dates (format: YYYY-MM-DD).
    If the date falls on a Monday, prints a special message.
    """
    start_timestamp = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").timestamp())
    end_timestamp = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").timestamp())
    
    random_timestamp = random.randint(start_timestamp, end_timestamp)
    random_date = datetime.datetime.fromtimestamp(random_timestamp).date()
    
    print("Generated date:", random_date)
    
    if random_date.weekday() == 0: 
        print("אין לי ויניגרט!")
        
        
if __name__ == '__main__':
    # Example: Generate a random date between '2022-01-01' and '2023-01-01'
    generate_random_date('2022-01-01', '2023-01-01')
