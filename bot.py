import asyncio
import json
import logging
from typing import Any, Dict
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, types, F
import keyboards as kb
from aiogram.types import ReplyKeyboardRemove


token = "6781070415:AAGQspqRG1tRbq6zRF8cyIpFU3g-gY0XHMA"
bot = Bot(token)
dp = Dispatcher()
users = {837175722}
list = ["PEPEUSDT", "NDOUSDT", "QWEUSDT"]


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Какой то текс", reply_markup=kb.main)


@dp.message(Command('run'))
async def start_cmd(message: types.Message):
    data = message.from_user.id
    print(data)
    await message.answer("Для начала торговли следуйте укажите через запятую")


class Form(StatesGroup):
    coin = State()
    lever = State()
    summa = State()


@dp.message(Command('buy'))
async def command_start(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.coin)
    await message.answer(
        "Какую монету покупать?"
    )


@dp.message(Command("cancel"))
@dp.message(F.text.casefold() == "cancel")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled."
    )


@dp.message(Form.coin)
async def process_name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(coin=message.text)
    await state.clear()
    await state.set_state(Form.lever)
    await message.answer(
        f" Какое установить плечо для торговли?")


@dp.message(Form.lever)
async def process_name(message: types.Message, state: FSMContext) -> None:
    await state.update_data(lever=message.text)
    await state.clear()
    await state.set_state(Form.summa)
    await message.answer(
        f" На какую сумму хотите купить?")


@dp.message(Form.summa)
async def process_language(message: types.Message, state: FSMContext) -> None:
    data = await state.update_data(summa=message.text)
    await state.clear()
    await state.clear()
    await show_summary(message=message, data=data)


async def show_summary(message: types.Message, data: Dict[str, Any], positive: bool = True) -> None:
    coin = data["coin"]
    lever = data["lever"]
    summa = data.get("summa")
    if coin in list:
        await message.answer(f" Выбрана монета {coin}")
    if int(lever):
        await message.answer(f"Установлено плечо {lever}")
    if float(summa):
        await message.answer(f"На сумму {summa}")
    print(coin, type(lever), type(summa))


@dp.message(Command('info'))
async def start_cmd(message: types.Message):
    await message.answer("Данный бот создан для покупки и выставления ордеров. Перед покупкой убедитесь что все "
                         "параметры выставлены правильно, а именно монета которую хотите купить, плечо покупки"
                         "и сумма на которую хотите купить. Сумму нужно указывать как показано 00.00")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
