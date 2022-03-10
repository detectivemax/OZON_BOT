# Период
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def period_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Сегодня', callback_data='period_today'),
            ],
            [
                InlineKeyboardButton(text='Вчера', callback_data='period_yesterday'),
            ],
            [
                InlineKeyboardButton(text='Неделя', callback_data='period_week')
            ],
            [
                InlineKeyboardButton(text='Месяц', callback_data='period_month')
            ]
        ]
    )
    return kb
