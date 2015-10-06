from datetime import datetime
from django.utils import timezone


def today():
    return timezone.now().date()


def normalize_weekdays(*idxs):
    """
    In datepicker weekday format is `0` for `Sunday`.
    In ISO format, `Sunday` is 7.
    """
    return map(lambda x: x if x else 7, idxs)


def format_date(_date, reverse=False):
    if reverse:
        return datetime.strptime(_date, "%d.%m.%Y").date()
    return _date.strftime('%d.%m.%Y')
