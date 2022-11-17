from aiogram.types import Message
from config import dp
from made_orders import *


'''
combo set = 32000
combo duet = 33000
'''


# Uz menudagi
@dp.message_handler(text="🍟🍗🧃 Kombo set")
async def a(msg: Message):
    if msg.from_user.id:
        order_combo_set.append('Kombo set')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Kombo set: 32000 so\'m\n'
                     f'{len(order_combo_set)} ta = {32000 * len(order_combo_set)} so\'m</b>',
                     parse_mode='html')


@dp.message_handler(text="🍟🍗🧃 Kombo duet")
async def a(msg: Message):
    if msg.from_user.id:
        order_combo_duet.append('Kombo duet')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Kombo duet: 33000 so\'m\n'
                     f'{len(order_combo_duet)} ta = {33000 * len(order_combo_duet)} so\'m</b>',
                     parse_mode='html')


# Ru menudagi
@dp.message_handler(text="🍟🍗🧃 Комбо сет")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_combo_set.append('Комбо сет')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Комбо сет: 32000 сум\n'
                     f'{len(ru_order_combo_set)} шт. = {32000 * len(ru_order_combo_set)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🍟🍗🧃 Комбо дует")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_combo_duet.append('Комбо дует')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Комбо дует: 33000 сум\n'
                     f'{len(ru_order_combo_duet)} шт. = {33000 * len(ru_order_combo_duet)} сум</b>',
                     parse_mode='html')