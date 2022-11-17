
from aiogram.types import Message
from config import dp
from made_orders import *


'''
burger klassik = 24000
burger junior = 21000
burger senior = 27000
gamburger = 25000
chizburger = 24000
chiliburger = 26000
'''

# Uz menudagi
@dp.message_handler(text="🍔 Burger klassik")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Burger klassik')
        await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                         f"Burger klassik: 24000 so\'m \n"
                         f"{data.count('Burger klassik')} ta = {24000 * data.count('Burger klassik')} so\'m</b>", parse_mode='html')

@dp.message_handler(text="🍔 Burger junior")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Burger junior')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                         f'Burger junior: 21000 so\'m\n'
                         f"{data.count('Burger junior')} ta = {21000 * data.count('Burger junior')} so\'m</b>", parse_mode='html')

@dp.message_handler(text="🍔 Burger senior")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Burger senior')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Burger senior: 27000 so\'m\n'
                     f"{data.count('Burger senior')} ta = {27000 * data.count('Burger senior')} so\'m</b>", parse_mode='html')

@dp.message_handler(text="🍔 Gamburger")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Gamburger')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Gamburger: 25000 so\'m\n'
                     f"{data.count('Gamburger')} ta = {25000 * data.count('Gamburger')} so\'m</b>", parse_mode='html')

@dp.message_handler(text="🍔 Chizburger")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Chizburger')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Chizburger: 24000 so\'m\n'
                     f"{data.count('Chizburger')} ta = {24000 * data.count('Chizburger')} so\'m</b>", parse_mode='html')

@dp.message_handler(text="🍔 Chiliburger")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Chiliburger')
    await msg.answer(f'<b>Buyurtma qabul qilindi!\n\n'
                     f'Chiliburger: 26000 so\'m\n'
                     f"{data.count('Chiliburger')} ta = {26000 * data.count('Chiliburger')} so\'m</b>", parse_mode='html')

# Ru menudagi
@dp.message_handler(text="🍔 Бургер классик")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Бургер классик')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Бургер классик: 24000 сум\n'
                     f"{data.count('Бургер классик')} ta = {24000 * data.count('Бургер классик')} сум</b>", parse_mode='html')

@dp.message_handler(text="🍔 Бургер юниор")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Бургер юниор')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Бургер юниор: 21000 сум\n'
                     f"{data.count('Бургер юниор')} ta = {21000 * data.count('Бургер юниор')} сум</b>", parse_mode='html')

@dp.message_handler(text="🍔 Бургер сеньор")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Бургер сеньор')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Бургер сеньор: 27000 сум\n'
                     f"{data.count('Бургер сеньор')} ta = {27000 * data.count('Бургер сеньор')} сум</b>", parse_mode='html')

@dp.message_handler(text="🍔 Гамбургер")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Гамбургер')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Гамбургер: 25000 сум\n'
                     f"{data.count('Гамбургер')} ta = {25000 * data.count('Гамбургер')} сум</b>", parse_mode='html')

@dp.message_handler(text="🍔 Чизбургер")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Чизбургер')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Чизбургер: 24000 сум\n'
                     f"{data.count('Чизбургер')} ta = {24000 * data.count('Чизбургер')} сум</b>", parse_mode='html')

@dp.message_handler(text="🍔 Чилибургер")
async def a(msg: Message):
    if msg.from_user.id:
        data.append('Чилибургер')
    await msg.answer(f'<b>Заказ принят!\n\n'
                     f'Чилибургер: 26000 сум\n'
                     f"{data.count('Чилибургер')} ta = {26000 * data.count('Чилибургер')} сум</b>", parse_mode='html')

