from datetime import date, timedelta


class MeetupDate:

    def __init__(self, year, month, nth, weekday):
        self.year = year
        self.month = month
        self.nth = nth
        self.weekday = weekday
        self.nth_day_of_week = None
        if self.nth < 0:
            self.set_neg_nth_day_of_week()
        else:
            self.set_nth_day_of_week()

    def set_neg_nth_day_of_week(self):
        if self.month == 12:
            next_month = 1
            next_month_y = self.year + 1
        else:
            next_month = self.month + 1
            next_month_y = self.year
        last_day_of_month = date(next_month_y, next_month, 1) - timedelta(days=1)
        if last_day_of_month.weekday() >= self.weekday:
            difference = last_day_of_month.weekday() - self.weekday
        else:
            difference = 7 - (self.weekday - last_day_of_month.weekday())
        last_day_of_week = last_day_of_month - timedelta(days=difference)
        self.nth_day_of_week = last_day_of_week.day + (self.nth + 1) * 7


    def set_nth_day_of_week(self):
        first_day_of_month = date(self.year, self.month, 1)
        if first_day_of_month.weekday() <= self.weekday:
            first_day_of_week = self.weekday + 1 - first_day_of_month.weekday()
        else:
            first_day_of_week = self.weekday + 8 - first_day_of_month.weekday()
        self.nth_day_of_week = first_day_of_week + (self.nth - 1) * 7

    def date_of_meetup(self):
        return date(self.year, self.month, self.nth_day_of_week)


class WeekDay:

    def __init__(self):
        self.MONDAY = 0
        self.TUESDAY = 1
        self.WEDNESDAY = 2
        self.THURSDAY = 3
        self.FRIDAY = 4
        self.SATURDAY = 5
        self.SUNDAY = 6
        self.Monday = 0
        self.Tuesday = 1
        self.Wednesday = 2
        self.Thursday = 3
        self.Friday = 4
        self.Saturday = 5
        self.Sunday = 6


Weekday = WeekDay()


def meetup_date(year_int, month_int, nth=4, weekday=3):
    meetup_day = MeetupDate(year_int, month_int, nth, weekday)
    return meetup_day.date_of_meetup()


def main():
    print(f"This program tells you the nth specified weekday of any month.\n")
    year = int(input(f"Enter the year: "))
    month = int(input(f"Enter the month number: "))
    weekday = int(input(f"Enter the weekday... \n"
                    f"0 for Monday\n"
                    f"1 for Tuesday\n"
                    f"2 for Wednesday\n"
                    f"3 for Thursday\n"
                    f"4 for Friday\n"
                    f"5 for Saturday\n"
                    f"6 for Sunday\n"
                    f"\n"
                    f"Your Choice: "))
    first = input(f"First(F) or Last(L)? ")
    weeks = int(input(f"Number of weeks? "))
    if first.lower()[0] == 'f':
        nth = abs(weeks)
    else:
        nth = 0 - abs(weeks)
    print(meetup_date(year, month, nth, weekday))


if __name__ == "__main__":
    main()
