from application import salary
from application.db.people import get_employees
from datetime import datetime


if __name__ == '__main__':
    print(datetime.today())
    salary.calculate_salary()
    get_employees()
