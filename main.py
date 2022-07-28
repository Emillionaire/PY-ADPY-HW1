from application.salary import calculate_salary
from application.db.people import get_employess
from datetime import datetime


if __name__ == '__main__':
    calculate_salary()
    get_employess()
    current_time = datetime.now(tz=None).strftime('%H:%M:%S')
    print(f'Current time is: {current_time}')
