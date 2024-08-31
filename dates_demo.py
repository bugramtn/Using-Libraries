import datetime

def do_datetime_stuff():
    now = datetime.datetime.now()
    print(now)

    now_formatted = now.strftime("%d/%m/%Y %H:%M")
    print(now_formatted)

    today = datetime.date.today()
    today_formatted = today.strftime("%d/%m/%Y")
    print(today_formatted)

    yesterday = today - datetime.timedelta(days = 1)
    yesterday_formatted = yesterday.strftime("%d/%m/%Y")
    print(yesterday_formatted)

do_datetime_stuff()