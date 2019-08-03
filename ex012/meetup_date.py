from datetime import date


class MeetupDate:

    def __init__(self, year, month, nth, weekday):
        self.year = year
        self.month = month
        self.nth = nth
        self.weekday = weekday
        self.nth_day_of_week = None
        self.set_nth_day_of_week()

    def set_nth_day_of_week(self):
        first_day_of_month = date(self.year, self.month, 1)
        first_day_of_week_of_month = first_day_of_month.weekday()
        if first_day_of_week_of_month <= self.weekday:
            first_day_of_week = self.weekday + 1 - first_day_of_week_of_month
        else:
            first_day_of_week = self.weekday + 8 - first_day_of_week_of_month
        self.nth_day_of_week = first_day_of_week + (self.nth - 1) * 7

    def date_of_meetup(self):
        return date(self.year, self.month, self.nth_day_of_week)


def meetup_date(year_int, month_int, nth=4, weekday=3):
    meetup_day = MeetupDate(year_int, month_int, nth, weekday)
    return meetup_day.date_of_meetup()

