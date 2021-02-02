import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from sql import sqll
import sqlite3
from keyboards import *


inline_kb1 = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Я готов взяться за это дело!', callback_data='button1_start'))
inline_kb2 = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('Я согласен пройти тестирование.', callback_data='button2_start'))
inline_b11 = types.InlineKeyboardButton('3', callback_data='bt11_3')
inline_b12 = types.InlineKeyboardButton('5', callback_data='bt11_5')
inline_b13 = types.InlineKeyboardButton('9', callback_data='bt11_9')
inline_b14 = types.InlineKeyboardButton('7', callback_data='bt11_7')
inline_kb3 = types.InlineKeyboardMarkup().add(inline_b11, inline_b12)
inline_kb3.add(inline_b13, inline_b14)

inline_b21 = types.InlineKeyboardButton('Емеля', callback_data='bt21_emeli')
inline_b22 = types.InlineKeyboardButton('Иван', callback_data='bt21_ivan')
inline_b23 = types.InlineKeyboardButton('Михаил', callback_data='bt21_michail')
inline_b24 = types.InlineKeyboardButton('Никита', callback_data='bt21_nicita')
inline_kb4 = types.InlineKeyboardMarkup().add(inline_b21, inline_b22)
inline_kb4.add(inline_b23, inline_b24)

inline_b31 = types.InlineKeyboardButton('ZXY', callback_data='bt31_zxy')
inline_b32 = types.InlineKeyboardButton('YZX', callback_data='bt31_yzx')
inline_b33 = types.InlineKeyboardButton('ZYX', callback_data='bt31_zyx')
inline_b34 = types.InlineKeyboardButton('XYZ', callback_data='bt31_xyz')
inline_kb5 = types.InlineKeyboardMarkup().add(inline_b31, inline_b32)
inline_kb5.add(inline_b33, inline_b34)

inline_b41 = types.InlineKeyboardButton('YZX', callback_data='bt41_yzx')
inline_b42 = types.InlineKeyboardButton('ZXY', callback_data='bt41_zxy')
inline_b43 = types.InlineKeyboardButton('XZY', callback_data='bt41_xzy')
inline_b44 = types.InlineKeyboardButton('ZYX', callback_data='bt41_zyx')
inline_kb6 = types.InlineKeyboardMarkup().add(inline_b41, inline_b42)
inline_kb6.add(inline_b43, inline_b44)

inline_b51 = types.InlineKeyboardButton('31', callback_data='bt51_31')
inline_b52 = types.InlineKeyboardButton('16', callback_data='bt51_16')
inline_b53 = types.InlineKeyboardButton('27', callback_data='bt51_27')
inline_b54 = types.InlineKeyboardButton('63', callback_data='bt51_63')
inline_kb7 = types.InlineKeyboardMarkup().add(inline_b51, inline_b52)
inline_kb7.add(inline_b53, inline_b54)

inline_b6 = types.InlineKeyboardButton('Я готов решить это задание!', callback_data='btn_otvet')
inline_kb8 = types.InlineKeyboardMarkup().add(inline_b6)

inline_b61 = types.InlineKeyboardButton('WYXZ', callback_data='bt61_wyxz')
inline_b62 = types.InlineKeyboardButton('ZYXW', callback_data='bt61_zyxw')
inline_b63 = types.InlineKeyboardButton('XWYZ', callback_data='bt61_xwyz')
inline_b64 = types.InlineKeyboardButton('ZYWX', callback_data='bt61_zywx')
inline_kb9 = types.InlineKeyboardMarkup().add(inline_b61, inline_b62)
inline_kb9.add(inline_b63, inline_b64)

inline_b7 = types.InlineKeyboardButton('Хорошо, пароль от сейфа 5197.', callback_data='btn_otvet2')
inline_kb10 = types.InlineKeyboardMarkup().add(inline_b7)


inline_b73 = types.InlineKeyboardButton('Конъюнкция', callback_data='bt71')
inline_b72 = types.InlineKeyboardButton('Дизъюнкция', callback_data='bt72')
inline_b71 = types.InlineKeyboardButton('XOR', callback_data='bt73')
inline_b74 = types.InlineKeyboardButton('Инверсия', callback_data='bt74')
inline_kb11 = types.InlineKeyboardMarkup().add(inline_b71, inline_b72)
inline_kb11.add(inline_b73, inline_b74)

inline_b77 = types.InlineKeyboardButton('Начать игру заново.', callback_data='bt77')
inline_kb12 = types.InlineKeyboardMarkup().add(inline_b77)