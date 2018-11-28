import operator

def get_earliest(*args):
    dates = []
    for date in args:
        month, day, year = date.split('/')
        month, day, year = int(month), int(day), int(year)
        dates.append((date, month, day, year))
    dates.sort(key=operator.itemgetter(3, 1, 2))
    return dates[0][0]
