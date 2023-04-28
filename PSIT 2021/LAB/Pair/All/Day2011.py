"""day2021"""
def day_of_week(day):
    """main"""
    return {
        0 : "Saturday",
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday",
    }[day]

def zellerformula():
    """main"""
    day = int(input())
    month = int(input())
    year = 2011
    if month == 1:
        month = 13
        year = year - 1

    if month == 2:
        month = 14
        year = year - 1
    first = day
    second = month
    century = year % 100
    no_zero = year // 100
    day = first + 13 * (second + 1) // 5 + century + century // 4 + no_zero // 4 + 5 * no_zero
    day = day % 7
    print(day_of_week(day))
zellerformula()
