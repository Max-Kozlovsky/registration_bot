from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.executor import start_webhook
import os
import logging
from config import token
from keyboards import choice_project, url_aviso, url_seofast, url_profitcentr, url_seotime, url_wmrfast, url_info, \
    cell_aviso, cell_seofast, cell_profitcentr, cell_seotime, cell_wmrfast

TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()
"""-----------------------------------------------Storage------------------------------------------------------------"""


class BackCall(StatesGroup):
    Q1 = State()  # для вопросов пользователей
    A1 = State()  # отправка ников Aviso
    SF = State()  # отправка ников Seofast
    P1 = State()  # отправка ников Profitcentr
    ST = State()  # отправка ников Seotime
    W1 = State()  # отправка ников Wmrfast
    A2 = State()  # запрос покупки Aviso
    SF2 = State()  # запрос покупки Seofast
    P2 = State()  # запрос покупки Profitcentr
    ST2 = State()  # запрос покупки Seotime
    W2 = State()  # запрос покупки Wmrfast


"""----------------------------------------Приветствие и информация--------------------------------------------------"""


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMDYkH4NfcYYEHuwA8h72aHPhlYUV8AAiQAA9Qs5g4Fi06wgZHmjCME')
    await bot.send_message(message.chat.id,
                           'Приветствую тебя. Ко мне приходят те, кто хочет зарабатывать в интернете больше'
                           ' и эффективнее. Я могу предложить тебе программы, которые помогут тебе работать'
                           ' эффективно на сервисах активной рекламы или проще говоря - буксах.\n'
                           ' Если ты согласен вступить в мою команду (зарегистрироваться по ссылке), я дам тебе '
                           'ботов БЕСПЛАТНО, просто следуй моим инструкциям.\n'
                           'Если же ты не можешь/не хочешь присоединиться к нам, можешь купить бота для себя.\n\n'
                           ' Программа для какого проекта тебе нужна?', reply_markup=choice_project)


@dp.callback_query_handler(text_contains='info')
async def about_bots(call: types.CallbackQuery):
    await bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAOdYkNjUCFHrneff7ecQWkRA90E9twAAicAA9Qs5g52RVQ85vusbyME')
    await bot.send_message(call.message.chat.id, 'Боты работают на компьютерах с Windows 10 в браузерах Google Chrome.'
                                                 ' Работа проходит в активном окне, имитируя действия человека для того'
                                                 ' чтоб рекламодатели могли получить заветные посещения и просмотры. От'
                                                 ' тебя требуется лишь запускать программу и при необходимости вводить '
                                                 'капчу каждый час, показывая, что ты не бот. Я подготовил видео '
                                                 'инструкцию по каждой программе. Если после просмотра останутся '
                                                 'вопросы, нажми "Есть вопрос" и напиши свой вопрос. Я проанализирую '
                                                 'его и пришлю ответ. Помни: Никогда не упускай случая испытать нечто '
                                                 'новое. Это расширяет твои возможности.', reply_markup=url_info)


"""---------------------------------Обработка вопросов от пользователей----------------------------------------------"""


