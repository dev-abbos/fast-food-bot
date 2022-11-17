from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Uz', callback_data='uz'),
            InlineKeyboardButton(text='Ru', callback_data='ru'),
        ],
    ]
)

menuUz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍔 Burgerlar'),
        ],
        [
            KeyboardButton(text='🌯 Lavashlar'),
        ],
        [
            KeyboardButton(text='🍕 Pizzalar'),
        ],
        [
            KeyboardButton(text='🥙 Shaurma'),
        ],
        [
            KeyboardButton(text='🍟🍗🧃 Combo'),
        ],
        [
            KeyboardButton(text='🥗 Salatlar'),
        ],
        [
            KeyboardButton(text='🥤 Ichimliklar'),
        ],
        [
            KeyboardButton(text='⬅ Orqaga')
        ]
    ],
    resize_keyboard=True
)
menuRu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍔 Бургеры'),
        ],
        [
            KeyboardButton(text='🌯 Лавашы'),
        ],
        [
            KeyboardButton(text='🍕 Пиццы'),
        ],
        [
            KeyboardButton(text='🥙 Шаурма'),
        ],
        [
            KeyboardButton(text='🍟🍗🧃 Комбо'),
        ],
        [
            KeyboardButton(text='🥗 Салаты'),
        ],
        [
            KeyboardButton(text='🥤 Напитки'),
        ],
        [
            KeyboardButton(text='⬅ Назад')
        ]
    ],
    resize_keyboard=True
)

menuUZ = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍽 Menu'),
        ],
        [
            KeyboardButton(text='✅ Buyurtmalarni tasdiqlash')
        ],
        [
            KeyboardButton(text='⚙ Sozlash')
        ]
    ],
    resize_keyboard=True
)

menuRU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍽 Меню'),
        ],
        [
            KeyboardButton(text='✅ Подтвердить заказы')
        ],
        [
            KeyboardButton(text='⚙ Настройки')
        ]
    ],
    resize_keyboard=True
)
sozlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tilni o'zgartirish")
        ],
        [
            KeyboardButton(text='⬅ Orqaga')
        ]
    ],
    resize_keyboard=True
)
nastroyki = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Изменить язык")
        ],
        [
            KeyboardButton(text='⬅ Назад')
        ]
    ],
    resize_keyboard=True
)
tasdiqlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Telefon raqamni jo'natish", request_contact=True),
            KeyboardButton(text="📍 Geolokatsiyani jo'natish", request_location=True),
        ],
        [
            KeyboardButton(text='⬅ Orqaga')
        ]

    ],
    resize_keyboard=True
)
podtverjdat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Отправить номер телефона", request_contact=True),
            KeyboardButton(text="📍 Отправить геолокацию", request_location=True),
        ],
        [
            KeyboardButton(text='⬅ Назад')
        ]
    ],
    resize_keyboard=True
)