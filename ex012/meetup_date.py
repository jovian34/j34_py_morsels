from datetime import date


class MeetupDate:

    def __init__(self, year_int: int, month_int: int):
        self.year = year_int
        self.month = month_int
        self.fourth_thursday = None
        self.set_fourth_thursday()

    def set_fourth_thursday(self):
        first_day_of_month = date(self.year, self.month, 1)
        first_day_of_week = first_day_of_month.weekday()
        if first_day_of_week < 4:
            first_thursday = 4 - first_day_of_week
        else:
            first_thursday = 11 - first_day_of_week
        self.fourth_thursday = first_thursday + 21

    def date_of_meetup(self):
        return date(self.year, self.month, self.fourth_thursday)


def meetup_date(year_int, month_int):
    meetup_day = MeetupDate(year_int, month_int)
    return meetup_day.date_of_meetup()

