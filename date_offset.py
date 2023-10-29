from datetime import date, datetime

from calendar import monthrange

from functools import lru_cache


@lru_cache(maxsize = None)
def next_day(my_date: date) -> date:

    my_year = my_date.year
    my_month = my_date.month
    my_day = my_date.day

    try:
        my_day += 1
        probable_date = datetime(year = my_year, month = my_month, day = my_day)
        next_date_wrong = False
    except:
        next_date_wrong = True
    
    if next_date_wrong:
        try:
            my_day = 1
            my_month += 1
            probable_date = datetime(year = my_year, month = my_month, day = my_day)
            next_date_wrong = False
        except:
            next_date_wrong = True
    
    if next_date_wrong:
        try:
            my_day = 1
            my_month = 1
            my_year += 1
            probable_date = datetime(year = my_year, month = my_month, day = my_day)
        except:
            return # impossible situation, the program will terminate with an error
    
    return probable_date


@lru_cache(maxsize = None)
def previous_day(my_date: date) -> date:

    LAST_DAY_OF_YEAR = 31
    LAST_MONTH_OF_YEAR = 12

    my_year = my_date.year
    my_month = my_date.month
    my_day = my_date.day

    if my_day > 1:
        my_day -= 1
        new_date = datetime(year = my_year, month = my_month, day = my_day)
    elif my_month > 1:
        my_month -= 1
        my_day = monthrange(my_year, my_month)[1]
        new_date = datetime(year = my_year, month = my_month, day = my_day)
    else:
        my_day = LAST_DAY_OF_YEAR
        my_month = LAST_MONTH_OF_YEAR
        my_year -= 1
        new_date = datetime(year = my_year, month = my_month, day = my_day)
    
    return new_date


def offset_date(old_date: date, delta: int) -> date:

    result = old_date

    if  delta < 0:
        for _ in range(-delta):
            result = previous_day(result)
    else:
        for _ in range(delta):
            result = next_day(result)

    return result
    