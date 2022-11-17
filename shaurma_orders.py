from aiogram.types import Message
from config import dp
from made_orders import *


'''
shaurma yarim = 18000
shaurma katta = 25000
shaurma super = 27000
'''

# Uz menudagi
@dp.message_handler(text="🥙 Shaurma yarim")
async def a(msg: Message):
    if msg.from_user.id:
        order_shaurma_half.append('Shaurma yarim')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Shaurma yarim: 18000 so\'m\n'
                     f'{len(order_shaurma_half)} ta = {18000 * len(order_shaurma_half)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥙 Shaurma katta")
async def a(msg: Message):
    if msg.from_user.id:
        order_shaurma_big.append('Shaurma katta')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Shaurma katta: 25000 so\'m\n'
                     f'{len(order_shaurma_big)} ta = {25000 * len(order_shaurma_big)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🥙 Shaurma super")
async def a(msg: Message):
    if msg.from_user.id:
        order_shaurma_super.append('Shaurma super')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Shaurma super: 27000 so\'m\n'
                     f'{len(order_shaurma_super)} ta = {27000 * len(order_shaurma_super)} so\'m</b>',
                     parse_mode='html')

# Ru menudagi
@dp.message_handler(text="🥙 Шаурма половина")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_shaurma_half.append('Шаурма половина')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Шаурма половина: 18000 сум\n'
                     f'{len(ru_order_shaurma_half)} шт. = {18000 * len(ru_order_shaurma_half)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥙 Шаурма большой")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_shaurma_big.append('Шаурма большой')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Шаурма большой: 25000 сум\n'
                     f'{len(ru_order_shaurma_big)} шт. = {25000 * len(ru_order_shaurma_big)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🥙 Шаурма супер")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_shaurma_super.append('Шаурма супер')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Шаурма супер: 27000 сум\n'
                     f'{len(ru_order_shaurma_super)} шт. = {27000 * len(ru_order_shaurma_super)} сум</b>',
                     parse_mode='html')