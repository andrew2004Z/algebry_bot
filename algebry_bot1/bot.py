import config
import logging
from aiogram import Bot, Dispatcher, executor, types
from sql import sqll
import sqlite3
from keyboards import *

logging.basicConfig(level=logging.INFO)

def new_user_in_game(user_id):
    if (not db.subscriber_exists(user_id)):
        db.add_user(user_id, col_quetions=1)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
db = sqll('database_game.db')



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        col_quetion = 1
        db.add_user(message.from_user.id, col_quetions=col_quetion)
        await message.answer('Вы успешно начали игру.')
        await message.answer(config.starts_text_message, reply_markup=inline_kb1)
    elif db.get_quetions(user_id=message.from_user.id) == 0:
        db.update_col_quetions(message.from_user.id, db.get_quetions(user_id=message.from_user.id) + 1)
        await message.answer('Вы успешно начали игру.')
        await message.answer(config.starts_text_message, reply_markup=inline_kb1)
    else:
        await message.answer('Вы уже начали игру, если вы хотите начать заново введите коменду "/reset".')

@dp.message_handler(commands=['plot'])
async def plot(message: types.Message):
    await message.answer(config.starts_text_message)

@dp.message_handler(commands=['reset'])
async def reset(message: types.Message):
    db.update_col_quetions(message.from_user.id, col_quetions=0)
    db.update_col_erorr(message.from_user.id, col_erorr=0)
    await message.answer('Вы начали игру заново.')

@dp.message_handler(lambda c: c.data == 'reset')
async def reset1(callback_query: types.CallbackQuery):
    db.update_col_quetions(callback_query.from_user.id, col_quetions=0)
    db.update_col_erorr(callback_query.from_user.id, col_erorr=0)
    await message.answer('Вы начали игру заново. Введите "/start"')

@dp.message_handler(commands=['help'])
async def helps(message: types.Message):
    await message.answer(config.helps_text_message)

@dp.callback_query_handler(lambda c: c.data == 'button1_start')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 1:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Ты приходишь на собеседование к Джорджу Булю в лабораторию, и он задает тебе несколько вопросов.', reply_markup=inline_kb2)
    elif db.get_quetions(callback_query.from_user.id) > 1:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 1:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'button2_start')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 2:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Первый вопрос.')
        await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)

