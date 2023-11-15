from datetime import datetime
from dateutil import relativedelta


def get_time_between_two_dates(start_date, final_date) -> int:
    '''Returns the amount of months between two dates'''

    # convert string to date object
    start_date = datetime.strptime(start_date.strftime("%d/%m/%Y") , "%d/%m/%Y")
    end_date = datetime.strptime(final_date.strftime("%d/%m/%Y"), "%d/%m/%Y")

    # Get the relativedelta between two dates
    delta = relativedelta.relativedelta(end_date, start_date)
    return delta.months + delta.years * 12
