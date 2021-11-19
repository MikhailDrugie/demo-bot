import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import Text

from config import TOKEN
import messages
import keyboards as kb
from ids import file_id_list as ID_LIST

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s] %(message)s',
                    level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

ABOUT_US_GIF = ID_LIST[0]
PHOTO = ID_LIST[1]
VIDEO = ID_LIST[2]
AUDIO = ID_LIST[3]


@dp.callback_query_handler(lambda c: c.data == 'about_us')
async def process_callback_about_us(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_animation(callback_query.from_user.id, ABOUT_US_GIF)
    await bot.send_message(callback_query.from_user.id, messages.about_us)


@dp.callback_query_handler(lambda c: c.data == 'address')
async def process_callback_address(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, messages.address)


@dp.callback_query_handler(lambda c: c.data == 'contacts')
async def process_callback_contacts(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, messages.contacts)


@dp.callback_query_handler(lambda c: c.data == 'site')
async def process_callback_site(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, messages.site)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(messages.start, reply_markup=kb.media_kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(messages.help_,
                        reply_markup=kb.inline_kb_info)


@dp.message_handler(Text(equals=messages.photo))
async def process_photo_command(message: types.Message):
    await message.reply("Our pride:")
    await bot.send_photo(message.from_user.id, PHOTO)


@dp.message_handler(Text(equals=messages.song))
async def process_audio_command(message: types.Message):
    await message.reply("Our hymn:")
    await bot.send_voice(message.from_user.id, AUDIO)


@dp.message_handler(Text(equals=messages.video))
async def process_video_command(message: types.Message):
    await message.reply("The video:")
    await bot.send_video(message.from_user.id, VIDEO)


@dp.message_handler()
async def process_message(message: types.Message):
    await message.reply(f'\"{message.text}\" to you too, {message.from_user["first_name"]}!')


if __name__ == '__main__':
    executor.start_polling(dp)