@dp.callback_query_handler(text_contains='question', state=None)
async def question(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Задавай вопрос")
    await BackCall.Q1.set()


@dp.message_handler(state=BackCall.Q1)
async def send_question(message: types.Message, state: FSMContext):
    await bot.send_message(770675831, f"{message.chat.id}({message.chat.username}): {message.text}")
    await state.finish()
    await bot.send_message(message.chat.id, 'Вопрос отправлен. Ожидайте ответ', reply_markup=choice_project)


"""----------------------------------------Презентация ботов---------------------------------------------------------"""


@dp.callback_query_handler(text_contains="aviso")
async def aviso(call: types.CallbackQuery):
    await bot.send_sticker(call.message.chat.id,
                           'CAACAgIAAxkBAAMaYkH8uifBa6MFBAWOFaZ5jZ9D_5YAAi0AA9Qs5g6RUHPFB5a5UyME')
    await bot.send_message(call.message.chat.id, 'Хороший выбор. Программа для работы в AVISO умеет смотреть серфинг,'
                                                 ' отлично справляется с просмотром видео на Youtube. Это даст тебе'
                                                 ' неплохой дополнительный доход. Для того чтоб получить программу, '
                                                 'нажми кнопку "Регистрация" и зарегистрируйся на сайте',
                           reply_markup=url_aviso)


@dp.callback_query_handler(text_contains="seofast")
async def seofast(call: types.CallbackQuery):
    await bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAMaYkH8uifBa6MFBAWOFaZ5jZ9D_5YAAi0AA9Qs5g6RUHPFB5a5UyME')
    await bot.send_message(call.message.chat.id, 'Хороший выбор. Программа для работы в Seofast сама смотрит серфинг,'
                                                 ' отлично справляется с просмотром видео на Youtube (обрати внимание'
                                                 ' на бонусы от проекта за просмотр видео). Это даст тебе неплохой '
                                                 'дополнительный доход. Для того чтоб получить программу, нажми кнопку '
                                                 '"Регистрация" и зарегистрируйся на сайте', reply_markup=url_seofast)


@dp.callback_query_handler(text_contains='profitcentr')
async def profitcentr(call: types.CallbackQuery):
    await bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAMaYkH8uifBa6MFBAWOFaZ5jZ9D_5YAAi0AA9Qs5g6RUHPFB5a5UyME')
    await bot.send_message(call.message.chat.id, 'Хорошо. Бот для Profitcentr смотрит серфинг и посещения,'
                                                 ' отлично справляется с просмотром видео на Youtube (обрати внимание'
                                                 ' на бонусы от проекта за просмотр видео). Это даст тебе неплохой '
                                                 'дополнительный доход. Для того чтоб получить бота, нажми кнопку '
                                                 '"Регистрация" и зарегистрируйся на сайте',
                           reply_markup=url_profitcentr)


@dp.callback_query_handler(text_contains='seotime')
async def seotime(call: types.CallbackQuery):
    await bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAMaYkH8uifBa6MFBAWOFaZ5jZ9D_5YAAi0AA9Qs5g6RUHPFB5a5UyME')
    await bot.send_message(call.message.chat.id, 'Хорошо. Бот для Seotime смотрит серфинг, отлично справляется с '
                                                 'просмотром видео на Youtube (обрати внимание на бонусы от проекта за '
                                                 'просмотр видео). Это даст тебе неплохой дополнительный доход. Для '
                                                 'того чтоб получить бота, нажми кнопку "Регистрация" и зарегистрируйся'
                                                 ' на сайте', reply_markup=url_seotime)


@dp.callback_query_handler(text_contains='wmrfast')
async def wmrfast(call: types.CallbackQuery):
    await bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAMaYkH8uifBa6MFBAWOFaZ5jZ9D_5YAAi0AA9Qs5g6RUHPFB5a5UyME')
    await bot.send_message(call.message.chat.id, 'Внимание!!! Бот работает с браузером Mozilla Firefox.\n '
                                                 'Бот для Wmrfast умеет смотреть посещения, смотрит Youtube и '
                                                 'сам собирает бонус каждый час. Это даст тебе неплохой дополнительный '
                                                 'доход. Для того чтоб получить бота, нажми кнопку "Регистрация" и '
                                                 'зарегистрируйся на сайте', reply_markup=url_wmrfast)


"""-----------------------------------------Описание ботов-----------------------------------------------------------"""


@dp.callback_query_handler(text_contains='aboutAviso')
async def about_aviso(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Параметры бота Aviso:\n'
                                                 'Умения: серфинг, просмотр Youtube\n'
                                                 'Среднее время автономной работы: 5 часов и больше\n'
                                                 'Необходимость участия пользователя: отсутствует\n'
                                                 'Наличие ручной капчи: очень редко\n'
                                                 'Видео обзор: https://www.youtube.com/watch?v=dcZ8-J7ACn8',
                           reply_markup=choice_project)


@dp.callback_query_handler(text_contains='aboutSeofast')
async def about_seofast(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Параметры бота Seofast:\n'
                                                 'Умения: серфинг, просмотр Youtube (не забывай забирать бонус)\n'
                                                 'Среднее время автономной работы: 1 час\n'
                                                 'Необходимость участия пользователя: да (на входе и перед первым '
                                                 'действием)\n'
                                                 'Наличие ручной капчи: каждый час\n'
                                                 'Видео обзор: https://www.youtube.com/watch?v=L5b8abcE8lI',
                           reply_markup=choice_project)


@dp.callback_query_handler(text_contains='aboutProfitcentr')
async def about_profitcentr(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Параметры бота Profitcentr:\n'
                                                 'Умения: серфинг, посещения, просмотр Youtube (не забывай забирать '
                                                 'бонус)\n'
                                                 'Среднее время автономной работы: 30-40 минут\n'
                                                 'Необходимость участия пользователя: да (на входе и перед первым '
                                                 'действием)\n'
                                                 'Наличие ручной капчи: каждые 30-40 минут',
                           reply_markup=choice_project)


@dp.callback_query_handler(text_contains='aboutSeotime')
async def about_seotime(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Параметры бота Seotime:\n'
                                                 'Умения: серфинг, просмотр Youtube (не забывай забирать бонус)\n'
                                                 'Среднее время автономной работы: 5 часов и больше\n'
                                                 'Необходимость участия пользователя: да (на входе)\n'
                                                 'Наличие ручной капчи: нет', reply_markup=choice_project)


@dp.callback_query_handler(text_contains='aboutWmrfast')
async def about_wmrfast(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, 'Параметры бота Wmrfast:\n'
                                                 'Умения: посещения, просмотр Youtube, сбор бонуса каждый час\n'
                                                 'Среднее время автономной работы: 5 часов и больше\n'
                                                 'Необходимость участия пользователя: да (на входе)\n'
                                                 'Наличие ручной капчи: нет', reply_markup=choice_project)


"""--------------------------------------Подтверждение регистрации---------------------------------------------------"""


@dp.callback_query_handler(text_contains='alreadyAviso', state=None)
async def aviso_reg(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Уже прошел регистрацию Aviso? Напиши мне ник, под которым ты "
                                                 "зарегистрировался на проекте.\n Я проверю, по какой ссылке"
                                                 " ты регистрировался. Если все хорошо, то в течении 24 часов для тебя "
                                                 "соберут бота и пришлют его тебе вместе с инструкцией")
    await BackCall.A1.set()


@dp.message_handler(state=BackCall.A1)
async def send_login_aviso(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Регистрация в Aviso. {message.chat.id}({message.chat.username}): '
                                            f'{message.text}')
    await state.finish()
    await bot.send_message(message.chat.id, 'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                                            'постараюсь не затаягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


@dp.callback_query_handler(text_contains='alreadySeofast', state=None)
async def seofast_reg(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Уже прошел регистрацию Seofast? Напиши мне электронную почту и ник, "
                                                 "под которым ты зарегистрировался на проекте.\n Я проверю, по какой "
                                                 "ссылке ты регистрировался. Если все хорошо, то в течении 24 часов для"
                                                 " тебя соберут бота и пришлют его тебе вместе с инструкцией")
    await BackCall.SF.set()


@dp.message_handler(state=BackCall.SF)
async def send_login_seofast(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Регистрация в Seofast. Ник: {message.chat.id}({message.chat.username}): '
                                            f'{message.text}')
    await state.finish()
    await bot.send_message(message.chat.id, 'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                                            'постараюсь не затаягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


@dp.callback_query_handler(text_contains='alreadyProfitcentr', state=None)
async def profitcentr_reg(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Уже прошел регистрацию Profitcentr? Напиши мне "
                                                 "ник, под которым ты зарегистрировался на проекте.\n Я проверю, по "
                                                 "какой ссылке ты регистрировался. Если все хорошо, то в течении 24 "
                                                 "часов для тебя соберут бота и пришлют его тебе вместе с инструкцией")
    await BackCall.P1.set()


@dp.message_handler(state=BackCall.P1)
async def send_login_profitcentr(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Регистрация в Profitcentr. Ник: {message.chat.id}({message.chat.username}'
                                            f'): {message.text}')
    await state.finish()
    await bot.send_message(message.chat.id, 'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                                            'постараюсь не затаягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


@dp.callback_query_handler(text_contains='alreadySeotime', state=None)
async def seotime_reg(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Уже прошел регистрацию Seotime? Напиши мне "
                                                 "ник, под которым ты зарегистрировался на проекте.\n Я проверю, по "
                                                 "какой ссылке ты регистрировался. Если все хорошо, то в течении 24 "
                                                 "часов для тебя соберут бота и пришлют его тебе вместе с инструкцией")
    await BackCall.ST.set()


@dp.message_handler(state=BackCall.ST)
async def send_login_seotime(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Регистрация в Seotime. Ник: {message.chat.id}({message.chat.username}): '
                                            f'{message.text}')
    await state.finish()
    await bot.send_message(message.chat.id, 'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                                            'постараюсь не затаягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


@dp.callback_query_handler(text_contains='alreadyWmrfast', state=None)
async def wmrfast_reg(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Уже прошел регистрацию WmrFast? Напиши мне "
                                                 "ник, под которым ты зарегистрировался на проекте.\n Я проверю, по "
                                                 "какой ссылке ты регистрировался. Если все хорошо, то в течении 24 "
                                                 "часов для тебя соберут бота и пришлют его тебе вместе с инструкцией")
    await BackCall.W1.set()


@dp.message_handler(state=BackCall.W1)
async def send_login_wmrfast(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Регистрация в WmrFast. Ник: {message.chat.id}({message.chat.username}): '
                                            f'{message.text}')
    await state.finish()
    await bot.send_message(message.chat.id, 'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                                            'постараюсь не затаягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


"""-----------------------------------------Покупка бота-------------------------------------------------------------"""


# Aviso
@dp.callback_query_handler(text_contains='buy_process_1')
async def buy_aviso(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Задумался о покупке бота Aviso? Это правильное решение.\nНа всякий "
                                                 "случай дам тебе совет. Если сомневаешься в боте, зарегистрируй "
                                                 "отдельный аккаунт по ссылке выше и протестируй бота. (только следи, "
                                                 "чтоб с одного IP два аккаунта одновременно не были запущены) Если "
                                                 "тебя все устроит, можешь смело покупать бота для основного аккаунта."
                                                 "\n\nБот Aviso стоит 200 рублей. ", reply_markup=cell_aviso)


@dp.callback_query_handler(text_contains="cell_1", state=None)
async def start_buying_aviso(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Напиши мне логин в проекте и я создам"
                                                 " заказ. Когда заказ будет готов, тебе сообщат об этом. После этого ты"
                                                 " перечислишь сумму на Payeer или Юmoney по своему выбору и тебе "
                                                 "пришлют бота в телеграм. Так же тебе назначат куратора и добавят в "
                                                 "группу, чтоб ты знал обо всех изменениях в работе бота")
    await BackCall.A2.set()


@dp.message_handler(state=BackCall.A2)
async def send_login_aviso(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Покупка бота Aviso. Ник: {message.chat.id}({message.chat.username}): '
                                            f'{message.text}')
    await state.finish()
    await bot.send_message(message.chat.id,
                           'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                           'постараюсь не затягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


# Seofast
@dp.callback_query_handler(text_contains='buy_process_2')
async def buy_seofast(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Задумался о покупке бота Seofast? Это правильное решение.\nНа всякий "
                                                 "случай дам тебе совет. Если сомневаешься в боте, зарегистрируй "
                                                 "отдельный аккаунт по ссылке выше и протестируй бота. (только следи, "
                                                 "чтоб с одного IP два аккаунта одновременно не были запущены) Если "
                                                 "тебя все устроит, можешь смело покупать бота для основного аккаунта."
                                                 "\n\nБот Seofast стоит 100 рублей. ", reply_markup=cell_seofast)


@dp.callback_query_handler(text_contains="cell_2", state=None)
async def start_buying_seofast(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Напиши мне логин и электронную почту в проекте и я создам"
                                                 " заказ. Когда заказ будет готов, тебе сообщат об этом. После этого ты"
                                                 " перечислишь сумму на Payeer или Юmoney по своему выбору и тебе "
                                                 "пришлют бота в телеграм. Так же тебе назначат куратора и добавят в "
                                                 "группу, чтоб ты знал обо всех изменениях в работе бота")
    await BackCall.SF2.set()


@dp.message_handler(state=BackCall.SF2)
async def send_login_seofast(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Покупка бота Seofast. {message.chat.id}({message.chat.username}) Ник: '
                                            f'{message.text}')
    await state.finish()
    await bot.send_message(message.chat.id,
                           'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                           'постараюсь не затягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


# Profitcentr
@dp.callback_query_handler(text_contains='buy_process_3')
async def buy_profitcentr(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Задумался о покупке бота Profitcentr? Это правильное решение.\nНа "
                                                 "всякий случай дам тебе совет. Если сомневаешься в боте, зарегистрируй"
                                                 " отдельный аккаунт по ссылке выше и протестируй бота. (только следи, "
                                                 "чтоб с одного IP два аккаунта одновременно не были запущены) Если "
                                                 "тебя все устроит, можешь смело покупать бота для основного аккаунта."
                                                 "\n\nБот Profitcentr стоит 100 рублей. ",
                           reply_markup=cell_profitcentr)


@dp.callback_query_handler(text_contains="cell_3", state=None)
async def start_buying_profitcentr(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Напиши мне логин в проекте и я создам"
                                                 " заказ. Когда заказ будет готов, тебе сообщат об этом. После этого ты"
                                                 " перечислишь сумму на Payeer или Юmoney по своему выбору и тебе "
                                                 "пришлют бота в телеграм. Так же тебе назначат куратора и добавят в "
                                                 "группу, чтоб ты знал обо всех изменениях в работе бота")
    await BackCall.P2.set()


@dp.message_handler(state=BackCall.P2)
async def send_login_profitcentr(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Покупка бота Profitcentr. {message.chat.id}({message.chat.username}) Ник:'
                                            f' {message.text}')
    await state.finish()
    await bot.send_message(message.chat.id,
                           'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                           'постараюсь не затягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


# Seotime
@dp.callback_query_handler(text_contains='buy_process_4')
async def buy_seotime(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Задумался о покупке бота Seotime? Это правильное решение.\nНа "
                                                 "всякий случай дам тебе совет. Если сомневаешься в боте, зарегистрируй"
                                                 " отдельный аккаунт по ссылке выше и протестируй бота. (только следи, "
                                                 "чтоб с одного IP два аккаунта одновременно не были запущены) Если "
                                                 "тебя все устроит, можешь смело покупать бота для основного аккаунта."
                                                 "\n\nБот Seotime стоит 100 рублей. ", reply_markup=cell_seotime)


@dp.callback_query_handler(text_contains="cell_4", state=None)
async def start_buying_seotime(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Напиши мне логин в проекте и я создам"
                                                 " заказ. Когда заказ будет готов, тебе сообщат об этом. После этого ты"
                                                 " перечислишь сумму на Payeer или Юmoney по своему выбору и тебе "
                                                 "пришлют бота в телеграм. Так же тебе назначат куратора и добавят в "
                                                 "группу, чтоб ты знал обо всех изменениях в работе бота")
    await BackCall.ST2.set()


@dp.message_handler(state=BackCall.ST2)
async def send_login_seotime(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Покупка бота Seotime. {message.chat.id}({message.chat.username}) Ник:'
                                            f' {message.text}')
    await state.finish()
    await bot.send_message(message.chat.id,
                           'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                           'постараюсь не затягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


# Wmrfast
@dp.callback_query_handler(text_contains='buy_process_5')
async def buy_wmrfast(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Задумался о покупке бота Wmrfast? Это правильное решение.\nНа "
                                                 "всякий случай дам тебе совет. Если сомневаешься в боте, зарегистрируй"
                                                 " отдельный аккаунт по ссылке выше и протестируй бота. (только следи, "
                                                 "чтоб с одного IP два аккаунта одновременно не были запущены) Если "
                                                 "тебя все устроит, можешь смело покупать бота для основного аккаунта."
                                                 "\n\nБот Wmrfast стоит 100 рублей. ", reply_markup=cell_wmrfast)


@dp.callback_query_handler(text_contains="cell_5", state=None)
async def start_buying_wmrfast(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Напиши мне логин в проекте и я создам"
                                                 " заказ. Когда заказ будет готов, тебе сообщат об этом. После этого ты"
                                                 " перечислишь сумму на Payeer или Юmoney по своему выбору и тебе "
                                                 "пришлют бота в телеграм. Так же тебе назначат куратора и добавят в "
                                                 "группу, чтоб ты знал обо всех изменениях в работе бота")
    await BackCall.W2.set()


@dp.message_handler(state=BackCall.W2)
async def send_login_wmrfast(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, f'Покупка бота Wmrfast. {message.chat.id}({message.chat.username}) Ник:'
                                            f' {message.text}')
    await state.finish()
    await bot.send_message(message.chat.id,
                           'Данные получил, начинаю проверку. Ответ будет в течении 24 часов. Но я '
                           'постараюсь не затягивать\n Хочешь заказать еще одного бота?',
                           reply_markup=choice_project)


"""-----------------------------------------Запуск программы---------------------------------------------------------"""
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=False,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
