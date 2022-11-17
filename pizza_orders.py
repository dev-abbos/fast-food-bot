
from aiogram.types import Message
from config import dp
from made_orders import *

'''
pizza klassik = 39000
pizza vegetarian = 42000
pizza lazzat 48000
pizza special = 51000
pizza sirli = 43000
pizza margarita = 53000
'''

# Uz menudagi
@dp.message_handler(text="🍕 Pizza klassik")
async def a(msg: Message):
    if msg.from_user.id:
        order_pizza_classic.append('Pizza klassik')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Pizza klassik: 39000 so\'m\n'
                     f'{len(order_pizza_classic)} ta = {39000 * len(order_pizza_classic)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Pizza vegetarian")
async def a(msg: Message):
    if msg.from_user.id:
        order_pizza_vegetarian.append('Pizza vegetarian')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Pizza vegetarian: 42000 so\'m\n'
                     f'{len(order_pizza_vegetarian)} ta = {42000 * len(order_pizza_vegetarian)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Pizza lazzat")
async def a(msg: Message):
    if msg.from_user.id:
        order_pizza_lazzat.append('Pizza lazzat')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Pizza lazzat: 48000 so\'m\n'
                     f'{len(order_pizza_lazzat)} ta = {48000 * len(order_pizza_lazzat)} so\'m</b>',
                     parse_mode='html')


@dp.message_handler(text="🍕 Pizza special")
async def a(msg: Message):
    if msg.from_user.id:
        order_pizza_special.append('Pizza special')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Pizza special: 51000 so\'m\n'
                     f'{len(order_pizza_special)} ta = {51000 * len(order_pizza_special)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Pizza sirli")
async def a(msg: Message):
    if msg.from_user.id:
        order_pizza_cheese.append('Pizza sirli')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Pizza sirli: 43000 so\'m\n'
                     f'{len(order_pizza_cheese)} ta = {43000 * len(order_pizza_cheese)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Pizza margarita")
async def a(msg: Message):
    if msg.from_user.id:
        order_pizza_margarita.append('Pizza margarita')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Pizza margarita: 53000 so\'m\n'
                     f'{len(order_pizza_margarita)} ta = {53000 * len(order_pizza_margarita)} so\'m</b>',
                     parse_mode='html')


# Ru menudagi
@dp.message_handler(text="🍕 Пицца классик")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_pizza_classic.append('Пицца классик')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Пицца классик: 39000 сум\n'
                     f'{len(ru_order_pizza_classic)} шт. = {39000 * len(ru_order_pizza_classic)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Пицца вегетариан")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_pizza_vegetarian.append('Пицца вегетариан')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Пицца вегетариан: 42000 сум\n'
                     f'{len(ru_order_pizza_vegetarian)} шт. = {42000 * len(ru_order_pizza_vegetarian)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Пицца лаззет")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_pizza_lazzat.append('Пицца лаззет')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Пицца лаззет: 48000 сум\n'
                     f'{len(ru_order_pizza_lazzat)} шт. = {48000 * len(ru_order_pizza_lazzat)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Пицца спешл")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_pizza_special.append('Пицца спешл')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Пицца спешл: 51000 сум\n'
                     f'{len(ru_order_pizza_special)} шт. = {51000 * len(ru_order_pizza_special)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Пицца с сыром")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_pizza_cheese.append('Пицца с сыром')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Пицца спешл: 43000 сум\n'
                     f'{len(ru_order_pizza_cheese)} шт. = {43000 * len(ru_order_pizza_cheese)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🍕 Пицца маргарита")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_pizza_margarita.append('Пицца маргарита')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Пицца спешл: 53000 сум\n'
                     f'{len(ru_order_pizza_margarita)} шт. = {53000 * len(ru_order_pizza_margarita)} сум</b>',
                     parse_mode='html')

