from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.types import Message, CallbackQuery
import logging
from config import dp
from aiogram.utils.exceptions import *
from menu_keyboards import *
from order_keyboards_menu_RU import *
from order_menu_keyboards_UZ import *
from made_orders import *
from burger_orders import *
from lavash_orders import *
from pizza_orders import *
from shaurma_orders import *
from combo_orders import *
from salad_orders import *
from beverage_orders import *

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer("🇺🇿 O'zingizga qulay tilni tanlang!\n"
                         "🇷🇺 Выберите для себя удобный язык!", reply_markup=lang)

@dp.callback_query_handler(text='uz')
async def uz(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    await call.message.answer("Menu", parse_mode='html', reply_markup=menuUZ)

@dp.callback_query_handler(text='ru')
async def ru(call: CallbackQuery):
    await call.answer()
    await call.message.delete()
    await call.message.answer("Меню", parse_mode='html', reply_markup=menuRU)



# MENU_BUTTONS:
@dp.message_handler(text='🍽 Menu')
async def menu(message: Message):
    await message.answer('Tanlang', reply_markup=menuUz)

@dp.message_handler(text='🍽 Меню')
async def menu(message: Message):
    await message.answer('Выберите', reply_markup=menuRu)

@dp.message_handler(text='⬅ Orqaga')
async def back(message: Message):
    await message.answer('Orqaga', reply_markup=menuUZ)

@dp.message_handler(text='⏪ Orqaga')
async def back(message: Message):
    await message.answer('Orqaga', reply_markup=menuUz)

@dp.message_handler(text='⬅ Назад')
async def back(message: Message):
    await message.answer('Назад', reply_markup=menuRU)

@dp.message_handler(text='⏪ Назад')
async def back(message: Message):
    await message.answer('Назад', reply_markup=menuRu)

@dp.message_handler(text='⚙ Sozlash')
async def soz(msg: Message):
    await msg.answer('Sozlash', reply_markup=sozlash)

@dp.message_handler(text='⚙ Настройки')
async def soz(msg: Message):
    await msg.answer('Настройки', reply_markup=nastroyki)

@dp.message_handler(text="Tilni o'zgartirish")
async def soz(msg: Message):
    await msg.answer("Сделано", reply_markup=nastroyki)

@dp.message_handler(text='Изменить язык')
async def soz(msg: Message):
    await msg.answer('Sozlandi', reply_markup=sozlash)

# MenuUz:
@dp.message_handler(text='🍔 Burgerlar')
async def bur(msg: Message):
    await msg.answer('Tanlang', reply_markup=burgerlar)

@dp.message_handler(text='🌯 Lavashlar')
async def bur(msg: Message):
    await msg.answer('Tanlang', reply_markup=lavashlar)

@dp.message_handler(text='🍕 Pizzalar')
async def bur(msg: Message):
    await msg.answer('Tanlang', reply_markup=pizzalar)

@dp.message_handler(text='🥙 Shaurma')
async def bur(msg: Message):
    await msg.answer('Tanlang', reply_markup=shaurma)

@dp.message_handler(text='🍟🍗🧃 Combo')
async def bur(msg: Message):
    await msg.answer('Tanlang', reply_markup=kombo)

@dp.message_handler(text='🥗 Salatlar')
async def bur(msg: Message):
    await msg.answer('Tanlang', reply_markup=salatlar)

@dp.message_handler(text='🥤 Ichimliklar')
async def bur(msg: Message):
    await msg.answer('Tanlang', reply_markup=ichimliklar)

# MenuRu:
@dp.message_handler(text='🍔 Бургеры')
async def bur(msg: Message):
    await msg.answer('Выберайте', reply_markup=burgeri)

@dp.message_handler(text='🌯 Лавашы')
async def bur(msg: Message):
    await msg.answer('Выберайте', reply_markup=lavashi)

@dp.message_handler(text='🍕 Пиццы')
async def bur(msg: Message):
    await msg.answer('Выберайте', reply_markup=pizzi)

@dp.message_handler(text='🥙 Шаурма')
async def bur(msg: Message):
    await msg.answer('Выберайте', reply_markup=shaurmi)

@dp.message_handler(text='🍟🍗🧃 Комбо')
async def bur(msg: Message):
    await msg.answer('Выберайте', reply_markup=komboo)

@dp.message_handler(text='🥗 Салаты')
async def bur(msg: Message):
    await msg.answer('Выберайте', reply_markup=salati)

@dp.message_handler(text='🥤 Напитки')
async def bur(msg: Message):
    await msg.answer('Выберайте', reply_markup=napitki)

@dp.message_handler(text='✅ Buyurtmalarni tasdiqlash')
async def claim(msg: Message):
    await msg.answer("Ma'lumotingizni jo'nating", reply_markup=tasdiqlash)

@dp.message_handler(text='✅ Подтвердить заказы')
async def claim(msg: Message):
    await msg.answer("Отправьте данные", reply_markup=podtverjdat)


if __name__ == '__main__':
    executor.start_polling(dp)