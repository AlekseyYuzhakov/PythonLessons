date_to_prove = "12.11.2022"


def check_date(date):
    day_state = False
    month_state = False
    year_state = False
    special_year = None
    dict_month = {
        1: 31,
        2: (28, 29),
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    day, month, year = date.split(".")
    day = int(day)
    month = int(month)
    year = int(year)
    if 0 < month < 13:
        month_state = True
    else:
        return False
    if 0 < year < 10000:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            special_year = True
            year_state = True
        else:
            year_state = True
            special_year = False
    else:
        return False
    if special_year:
        if month == 2:
            if 0 < day <= dict_month[month][1]:
                day_state = True
        elif 0 < day <= dict_month[month]:
            day_state = True
        else:
            return False
    else:
        if month == 2:
            if 0 < day <= dict_month[month][0]:
                day_state = True
        elif 0 < day <= dict_month[month]:
            day_state = True
        else:
            return False

    return day_state and month_state and year_state


print(check_date(date_to_prove))
