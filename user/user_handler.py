import asyncio
import datetime

from config.config import ADMIN_ID
from data.data import cursor
from functions import bd_get_one, bd_set, get_date, get_time, max_id, bd_get_many
from main import bot, dp, types
from parsing import ozon_get_analytics_data, data_to_excel


#
# Сегодня
@dp.callback_query_handler(text_contains='period_today')
async def admin_sales_percent(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    content = ozon_get_analytics_data(get_date(), get_date())
    data_to_excel(content)
    doc = open(r'month_result.xlsx', 'rb')
    caption = f"Отчет за {get_date()}"
    await bot.send_document(user_id, doc, caption=caption)


#
# Вчера
@dp.callback_query_handler(text_contains='period_yesterday')
async def admin_sales_percent(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    content = ozon_get_analytics_data(get_date(-1), get_date(-1))
    data_to_excel(content)
    doc = open(r'month_result.xlsx', 'rb')
    caption = f"Отчет за {get_date(-1)}"
    await bot.send_document(user_id, doc, caption=caption)


#
# Неделя
@dp.callback_query_handler(text_contains='period_week')
async def admin_sales_percent(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    content = ozon_get_analytics_data(get_date(-6), get_date())
    data_to_excel(content)
    doc = open(r'month_result.xlsx', 'rb')
    caption = f"Отчет за неделю от {get_date(-6)} до {get_date()}"
    await bot.send_document(user_id, doc, caption=caption)


#
# Месяц
@dp.callback_query_handler(text_contains='period_month')
async def admin_sales_percent(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    content = ozon_get_analytics_data(get_date('-1m'), get_date())
    data_to_excel(content)
    doc = open(r'month_result.xlsx', 'rb')
    caption = f"Отчет за неделю от {get_date('-1m')} до {get_date()}"
    await bot.send_document(user_id, doc, caption=caption)


# Ежемесячный отчет
async def post():
    time_end = get_date(-1)
    time_start = get_date('-1m')
    time_start = f"01{time_start[2::]}"

    content = ozon_get_analytics_data(time_start, time_end)
    data_to_excel(content)
    doc = open(r'month_result.xlsx', 'rb')
    caption = f"Отчет за {time_start[3::]}"

    users = bd_get_many(f"SELECT user_id FROM user_stage")
    for user_id in users:
        await bot.send_document(user_id, doc, caption=caption)


async def posting():
    try:
        time_now = datetime.datetime.now()

        if str(time_now.day) == "1":
            max_post_id = max_id(f"SELECT post_id FROM post_status_info")
            check_time = bd_get_one(f"SELECT time FROM post_status_info WHERE post_id = {max_post_id}")
            check_date = bd_get_one(f"SELECT date FROM post_status_info WHERE post_id = {max_post_id}")

            print(check_time, get_time(), check_date, get_date())
            if check_time != get_time() and check_date != get_date():
                # Функция постинга
                await post()

    except Exception as e:
        await bot.send_massage(632392043, e)

    when_to_call = loop.time() + delay  # delay -- промежуток времени в секундах.
    loop.call_at(when_to_call, my_callback)


def my_callback():
    asyncio.ensure_future(posting())


delay = 60.0
loop = asyncio.get_event_loop()
my_callback()

