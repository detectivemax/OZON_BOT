from commnds_handler__kb import period_kb
from config.config import ADMIN_ID
from functions import bd_get_one, bd_set, get_date, get_time
from main import bot, dp, types


# Обработчик команды 'Start'
from parsing import ozon_get_analytics_data, data_to_excel
from user.user_handler import post


@dp.message_handler(commands=['start'])
async def send_welcome(message):
    user_id = message.from_user.id
    check = bd_get_one(f"SELECT user_id FROM user_stage WHERE user_id = '{user_id}'")

    # Проверка регистрации
    if check is None:
        # Бд состояния пользователя
        bd_set(f"INSERT INTO user_stage VALUES('{user_id}', '{0}', '{0}', '{0}')")

    await bot.send_message(user_id, "За каой период отправить сводку?", reply_markup=period_kb())
    content = ozon_get_analytics_data("01.02.2022", "28.02.2022")
    data_to_excel(content)
    doc = open(r'month_result.xlsx', 'rb')
    caption = f"Отчет за неделю от {get_date('-1m')} до {get_date()}"
    await bot.send_document(user_id, doc, caption=caption)