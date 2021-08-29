from datetime import date
from datetime import datetime
from datetime import timedelta


def update_initProcess(begin_date: date, final_date: date, step_date: int):
    return int(step_date / ((final_date - begin_date).days + 1) * 100)


def update_timeScope(start_date: date, step_date: int):
    end_date = start_date + timedelta(days=step_date - 1)
    time_scope = 'custom:' + start_date.isoformat() + ':' + end_date.isoformat()
    return time_scope


def format_timeInfo(time_info: str):
    if time_info.find('年') != -1:
        msg_date = datetime.strptime(time_info, "%Y年%m月%d日")
    elif time_info.find('日') != -1:
        msg_date = datetime.strptime(time_info, "%m月%d日")
        msg_date = msg_date.replace(year=2021)
    else:
        msg_date = date.today()
    date_str = msg_date.strftime('%Y-%m-%d')
    return date_str
