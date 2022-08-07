from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# выбор проекта
choice_project = InlineKeyboardMarkup(row_width=2)
aviso_button = InlineKeyboardButton(text='Aviso', callback_data='aviso')
seofast_button = InlineKeyboardButton(text='Seo-fast', callback_data='seofast')
profitcentr_button = InlineKeyboardButton(text='Profitcentr', callback_data='profitcentr')
seotime_button = InlineKeyboardButton(text='Seotime', callback_data='seotime')
wmrfast_button = InlineKeyboardButton(text='WmrFast', callback_data='wmrfast')
inform_button = InlineKeyboardButton(text='Лучше расскажи, как работают твои боты', callback_data='info')
choice_project.add(aviso_button, seofast_button, profitcentr_button, seotime_button, wmrfast_button)
choice_project.add(inform_button)

# кнопки вопроса
url_info = InlineKeyboardMarkup()
url_info.add(InlineKeyboardButton(text="У меня есть вопрос", callback_data='question'))

# проект aviso
url_aviso = InlineKeyboardMarkup(row_width=2)
url_aviso_reg = InlineKeyboardButton(text='Регистрация', url='https://aviso.bz/?r=jion777')
url_aviso_buy = InlineKeyboardButton(text='Я хочу купить бота', callback_data='buy_process_1')
url_aviso_info = InlineKeyboardButton(text='Подробнее о боте Aviso', callback_data='aboutAviso')
url_aviso_already = InlineKeyboardButton(text='Я прошел регистрацию', callback_data='alreadyAviso')
url_aviso.add(url_aviso_reg, url_aviso_info, url_aviso_already, url_aviso_buy)

# проект seofast
url_seofast = InlineKeyboardMarkup(row_width=2)
url_seofast_reg = InlineKeyboardButton(text='Регистрация', url='https://seo-fast.ru/?r=2491464')
url_seofast_buy = InlineKeyboardButton(text='Я хочу купить бота', callback_data='buy_process_2')
url_seofast_info = InlineKeyboardButton(text='Подробнее о боте SeoFast', callback_data='aboutSeofast')
url_seofast_already = InlineKeyboardButton(text='Я прошел регистрацию', callback_data='alreadySeofast')
url_seofast.add(url_seofast_reg, url_seofast_info, url_seofast_already, url_seofast_buy)

# проект profitcentr
url_profitcentr = InlineKeyboardMarkup(row_width=2)
url_profitcentr_reg = InlineKeyboardButton(text='Регистрация', url='https://profitcentr.com/?r=jion')
url_profitcentr_buy = InlineKeyboardButton(text='Я хочу купить бота', callback_data='buy_process_3')
url_profitcentr_info = InlineKeyboardButton(text='Подробнее о боте Profitcentr', callback_data='aboutProfitcentr')
url_profitcentr_already = InlineKeyboardButton(text='Я прошел регистрацию', callback_data='alreadyProfitcentr')
url_profitcentr.add(url_profitcentr_reg, url_profitcentr_info, url_profitcentr_already, url_profitcentr_buy)

# проект seotime
url_seotime = InlineKeyboardMarkup(row_width=2)
url_seotime_reg = InlineKeyboardButton(text='Регистрация', url='https://seotime.biz/?r=jion')
url_seotime_buy = InlineKeyboardButton(text='Я хочу купить бота', callback_data='buy_process_4')
url_seotime_info = InlineKeyboardButton(text='Подробнее о боте Seotime', callback_data='aboutSeotime')
url_seotime_already = InlineKeyboardButton(text='Я прошел регистрацию', callback_data='alreadySeotime')
url_seotime.add(url_seotime_reg, url_seotime_info, url_seotime_already, url_seotime_buy)

# проект wmrfast
url_wmrfast = InlineKeyboardMarkup(row_width=2)
url_wmrfast_reg = InlineKeyboardButton(text='Регистрация', url='https://wmrfast.com/?r=1722423')
url_wmrfast_buy = InlineKeyboardButton(text='Я хочу купить бота', callback_data='buy_process_5')
url_wmrfast_info = InlineKeyboardButton(text='Подробнее о боте Wmrfast', callback_data='aboutWmrfast')
url_wmrfast_already = InlineKeyboardButton(text='Я прошел регистрацию', callback_data='alreadyWmrfast')
url_wmrfast.add(url_wmrfast_reg, url_wmrfast_info, url_wmrfast_already, url_wmrfast_buy)

# покупка Aviso
cell_aviso = InlineKeyboardMarkup()
start_buy_aviso = InlineKeyboardButton(text='Перейти к покупке', callback_data='cell_1')
cell_aviso.add(start_buy_aviso)

# покупка Seofast
cell_seofast = InlineKeyboardMarkup()
start_buy_seofast = InlineKeyboardButton(text='Перейти к покупке', callback_data='cell_2')
cell_seofast.add(start_buy_seofast)

# покупка Profitcentr
cell_profitcentr = InlineKeyboardMarkup()
start_buy_profitcentr = InlineKeyboardButton(text='Перейти к покупке', callback_data='cell_3')
cell_profitcentr.add(start_buy_profitcentr)

# покупка Seotime
cell_seotime = InlineKeyboardMarkup()
start_buy_seotime = InlineKeyboardButton(text='Перейти к покупке', callback_data='cell_4')
cell_seotime.add(start_buy_seotime)

# покупка wmrfast
cell_wmrfast = InlineKeyboardMarkup()
start_buy_wmrfast = InlineKeyboardButton(text='Перейти к покупке', callback_data='cell_5')
cell_wmrfast.add(start_buy_wmrfast)
