import random
import datetime

def no_vinnigrete(start_date: str, end_date: str):
    """
    Chooses a random date between start_date and end_date.
    If the random date is Monday, prints a specific message.
    """
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    delta_days = (end - start).days
    if delta_days < 0:
        return  # invalid range, do nothing

    random_day_offset = random.randint(0, delta_days)
    random_date = start + datetime.timedelta(days=random_day_offset)

    if random_date.weekday() == 0:  # Monday = 0
        print("Ain't gettin' no vinaigrette today :(")


if __name__ == '__main__':
    no_vinnigrete('2022-01-01', '2023-01-01')
