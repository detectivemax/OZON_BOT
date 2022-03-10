import asyncio
from aiogram import Bot, Dispatcher, executor, types
from config import config

# Инициализация бота
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    from commands_handler import dp
    # from message_handler import dp
    # from admin.admin_handler import dp
    from user.user_handler import dp

    executor.start_polling(dp, skip_updates=True)


    # print(get_date())
    # content = ozon_get_analytics_data(get_date(-30), get_date())
    # data_to_excel(content)
