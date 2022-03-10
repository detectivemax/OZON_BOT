import datetime

from data.data import cursor, connect


# Выбрать один
import monthdelta


def bd_get_one(body):
    try:
        cursor.execute(body)
        user = cursor.fetchone()
        return user[0]
    except TypeError:
        return None


# Выбрать много
def bd_get_many(body):
    cursor.execute(body)
    rows = cursor.fetchall()
    get_list = []
    for row in rows:
        for x in row:
            get_list.append(x)
    return get_list


# Выполнить команду
def bd_set(body):
    cursor.execute(body)
    connect.commit()


# Получить дату
# + x дней
def get_date(x='0'):
    x = str(x)

    if x.find("m") != -1:
        tine_now = datetime.datetime.now() + monthdelta.monthdelta(int(x.replace("m", ""))) + datetime.timedelta(days=1)
        date = f"{tine_now.date()}"

    else:
        tine_now = datetime.datetime.now() + datetime.timedelta(days=int(x))
        date = f"{tine_now.date()}"

    date = f"{date[8:]}.{date[5:7]}.{date[:4]}"

    return date


# Получить время
# + x часов
def get_time(x=0):
    tine_now = datetime.datetime.now() + datetime.timedelta(hours=x)
    time = f"{tine_now.time()}"
    time = time[:8]
    return time


# Максимальное значение
def max_id(function):
    try:
        task_id = bd_get_many(function)
        task_id = max(task_id)
    except ValueError:
        task_id = 0

    return task_id


def get_num(x):
    num = ""
    for let in x:
        if let.isdigit() is True:
            num += let

    if num == "":
        num = 0
    return int(num)
