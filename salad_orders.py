
from aiogram.types import Message
from config import dp
from made_orders import *

'''
grekcha salat = 26000
italyancha salat = 24000
achuchu = 13000
olivye = 15000
'''

# Uz menudagi
@dp.message_handler(text="🥗 Grekcha salat")
async def a(msg: Message):
    if msg.from_user.id:
        order_salad_greeks.append('Grekcha salat')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Grekcha salat: 26000 so\'m\n'
                     f'{len(order_salad_greeks)} ta = {26000 * len(order_salad_greeks)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥗 Italyancha salat")
async def a(msg: Message):
    if msg.from_user.id:
        order_salad_italian.append('Italyancha salat')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Italyancha salat: 24000 so\'m\n'
                     f'{len(order_salad_italian)} ta = {24000 * len(order_salad_italian)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥗 Achuchu")
async def a(msg: Message):
    if msg.from_user.id:
        order_salad_tomato.append('Achuchu')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Achuchu: 13000 so\'m\n'
                     f'{len(order_salad_tomato)} ta = {13000 * len(order_salad_tomato)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥗 Olivye")
async def a(msg: Message):
    if msg.from_user.id:
        order_salad_olivye.append('Olivye')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Olivye: 15000 so\'m\n'
                     f'{len(order_salad_olivye)} ta = {15000 * len(order_salad_olivye)} so\'m</b>',
                     parse_mode='html')


# Ru menudagi
@dp.message_handler(text="🥗 Греческий салат")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_salad_greeks.append('Греческий салат')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Греческий салат: 26000 сум\n'
                     f'{len(ru_order_salad_greeks)} шт. = {26000 * len(ru_order_salad_greeks)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥗 Итальянский салат")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_salad_italian.append('Итальянский салат')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Итальянский салат: 24000 сум\n'
                     f'{len(ru_order_salad_italian)} шт. = {24000 * len(ru_order_salad_italian)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥗 Салат помидоры")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_salad_tomato.append('Салат помидоры')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Салат помидоры: 13000 сум\n'
                     f'{len(ru_order_salad_tomato)} шт. = {13000 * len(ru_order_salad_tomato)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥗 Оливье")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_salad_olivye.append('Оливье')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Оливье: 15000 сум\n'
                     f'{len(ru_order_salad_olivye)} шт. = {15000 * len(ru_order_salad_olivye)} сум</b>',
                     parse_mode='html')