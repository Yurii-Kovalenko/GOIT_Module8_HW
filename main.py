from datetime import date, datetime

from date_offset import offset_date


LIST_DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

DATE_OFFSET_LOGIC = {0: {0: (0, -1, -2), 1: 1, 2: 2, 3: 3, 4: 4},
                     1: {1: 0, 2: 1, 3: 2, 4: 3, 0: (4, 5, 6)},
                     2: {2: 0, 3: 1, 4: 2, 0: (3, 4, 5), 1: 6},
                     3: {3: 0, 4: 1, 0: (2, 3, 4), 1: 5, 2: 6},
                     4: {4: 0, 0: (1, 2, 3), 1: 4, 2: 5, 3: 6},
                     5: {0: (0, 1, 2), 1: 3, 2: 4, 3: 5, 4: 6},
                     6: {0: (-1, 0, 1), 1: 2, 2: 3, 3: 4, 4: 5}
                     }

NUMBER_OF_CONTROLLED_DAYS_OF_WEEK = 5

BIRTHDAY = "birthday"


def name_days_of_week(weekday: int) -> str:
    return LIST_DAYS_OF_WEEK[weekday]


def day_and_month_are_the_same(date1, date2: date) -> bool:
    return date1.day == date2.day and date1.month == date2.month


def get_birthdays_per_week(users: dict) -> dict:
    # Реалізуйте тут домашнє завдання

    result = {}

    now_date = date.today()

    now_day_of_week = now_date.weekday()

    date_offset_from_day_of_week = DATE_OFFSET_LOGIC[now_day_of_week]

    verified_dates = {}

    for i in range(NUMBER_OF_CONTROLLED_DAYS_OF_WEEK):
        deltas_of_day = date_offset_from_day_of_week[i]
        if type(deltas_of_day) == tuple:
            for delta in deltas_of_day:
                verified_dates[offset_date(now_date,delta)] = i
        else:
            verified_dates[offset_date(now_date,deltas_of_day)] = i

    
    for user in users:
        for verified_date in verified_dates:
            if day_and_month_are_the_same(user[BIRTHDAY], verified_date):
                days_of_week = name_days_of_week(verified_dates[verified_date])
                new_name = user["name"].split()[0]
                if days_of_week in result:
                    list_names = result[days_of_week]
                    list_names.append(new_name)
                    result[days_of_week] = list_names
                else:
                    result[days_of_week] = [new_name]

    return result

# {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}
if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 27).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Brother Gates", "birthday": datetime(1955, 10, 29).date()}
    ]

    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")