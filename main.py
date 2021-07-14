import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('нулевая неделя')
    item2 = types.KeyboardButton('первая неделя')
    item3 = types.KeyboardButton('вторая неделя')
    item4 = types.KeyboardButton('третья неделя')
    item5 = types.KeyboardButton('четвёртая неделя')
    item6 = types.KeyboardButton('пятая неделя')
    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id,
                     'Привет, я создатель этого телеграм бота. Можешь звать меня Герой'.format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'нулевая неделя':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Введение Linux')
            item2 = types.KeyboardButton('Знакомство с инструментами')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Темы:', reply_markup=markup)

        elif message.text == 'первая неделя':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Hello Python')
            item2 = types.KeyboardButton('Условия')
            item3 = types.KeyboardButton('Строки Python')
            item4 = types.KeyboardButton('Циклы')
            item5 = types.KeyboardButton('Tuples and Lists')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, item3, item4, item5, back)

            bot.send_message(message.chat.id, 'первая неделя', reply_markup=markup)


        elif message.text == 'вторая неделя':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Словари и множества')
            item2 = types.KeyboardButton('Работа с файлами')
            item3 = types.KeyboardButton('Modules')
            item4 = types.KeyboardButton('Встроеные функции')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, 'вторая неделя', reply_markup=markup)


        elif message.text == 'третья неделя':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Функции часть 1')
            item2 = types.KeyboardButton('Функции часть 2')
            item3 = types.KeyboardButton('Функции часть 3')
            item4 = types.KeyboardButton('Classes')
            item5 = types.KeyboardButton('Classes 2')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, item3, item4, item5, back)

            bot.send_message(message.chat.id, 'третья неделя', reply_markup=markup)


        elif message.text == 'четвёртая неделя':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Базы Данных 1')
            item2 = types.KeyboardButton('Базы Данных 2')
            item3 = types.KeyboardButton('Базы Данных 3')
            item4 = types.KeyboardButton('Базы Данных 4')
            item5 = types.KeyboardButton('Базы Данных 5')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, item3, item4, item5, back)

            bot.send_message(message.chat.id, 'четвёртая неделя', reply_markup=markup)
        elif message.text == 'пятая неделя':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('JSON CRUD')
            item2 = types.KeyboardButton('HTTP протоколы')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'пятая неделя', reply_markup=markup)

        elif message.text == '⬅️ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('нулевая неделя')
            item2 = types.KeyboardButton('первая неделя')
            item3 = types.KeyboardButton('вторая неделя')
            item4 = types.KeyboardButton('третья неделя')
            item5 = types.KeyboardButton('четвёртая неделя')
            item6 = types.KeyboardButton('пятая неделя')
            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, 'главное меню', reply_markup=markup)
        #     ВОТ И ЛОГИКА ОТПРАВКИ ССЫЛОК ⬇️
        elif message.text == 'Введение Linux':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEJOpH_CxM/1UDX2PuUoAQgeBj3MXPFtw/edit')
        elif message.text == 'Знакомство с инструментами':
            bot.send_message(message.chat.id, 'https://drive.google.com/file/d/1-ja-7DcQELhZRG3eE3eVUlAiO-tde1pE/view')
        elif message.text == 'Hello Python':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEJVu8SdeE/RM3BbnB9ugFMdzdHwacTDw/edit')
        elif message.text == 'Условия':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEKL3xKe_w/ZVxnexfFiXcE0C8UFaaRUg/edit')
        elif message.text == 'Строки Python':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEJtybm4rE/puy_vAomu4xfpkIuoxiLPw/edit')
        elif message.text == 'Циклы':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEKLwi67Q0/7GrpPl-JkU-ChnUueFrALQ/edit')
        elif message.text == 'Tuples and Lists':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEKCfdDNlM/PfYLaUxrw1TZKLZuma2Kbg/edit')
        elif message.text == 'Словари и множества':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEKITn4cps/ePJaIqlSP1xkXx-Ursv-xw/edit')
        elif message.text == 'Работа с файлами':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAELncnAUd0/Y1HA4swte_Z0MsyQFumTLQ/edit')
        elif message.text == 'Modules':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEL3jdjjeE/D0J1bLigW9wnAx3BeH8x1Q/edit')
        elif message.text == 'Встроеные функции':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAELmM4ZppM/_25Qsdu2V8MSWHpajKUBRA/edit')
        elif message.text == 'Функции часть 1':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEL9aD6ZMA/ZtE3OBC0zpEqMZ9ZeqhTGw/edit')
        elif message.text == 'Функции часть 2':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEL957OyMI/bt_vqVr9T143MWpc9OGd5w/edit')
        elif message.text == 'Функции часть 3':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEMeGHbmzM/g8-haIvlYpoSdhLOrEZU9g/edit')
        elif message.text == 'Classes':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEMKEfSyG4/RPVZcAYFdyitMxd8vUMDmA/edit')
        elif message.text == 'Classes 2':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEMofMUm0o/iRIFYlFlSAF20STv1bxhGg/edit')
        elif message.text == 'Базы Данных 1':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAEM7aTvf6w/GYrj-xuF2x6z0pisVH7sdQ/edit')
        elif message.text == 'Базы Данных 2':
            bot.send_message(message.chat.id, 'https://www.canva.com/design/DAENAcLe7cM/F-kIMzPejRlt86AZDwDNpw/edit')
        elif message.text == 'Базы Данных 3':
            bot.send_message(message.chat.id, 'https://drive.google.com/file/d/1CGgv1oNxv82kyqNNNj4WrgR6n3iqic9c/view')
        elif message.text == 'Базы Данных 4':
            bot.send_message(message.chat.id, 'https://drive.google.com/file/d/1uF6kAuu6ehADLYnst_QdM2Oy4nViC-l-/view')
        elif message.text == 'Базы Данных 5':
            bot.send_message(message.chat.id, 'https://drive.google.com/file/d/1t8cB4UGoKmdtmLUSW_7HKTXeKE4Z_27H/view')
        elif message.text == 'JSON CRUD':
            bot.send_message(message.chat.id, 'https://drive.google.com/file/d/1hjtbkZ7g17nlfq4jti8UPVNOtv_s7pGE/view')
        elif message.text == 'HTTP протоколы':
            bot.send_message(message.chat.id, 'https://drive.google.com/file/d/1n1fuKXWQLALN7-wBbaZCCXWVVLTiX4Dh/view')


bot.polling(none_stop=True)