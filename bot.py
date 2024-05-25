

# API_TOKEN = '6974540824:AAEnFNOFrG3pfjtqNualUVJRRrcVKkJjwBw'

import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import re
from aiogram.utils import exceptions
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import BoundFilter
from string import ascii_letters, digits

API_TOKEN = '6974540824:AAEnFNOFrG3pfjtqNualUVJRRrcVKkJjwBw'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


user_to_forward = None

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global user_to_forward
    info = await bot.get_me()
    name = info.username

    link = f'https://t.me/{name}?start={message.from_user.id}'
    if message.get_args():
        try:
            user_id = int(message.get_args())
            if user_id > 0:
                await message.answer(f"💬 Введите сообщение:")
                user_to_forward = message.get_args()
            else:
                await message.answer("❌ Ошибка не верная ссылка")
        except ValueError:
            await message.answer("❌ Ошибка не верная ссылка")
    else:
        await message.reply(f'👋🏻 Привет! Временно можно отправлять только текст в будущем будут фото и видео\n🔗 Твоя ссылка для отправки сообщений: `{link}`', parse_mode="Markdown")

@dp.message_handler()
async def forward_message(message: types.Message):
    global user_to_forward
    if user_to_forward:
        await bot.send_message(user_to_forward, f"💬 Вам пришло новое сообщение:\n`{message.text}`", parse_mode="Markdown")
        user_to_forward = None


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)