@dp.callback_query_handler(lambda c: c.data == 'bt11_3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 3:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 3:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 3:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt11_5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 3:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Молодец, ты ответил правильно!')
        await bot.send_message(callback_query.from_user.id, 'Второй вопрос:')
        await bot.send_message(callback_query.from_user.id, config.n2, reply_markup=inline_kb4)
    elif db.get_quetions(callback_query.from_user.id) > 3:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 3:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt11_9')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 3:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 3:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 3:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt11_7')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 3:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 3:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 3:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt21_emeli')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 4:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 4:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 4:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt21_michail')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 4:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Молодец, ты ответил правильно!')
        await bot.send_message(callback_query.from_user.id, 'Третий вопрос:')
        #await bot.send_message(callback_query.from_user.id, config.n3, reply_markup=inline_kb5)
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/n3_photo.png', 'rb'), caption=str(config.n3), reply_markup=inline_kb5)
    elif db.get_quetions(callback_query.from_user.id) > 4:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 4:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt21_ivan')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 4:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 4:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 4:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt21_nicita')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 4:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 4:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 4:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt31_zxy')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 5:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 5:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 5:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt31_zyx')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 5:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 5:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 5:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt31_xyz')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 5:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 5:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 5:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt31_yzx')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 5:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Молодец, ты ответил правильно!')
        await bot.send_message(callback_query.from_user.id, 'Четвертый вопрос:')
        #await bot.send_message(callback_query.from_user.id, config.n4, reply_markup=inline_kb6)
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/n4_photo.png', 'rb'), caption=str(config.n4), reply_markup=inline_kb6)
    elif db.get_quetions(callback_query.from_user.id) > 5:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 5:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt41_xzy')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 6:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 6:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 6:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt41_zxy')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 6:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 6:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 6:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt41_yzx')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 6:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 6:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 6:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt41_zyx')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 6:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Молодец, ты ответил правильно!')
        await bot.send_message(callback_query.from_user.id, 'Последний вопрос:')
        await bot.send_message(callback_query.from_user.id, config.n5, reply_markup=inline_kb7)
        #await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/n4_photo.png', 'rb'), caption=str(config.n4), reply_markup=inline_kb6)
    elif db.get_quetions(callback_query.from_user.id) > 6:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 6:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt51_27')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 7:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 7:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 7:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt51_63')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 7:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 7:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 7:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt51_16')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 7:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 7:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 7:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt51_31')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 7:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        if db.get_erorr(callback_query.from_user.id) == 0:
            await bot.send_message(callback_query.from_user.id, f'Молодец, ты ответил правильно на все вопросы! И Джордж Буль взял тебя на работу.')
        elif db.get_erorr(callback_query.from_user.id) == 1:
            await bot.send_message(callback_query.from_user.id, f'Молодец, ты ответил правильно! Но за всё тестирование ты сделал {db.get_erorr(callback_query.from_user.id)} ошибку, но Джордж Буль взял тебя на испытательный срок.')
        elif db.get_erorr(callback_query.from_user.id) == 2:
            await bot.send_message(callback_query.from_user.id, f'Молодец, ты ответил правильно! Но за всё тестирование ты сделал {db.get_erorr(callback_query.from_user.id)} ошибки, но Джордж Буль взял тебя на испытательный срок.')
        elif db.get_erorr(callback_query.from_user.id) == 3:
            await bot.send_message(callback_query.from_user.id, f'Молодец, ты ответил правильно! Но за всё тестирование ты сделал {db.get_erorr(callback_query.from_user.id)} ошибки, но Джордж Буль взял тебя на испытательный срок.')
        elif db.get_erorr(callback_query.from_user.id) == 4:
            await bot.send_message(callback_query.from_user.id, f'Молодец, ты ответил правильно! Но за всё тестирование ты сделал {db.get_erorr(callback_query.from_user.id)} ошибки, но Джордж Буль взял тебя на испытательный срок.')
        elif db.get_erorr(callback_query.from_user.id) == 5:
            await bot.send_message(callback_query.from_user.id, f'Молодец, ты ответил правильно! Но за всё тестирование ты сделал {db.get_erorr(callback_query.from_user.id)} ошибок, но Джордж Буль взял тебя на испытательный срок.')
        else:
            await bot.send_message(callback_query.from_user.id, f'Молодец, ты ответил правильно! Но за всё тестирование ты сделал {db.get_erorr(callback_query.from_user.id)} ошибки/ошибок, но Джордж Буль взял тебя на испытательный срок.')
        #await bot.send_message(callback_query.from_user.id, 'Последний вопрос:')
        await bot.send_message(callback_query.from_user.id, config.otvet1, reply_markup=inline_kb8)
        #await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/n4_photo.png', 'rb'), caption=str(config.n4), reply_markup=inline_kb6)
    elif db.get_quetions(callback_query.from_user.id) > 7:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 7:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'btn_otvet')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 8:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        #await bot.send_message(callback_query.from_user.id, f'Молодец, ты ответил правильно! Но за всё тестирование ты сделал {db.get_erorr(callback_query.from_user.id)} ошибок, но Джордж Буль взял тебя на испытательный срок')
        await bot.send_message(callback_query.from_user.id, 'Вот это задание:')
        #await bot.send_message(callback_query.from_user.id, config.otvet1, reply_markup=inline_kb8)
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/n6_photo.png', 'rb'), caption=str(config.n6), reply_markup=inline_kb9)
    elif db.get_quetions(callback_query.from_user.id) > 8:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 8:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt61_wyxz')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 9:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 9:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 9:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt61_xwyz')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 9:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 9:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 9:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt61_zywx')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 9:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Неправильный ответ!')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 9:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 9:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt61_zyxw')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 9:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Молодец, правильный ответ ZYXW')
        await bot.send_message(callback_query.from_user.id, config.otvet2, reply_markup=inline_kb10)
        #await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/n4_photo.png', 'rb'), caption=str(config.n4), reply_markup=inline_kb6)
    elif db.get_quetions(callback_query.from_user.id) > 9:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 9:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'btn_otvet2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 10:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        #await bot.send_message(callback_query.from_user.id, 'Молодец, правильный ответ ZYXW')
        await bot.send_message(callback_query.from_user.id, config.otvet3, reply_markup=inline_kb11)
        #await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/n4_photo.png', 'rb'), caption=str(config.n4), reply_markup=inline_kb6)
    elif db.get_quetions(callback_query.from_user.id) > 10:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 10:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')


@dp.callback_query_handler(lambda c: c.data == 'bt74')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 11:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Мне кажется, лучше назвать по-другому.')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 11:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 11:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt72')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 11:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Мне кажется, лучше назвать по-другому.')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 11:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 11:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt73')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 11:
        #db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        db.update_col_erorr(callback_query.from_user.id, db.get_erorr(callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Мне кажется, лучше назвать по-другому.')
        #await bot.send_message(callback_query.from_user.id, config.n1, reply_markup=inline_kb3)
    elif db.get_quetions(callback_query.from_user.id) > 11:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 11:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt71')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 11:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Хорошо, я бы назвал точно также.')
        await bot.send_message(callback_query.from_user.id, config.otvet4)
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/10.jpg', 'rb'), reply_markup=inline_kb12)
    elif db.get_quetions(callback_query.from_user.id) > 11:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 11:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt71')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 11:
        db.update_col_quetions(callback_query.from_user.id, db.get_quetions(user_id=callback_query.from_user.id) + 1)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Хорошо, я бы назвал точно также.')
        await bot.send_message(callback_query.from_user.id, config.otvet4)
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/10.jpg', 'rb'), reply_markup=inline_kb12)
    elif db.get_quetions(callback_query.from_user.id) > 11:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 11:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')

@dp.callback_query_handler(lambda c: c.data == 'bt77')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if db.get_quetions(callback_query.from_user.id) == 12:
        db.update_col_quetions(callback_query.from_user.id, col_quetions=0)
        db.update_col_erorr(callback_query.from_user.id, col_erorr=0)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, 'Вы начали игру заново. Введите "/start".')
        #await bot.send_message(callback_query.from_user.id, config.otvet4)
        #await bot.send_photo(chat_id=callback_query.from_user.id, photo=open('data/10.jpg', 'rb'), reply_markup=inline_kb12)
    elif db.get_quetions(callback_query.from_user.id) > 12:
        await bot.send_message(callback_query.from_user.id, 'Этот шаг ты уже прошел.')
    elif db.get_quetions(callback_query.from_user.id) < 12:
        await bot.send_message(callback_query.from_user.id, 'До зтого шага ты ещё не дошёл.')


if __name__ == "__main__":
    executor.start_polling(dp)