import datetime

print(__name__)

def get_now_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')