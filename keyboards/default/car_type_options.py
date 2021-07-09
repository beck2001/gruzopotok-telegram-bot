from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

car_type_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"Рефрижератор"),
            KeyboardButton(text=f"Тент")
        ],
        [
            KeyboardButton(text=f"Самосвал"),
            KeyboardButton(text=f"Изотерм")
        ],
        [
            KeyboardButton(text=f"Автотранспортер"),
            KeyboardButton(text=f"Кран")
        ]
    ],
    resize_keyboard=True
)
