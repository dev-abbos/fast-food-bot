from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

burgeri = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍔 Бургер классик'),
            KeyboardButton(text='🍔 Бургер юниор'),
            KeyboardButton(text='🍔 Бургер сеньор'),
        ],
        [
            KeyboardButton(text='🍔 Гамбургер'),
            KeyboardButton(text='🍔 Чизбургер'),
            KeyboardButton(text='🍔 Чилибургер'),
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
lavashi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌯 Лаваш малый'),
            KeyboardButton(text='🌯 Лаваш большой'),
            KeyboardButton(text='🌯 Лаваш с сыром'),
        ],
        [
            KeyboardButton(text='🌯 Лаваш с курицей'),
            KeyboardButton(text="🌯 Лаваш говядина"),
            KeyboardButton(text="🌯 Лаваш с перцем"),
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
pizzi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍕 Пицца классик'),
            KeyboardButton(text='🍕 Пицца вегетариан'),
            KeyboardButton(text='🍕 Пицца лаззет'),
        ],
        [
            KeyboardButton(text='🍕 Пицца спешл'),
            KeyboardButton(text="🍕 Пицца с сыром"),
            KeyboardButton(text="🍕 Пицца маргарита"),
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
shaurmi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🥙 Шаурма половина'),
            KeyboardButton(text="🥙 Шаурма большой"),
            KeyboardButton(text="🥙 Шаурма супер"),
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
komboo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍟🍗🧃 Комбо сет'),
            KeyboardButton(text="🍟🍗🧃 Комбо дует"),
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
salati = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🥗 Греческий салат'),
            KeyboardButton(text='🥗 Итальянский салат'),
        ],
        [
            KeyboardButton(text='🥗 Салат помидоры'),
            KeyboardButton(text='🥗 Оливье'),
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
napitki = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🥤 Кола 1л'),
            KeyboardButton(text='🥤 Кола 1.5л'),
            KeyboardButton(text='🥤 Фанта 1л'),
            KeyboardButton(text='🥤 Фанта 1.5л'),
        ],
        [
            KeyboardButton(text='🥤 Гидролайф 0.5л'),
            KeyboardButton(text='🥤 Гидролайф 1л'),
            KeyboardButton(text='🥤 Шаффоф 0.5л'),
            KeyboardButton(text='🥤 Шаффоф 1л'),
        ],
        [
            KeyboardButton(text='🧃 Сок 1л'),
            KeyboardButton(text='🧃 Просто Сок 1л'),
            KeyboardButton(text='🧃 Блисс 1л'),
            KeyboardButton(text='🧃 Наш Сад 1л'),
        ],
        [
            KeyboardButton(text='⏪ Назад')
        ]
    ],
    resize_keyboard=True
)
