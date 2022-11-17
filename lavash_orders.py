from aiogram.types import Message
from config import dp
from made_orders import *

'''
kichik lavash = 19000
katta lavash = 26000
sirli lavash = 24000
tovuqli lavash = 25000
lavash mol go'shlti = 28000
lavash qalampir = 22000
'''



# Uz menudagi
@dp.message_handler(text="🌯 Kichik lavash")
async def a(msg: Message):
    if msg.from_user.id:
        order_lavash_small.append('Kichik lavash')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Kichik lavash: 19000 so\'m\n'
                     f'{len(order_lavash_small)} ta = {19000 * len(order_lavash_small)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Katta lavash")
async def a(msg: Message):
    if msg.from_user.id:
        order_lavash_big.append('Katta lavash')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Katta lavash: 26000 so\'m\n'
                     f'{len(order_lavash_big)} ta = {26000 * len(order_lavash_big)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Sirli lavash")
async def a(msg: Message):
    if msg.from_user.id:
        order_lavash_cheese.append('Sirli lavash')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Sirli lavash: 24000 so\'m\n'
                     f'{len(order_lavash_cheese)} ta = {24000 * len(order_lavash_cheese)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Tovuqli lavash")
async def a(msg: Message):
    if msg.from_user.id:
        order_lavash_chicken.append('Tovuqli lavash')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Tovuqli lavash: 25000 so\'m\n'
                     f'{len(order_lavash_chicken)} ta = {25000 * len(order_lavash_chicken)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Lavash mol go'shtli")
async def a(msg: Message):
    if msg.from_user.id:
        order_lavash_beef.append("Lavash mol go'shtli")
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Lavash mol go\'shtli: 28000 so\'m\n'
                     f'{len(order_lavash_beef)} ta = {28000 * len(order_lavash_beef)} so\'m</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Lavash qalampir")
async def a(msg: Message):
    if msg.from_user.id:
        order_lavash_pepper.append("Lavash qalampir")
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Lavash qalampir: 22000 so\'m\n'
                     f'{len(order_lavash_pepper)} ta = {22000 * len(order_lavash_pepper)} so\'m</b>',
                     parse_mode='html')

# Ru menudagi
@dp.message_handler(text="🌯 Лаваш малый")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_lavash_small.append('Лаваш малый')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Лаваш малый: 19000 сум\n'
                     f'{len(ru_order_lavash_small)} шт. = {19000 * len(ru_order_lavash_small)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Лаваш большой")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_lavash_big.append('Лаваш большой')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Лаваш большой: 26000 сум\n'
                     f'{len(ru_order_lavash_big)} шт. = {26000 * len(ru_order_lavash_big)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Лаваш с сыром")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_lavash_cheese.append('Лаваш с сыром')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Лаваш с сыром: 24000 сум\n'
                     f'{len(ru_order_lavash_cheese)} шт. = {24000 * len(ru_order_lavash_cheese)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Лаваш с курицей")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_lavash_chicken.append('Лаваш с курицей')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Лаваш с курицей: 25000 сум\n'
                     f'{len(ru_order_lavash_chicken)} шт. = {25000 * len(ru_order_lavash_chicken)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Лаваш говядина")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_lavash_beef.append('Лаваш говядина')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Лаваш говядина: 28000 сум\n'
                     f'{len(ru_order_lavash_beef)} шт. = {28000 * len(ru_order_lavash_beef)} сум</b>',
                     parse_mode='html')

@dp.message_handler(text="🌯 Лаваш с перцем")
async def a(msg: Message):
    if msg.from_user.id:
        ru_order_lavash_pepper.append('Лаваш с перцем')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Лаваш с перцем: 22000 сум\n'
                     f'{len(ru_order_lavash_pepper)} шт. = {22000 * len(ru_order_lavash_pepper)} сум</b>',
                     parse_mode='html')