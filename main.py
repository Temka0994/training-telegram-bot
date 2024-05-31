import telebot
from telebot import types
from telebot.types import InlineKeyboardButton
from complex_dao import *
from complex_progress_caching import *
from exercise_dao import *
from connection_manager import *
from exercise_list_message_context import *
from complex_progress import *
from exercise_message_context import *
from history_dao import *
from history_list_message_context import *
import datetime

bot = telebot.TeleBot('7152882771:AAEnSjTbLH_AU-8VHp0KHtqLg7uPpd7HHhI')
connection_manager = ConnectionManager()
exercise_dao = ExerciseDao(connection_manager)
complex_dao = ComplexDao(connection_manager)
history_dao = HistoryDao(connection_manager)
complex_dict = {'Ноги': 1, 'Руки': 5, 'Плечі': 2, 'Прес': 4, 'Спина': 3}
cache = ComplexProgressCache()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Продуктивного дня та вдалого тренування!')
    cache.remove_by(message.from_user.id)
    complex_buttons(message)


def complex_buttons(message):
    legs_button = types.KeyboardButton('Ноги')
    hands_button = types.KeyboardButton('Руки')
    shoulders_button = types.KeyboardButton('Плечі')
    back_button = types.KeyboardButton('Спина')
    press_button = types.KeyboardButton('Прес')
    markup = types.ReplyKeyboardMarkup()
    markup.add(legs_button, hands_button, shoulders_button, back_button, press_button)
    bot.send_message(message.from_user.id, 'Оберіть зі списку комплекс:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def choose_complex(message):
    if message.text in complex_dict.keys():
        bot.send_message(message.from_user.id, f'Тож ви обрали комплекс "{message.text}".')
        exercise_tuple = complex_dao.find_all_exercise_by_id(complex_dict[message.text])
        exercise_list_message_context = ExerciseListMessageContext(exercise_tuple)
        bot.send_message(message.from_user.id, exercise_list_message_context.description)
        bot.send_message(message.from_user.id, 'Давайте перейдемо до його виконання.')
        complex_progress_list = complex_dao.find_exercise_ids_by_id(complex_dict[message.text])
        complex_progress = ComplexProgres(complex_progress_list, complex_dict[message.text])
        cache.add(message.from_user.id, complex_progress)
        implementation_of_the_complex(message)
    else:
        bot.send_message(message.from_user.id, 'Незрозумів вас. Спробуйте ще раз!')


def implementation_of_the_complex(message):
    markup = types.InlineKeyboardMarkup()
    start_button = InlineKeyboardButton('Почати', callback_data="start")
    back_button = InlineKeyboardButton('Повернутися назад', callback_data="back")
    markup.add(start_button, back_button)
    bot.send_message(message.chat.id, "Це ваш остаточний вибір?", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['start', 'back'])
def handle_callback(call):
    if call.data == "start":
        exercise_done(call)
    elif call.data == "back":
        complex_buttons(call)


def exercise_done(call):
    try:
        comprog = cache.get_by(call.from_user.id)
        if comprog.current_exercise():
            markup = types.InlineKeyboardMarkup()
            done_button = InlineKeyboardButton('Виконано', callback_data="done")
            skip_button = InlineKeyboardButton('Пропустити', callback_data="skip")
            markup.add(done_button, skip_button)
            message_content = exercise_dao.find_by_id(comprog.current_exercise())
            message_context = MessageContext(message_content[0])
            bot.send_photo(call.from_user.id, message_context.url, message_context.description, reply_markup=markup)
        else:
            cache.remove_by(call.from_user.id)
    except IndexError:
        history_dao.save(call.from_user.id, cache.get_by(call.from_user.id).get_complex_id(), datetime.date.today())
        bot.send_message(call.from_user.id, "Виконання комплексу закінчено. Гарного відпочинку!")
        history_and_back_buttons(call)


@bot.callback_query_handler(func=lambda call: call.data in ['done', 'skip'])
def handle_callback(call):
    if call.data == 'done':
        cache.get_by(call.from_user.id).complete_current_exercise()
        exercise_done(call)
    elif call.data == 'skip':
        exercise_skip(call)


def exercise_skip(call):
    comprog = cache.get_by(call.from_user.id)
    if comprog.skip_current_exercise():
        exercise_done(call)


@bot.message_handler(content_types=['text'])
def history_and_back_buttons(call):
    markup = types.InlineKeyboardMarkup()
    history_button = InlineKeyboardButton('Історія', callback_data="history")
    back_button = InlineKeyboardButton('На початок', callback_data="back")
    markup.add(history_button, back_button)
    bot.send_message(call.from_user.id,
                     'Ви можете вивести історію своїх тренувань, або ж повернутися до вибору комплексу.',
                     reply_markup=markup)
    choosing_next_step(call)


@bot.callback_query_handler(func=lambda call: call.data in ['history', 'back'])
def choosing_next_step(call):
    if call.data == 'history':
        history_list = HistoryListMessageContext(history_dao.find_by_id(call.from_user.id), complex_dict)
        bot.send_message(call.from_user.id, history_list.description)
    elif call.data == 'back':
        complex_buttons(call)


bot.infinity_polling()
