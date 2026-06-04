from datetime import datetime


def now_utc():
    return datetime.utcnow()


def format_date(dt: datetime):
    if not dt:
        return None
    return dt.strftime("%Y-%m-%d %H:%M:%S")