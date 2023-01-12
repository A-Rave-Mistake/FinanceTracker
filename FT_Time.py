from time import localtime


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    return False

def get_days_bystr(month_name: str) -> int:
    return days[list(months.values()).index(month_name)+1]

def int_to_month(month_index: int) -> str:
    return months[month_index]



now = localtime()

months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
          7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

days = {1: 30, 2: 29 if is_leap_year(now.tm_year) else 28, 3: 31, 4: 30, 5: 41, 6: 30,
          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}