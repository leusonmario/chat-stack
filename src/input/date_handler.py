import datetime


class DateHandler:

    def __init__(self, from_date, until_date):
        self.from_date = from_date
        self.until_date = until_date
        self.current_starting_date = self.from_date
        self.current_finishing_date = self.from_date

    def is_there_valid_pair_of_days(self):
        if (self.current_finishing_date == self.from_date):
            self.start_counting_days()
            return True
        elif (self.current_finishing_date + datetime.timedelta(days=1)) <= self.until_date:
            self.update_current_pair_days()
            return True
        return False

    def start_counting_days(self):
        self.current_finishing_date += datetime.timedelta(days=1)

    def update_current_pair_days(self):
        self.current_starting_date += datetime.timedelta(days=1)
        self.current_finishing_date += datetime.timedelta(days=1)


