from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

burgerlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍔 Burger klassik'),
            KeyboardButton(text='🍔 Burger junior'),
            KeyboardButton(text='🍔 Burger senior'),
        ],
        [
            KeyboardButton(text='🍔 Gamburger'),
            KeyboardButton(text='🍔 Chizburger'),
            KeyboardButton(text='🍔 Chiliburger'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
lavashlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌯 Kichik lavash'),
            KeyboardButton(text='🌯 Katta lavash'),
            KeyboardButton(text='🌯 Sirli lavash'),
        ],
        [
            KeyboardButton(text='🌯 Tovuqli lavash'),
            KeyboardButton(text="🌯 Lavash mol go'shtli"),
            KeyboardButton(text="🌯 Lavash qalampir"),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
pizzalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍕 Pizza klassik'),
            KeyboardButton(text='🍕 Pizza vegetarian'),
            KeyboardButton(text='🍕 Pizza lazzat'),
        ],
        [
            KeyboardButton(text='🍕 Pizza special'),
            KeyboardButton(text="🍕 Pizza sirli"),
            KeyboardButton(text="🍕 Pizza margarita"),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
shaurma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🥙 Shaurma yarim'),
            KeyboardButton(text="🥙 Shaurma katta"),
            KeyboardButton(text="🥙 Shaurma super"),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
kombo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍟🍗🧃 Kombo set'),
            KeyboardButton(text="🍟🍗🧃 Kombo duet"),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
salatlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🥗 Grekcha salat'),
            KeyboardButton(text='🥗 Italyancha salat'),
        ],
        [
            KeyboardButton(text='🥗 Achuchu'),
            KeyboardButton(text='🥗 Olivye'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)
ichimliklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🥤 Kola 1L'),
            KeyboardButton(text='🥤 Kola 1.5L'),
            KeyboardButton(text='🥤 Fanta 1L'),
            KeyboardButton(text='🥤 Fanta 1.5L'),
        ],
        [
            KeyboardButton(text='🥤 Gidrolife 0.5L'),
            KeyboardButton(text='🥤 Gidrolife 1L'),
            KeyboardButton(text='🥤 Shaffof 0.5L'),
            KeyboardButton(text='🥤 Shaffof 1L'),
        ],
        [
            KeyboardButton(text='🧃 Sok 1L'),
            KeyboardButton(text='🧃 Prost Sok 1L'),
            KeyboardButton(text='🧃 Bliss 1L'),
            KeyboardButton(text='🧃 Nash sad 1L'),
        ],
        [
            KeyboardButton(text='⏪ Orqaga')
        ]
    ],
    resize_keyboard=True
)