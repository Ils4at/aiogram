import asyncio
from aiogram.filters import CommandStart
from aiogram import Bot, Dispatcher, types


token = "6781070415:AAGQspqRG1tRbq6zRF8cyIpFU3g-gY0XHMA"
bot = Bot(token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Эта была команда старт")



async def main():
    await dp.start_polling(bot)


asyncio.run(main())
