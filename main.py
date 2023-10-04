from datetime import datetime

from application.salary import get_employess
from application.db.people import calculate_salary

if __name__ == '__main__':
    print(datetime.now())
    get_employess()
    calculate_salary()

