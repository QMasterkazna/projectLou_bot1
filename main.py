Token_Api = '5962999120:AAEO3YAT1hIBckQPRZjYoZtnJGETv_6Fq30'

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(Token_Api)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton("Csharp")).insert(KeyboardButton("Python"))
kb.add(KeyboardButton("C")).insert(KeyboardButton("JavaScript"))


async def on_startup(_):
    print("im ready")


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("Выбери один из языков, который ты хочешь изучить: ", reply_markup=kb)


@dp.message_handler()
async def answer(message: types.Message):
    if message.text =="Python":
        await message.reply("инфа о python", reply_markup=ReplyKeyboardRemove())
    elif message.text =="Csharp":
        await message.reply("инфа о C#", reply_markup=ReplyKeyboardRemove())
    elif message.text == "C":
        await message.reply("инфа о C", reply_markup=ReplyKeyboardRemove())
    elif message.text == "JavaScript":
        await message.reply("инфа о JavaScript", reply_markup=ReplyKeyboardRemove())



if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
