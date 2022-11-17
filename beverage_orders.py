from aiogram.types import Message
from config import dp
from made_orders import *


'''
kola1 = 11000
kola1.5 = 14000
fanta1 = 11000
fanta1.5 = 13000
gidrolife0.5 = 4000
gidrolife1 = 5000
shaffof0.5 = 3000
shaffof1 = 4500
sok = 12000
prost sok = 13000
bliss = 13500
nash sad = 15000
'''

# Uz menudagi
@dp.message_handler(text="🥤 Kola 1L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_cola1.append('Kola 1L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Kola 1L: 11000 so\'m\n'
                     f'{len(order_beverage_cola1)} ta = {11000 * len(order_beverage_cola1)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Kola 1.5L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_cola15.append('Kola 1.5L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Kola 1.5L: 14000 so\'m\n'
                     f'{len(order_beverage_cola15)} ta = {14000 * len(order_beverage_cola15)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Fanta 1L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_fanta1.append('Fanta 1L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Fanta 1L: 11000 so\'m\n'
                     f'{len(order_beverage_fanta1)} ta = {11000 * len(order_beverage_fanta1)} so\'m</b>',
                     parse_mode='html')


@dp.message_handler(text="🥤 Fanta 1.5L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_fanta15.append('Fanta 1.5L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Fanta 1.5L: 13000 so\'m\n'
                     f'{len(order_beverage_fanta15)} ta = {13000 * len(order_beverage_fanta15)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Gidrolife 0.5L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_hydro05.append('Gidrolife 0.5L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Gidrolife 0.5L: 4000 so\'m\n'
                     f'{len(order_beverage_hydro05)} ta = {4000 * len(order_beverage_hydro05)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Gidrolife 1L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_hydro1.append('Gidrolife 1L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Gidrolife 1L: 5000 so\'m\n'
                     f'{len(order_beverage_hydro1)} ta = {5000 * len(order_beverage_hydro1)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Shaffof 0.5L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_shaff05.append('Shaffof 0.5L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Shaffof 0.5L: 3000 so\'m\n'
                     f'{len(order_beverage_shaff05)} ta = {3000 * len(order_beverage_shaff05)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Shaffof 1L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_shaff1.append('Shaffof 1L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Shaffof 1L: 4500 so\'m\n'
                     f'{len(order_beverage_shaff1)} ta = {4500 * len(order_beverage_shaff1)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🧃 Sok 1L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_sok.append('Sok 1L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Sok 1L: 12000 so\'m\n'
                     f'{len(order_beverage_sok)} ta = {12000 * len(order_beverage_sok)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🧃 Prosto Sok 1L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_prostosok.append('Prosto Sok 1L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Prosto Sok 1L: 13000 so\'m\n'
                     f'{len(order_beverage_prostosok)} ta = {13000 * len(order_beverage_prostosok)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🧃 Bliss 1L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_bliss.append('Bliss 1L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Bliss 1L: 13500 so\'m\n'
                     f'{len(order_beverage_bliss)} ta = {13500 * len(order_beverage_bliss)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🧃 Nash sad 1L")
async def a(msg: Message):
    if msg.from_user.id:
        order_beverage_nashsad.append('Nash sad 1L')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Nash sad 1L: 15000 so\'m\n'
                     f'{len(order_beverage_nashsad)} ta = {15000 * len(order_beverage_nashsad)} so\'m</b>',
                     parse_mode='html')


# RU menudagi

@dp.message_handler(text="🥤 Кола 1л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_cola1.append('Кола 1л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Кола 1л: 11000 сум\n'
                     f'{len(ru_order_beverage_cola1)} шт. = {11000 * len(ru_order_beverage_cola1)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Кола 1.5л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_cola15.append('Кола 1.5л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Кола 1л: 14000 сум\n'
                     f'{len(ru_order_beverage_cola15)} шт. = {14000 * len(ru_order_beverage_cola15)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Фанта 1л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_fanta1.append('Фанта 1л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Фанта 1л: 11000 сум\n'
                     f'{len(ru_order_beverage_fanta1)} шт. = {11000 * len(ru_order_beverage_fanta1)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Фанта 1.5л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_fanta15.append('Фанта 1.5л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Фанта 1.5л: 13000 сум\n'
                     f'{len(ru_order_beverage_fanta15)} шт. = {13000 * len(ru_order_beverage_fanta15)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Гидролайф 0.5л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_hydro05.append('Гидролайф 0.5л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Гидролайф 0.5л: 4000 сум\n'
                     f'{len(ru_order_beverage_hydro05)} шт. = {4000 * len(ru_order_beverage_hydro05)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Гидролайф 1л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_hydro1.append('Гидролайф 1л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Гидролайф 1л: 5000 сум\n'
                     f'{len(ru_order_beverage_hydro1)} шт. = {5000 * len(ru_order_beverage_hydro1)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Шаффоф 0.5л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_shaff05.append('Шаффоф 0.5л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Шаффоф 0.5л: 3000 сум\n'
                     f'{len(ru_order_beverage_shaff05)} шт. = {3000 * len(ru_order_beverage_shaff05)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥤 Шаффоф 1л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_shaff1.append('Шаффоф 1л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Шаффоф 1л: 4500 сум\n'
                     f'{len(ru_order_beverage_shaff1)} шт. = {4500 * len(ru_order_beverage_shaff1)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🧃 Сок 1л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_sok.append('Сок 1л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Сок 1л: 12000 сум\n'
                     f'{len(ru_order_beverage_sok)} шт. = {12000 * len(ru_order_beverage_sok)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🧃 Просто Сок 1л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_prostosok.append('Просто Сок 1л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Просто Сок 1л: 13000 сум\n'
                     f'{len(ru_order_beverage_prostosok)} шт. = {13000 * len(ru_order_beverage_prostosok)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🧃 Блисс 1л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_bliss.append('Блисс 1л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Блисс 1л: 13500 сум\n'
                     f'{len(ru_order_beverage_bliss)} шт. = {13500 * len(ru_order_beverage_bliss)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🧃 Наш Сад 1л")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_beverage_nashsad.append('Наш Сад 1л')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Наш Сад 1л: 15000 сум\n'
                     f'{len(ru_order_beverage_nashsad)} шт. = {15000 * len(ru_order_beverage_nashsad)} сум</b>',
                     parse_mode='html')