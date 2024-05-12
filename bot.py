import asyncio
from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, types
import keyboards as kb


token = "6781070415:AAGQspqRG1tRbq6zRF8cyIpFU3g-gY0XHMA"
bot = Bot(token)
dp = Dispatcher()
users = {837175722}


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Какой то текс", reply_markup=kb.main)


@dp.message(Command('run'))
async def start_cmd(message: types.Message):
    data = message.from_user.id
    print(data)
    await message.answer("Для начала торговли следуйте укажите через запятую")


@dp.message(Command('balance'))
async def start_cmd(message: types.Message):
    data = message.text
    print(data)
    await message.answer("Для начала торговли следуйте укажите через запятую")


def asd(a, message):
    pass


@dp.message()
async def wait_answer(message: types.Message):
    data = message.text
    data = data.split(',')
    if isinstance(data[0], str) and isinstance(data[1], str) and isinstance(data[2], str) and int(data[3]):
        pass
        #asd(data, message)
    else:
        await message.answer("вы допустили ошибку при вводе данных")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
