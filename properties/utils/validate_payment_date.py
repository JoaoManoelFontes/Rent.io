from django.utils import timezone


def validate_payment_date(base_payment_month, base_payment_date) -> bool:
    '''Returns True if the payment date is valid, False otherwise'''

    today_month, today_day = timezone.now().month, timezone.now().day
    if base_payment_month == today_month:
        return True
    elif base_payment_month < today_month:
        if today_month - base_payment_month == 1:
            return False if base_payment_date.day < today_day else True
        return False
    else:
        return True
