from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import messages

inline_address = InlineKeyboardButton('Адрес', callback_data='address')
inline_about_us = InlineKeyboardButton('О нас', callback_data='about_us')
inline_contacts = InlineKeyboardButton('Контакты', callback_data='contacts')
inline_site = InlineKeyboardButton('Наш сайт', url='mdprojecttg.ru')

inline_kb_info = InlineKeyboardMarkup(row_width=3).add(inline_about_us).add(inline_site).add(inline_address).add(
    inline_contacts)


button_song = KeyboardButton(messages.song)
button_photo = KeyboardButton(messages.photo)
button_video = KeyboardButton(messages.video)

media_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    button_photo, button_song, button_video
)
