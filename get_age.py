from datetime import datetime


def get_declination(year):
    words = ('год', 'года', 'лет')

    if all((year % 10 == 1, year % 100 != 11)):
        return words[0]
    elif all((2 <= year % 10 <= 4,
            any((year % 100 < 10, year % 100 >= 20)))):
        return words[1]
    return words[2]


def get_age(year):
    age = datetime.now().year - year
    return f'{age} {get_declination(age)}'
