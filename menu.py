from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


## Instantiate
def start(bot, update):
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())
def main_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=main_menu_message(),
                          reply_markup=main_menu_keyboard())
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('One Year?',
                                      callback_data='one_year')],
                [InlineKeyboardButton('6 Months?',
                                      callback_data='six_months')],
                [InlineKeyboardButton('About Us',
                                      callback_data='about_us')]
                ]
    return InlineKeyboardMarkup(keyboard)

def main_menu_message():
    return '''NOCBeijing Asks:'''


## One year menu ########################################
def one_year_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=one_year_menu_message(),
                          reply_markup=one_year_menu_keyboard())

def one_year_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Curriculum?',
                                      callback_data='curriculum_one_year')],
                [InlineKeyboardButton('Cost of Living & Intern Pay?',
                                      callback_data='cost')],
                [InlineKeyboardButton('Why NOC Beijing?',
                                      callback_data='why')],
                [InlineKeyboardButton('What kind of jobs can I get?',
                                      callback_data='jobs')],
                [InlineKeyboardButton('Main menu',
                                      callback_data='main')]
                ]
    return InlineKeyboardMarkup(keyboard)

def one_year_menu_message():
    return 'One Year Programme is actually 10 months. We think that one year provides ' \
           'the full experience of NOC compared to 6 months'


## 6 months menu########################################
########################################################
def six_months_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=six_months_menu_message(),
                          reply_markup=six_months_menu_keyboard())
def six_months_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Curriculum?',
                                      callback_data='m2_1')],
                [InlineKeyboardButton('Cost of Living & Intern Pay?',
                                      callback_data='m2_2')],
                [InlineKeyboardButton('Why NOC Beijing?',
                                      callback_data='m2_3')],
                [InlineKeyboardButton('What kind of jobs can I get?',
                                      callback_data='m2_4')],
                [InlineKeyboardButton('Main menu',
                                      callback_data='main')]
                ]
    return InlineKeyboardMarkup(keyboard)

def six_months_menu_message():
    return 'Six Months Programme is a shorter internship programme (about half of One Year Programme) ' \
           'but it is definitely still a fulfilling experience'


## about us menu########################################

def about_us_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=about_us_menu_message(),
                          reply_markup=about_us_menu_keyboard())
def about_us_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Instagram',
                                      callback_data='m2_1')],
                [InlineKeyboardButton('LinkedIn',
                                      callback_data='m2_2')],
                [InlineKeyboardButton('Main menu',
                                      callback_data='main')]
                ]
    return InlineKeyboardMarkup(keyboard)

def about_us_menu_message():
    return 'NOCBeijing has a student committee that actually do stuff. ' \
           'Follow us on Instagram and LinkedIn to find out more about our events!'


## curriculum

def curriculum_one_year_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=curriculum_one_year_menu_message(),
                          reply_markup=curriculum_one_year_menu_keyboard())

def curriculum_one_year_menu_keyboard():
    keyboard = [[InlineKeyboardButton('FASS',
                                      callback_data='m1_1_1')],
                [InlineKeyboardButton('Engineering',
                                      callback_data='m1_1_2')],
                [InlineKeyboardButton('SDE',
                                      callback_data='m1_1_3')],
                [InlineKeyboardButton('Business',
                                      callback_data='m1_1_4')],
                [InlineKeyboardButton('Back',
                                      callback_data='one_year')]
                ]
    return InlineKeyboardMarkup(keyboard)

def curriculum_one_year_menu_message():
    return 'Depending on your faculty and duration of the programme, up to ' \
           '40 Modular Credits can be cleared'


## cost_menu

def cost_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=cost_menu_message(),
                          reply_markup=cost_menu_keyboard())

def cost_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Rent',
                                      callback_data='rent')],
                [InlineKeyboardButton('Pay',
                                      callback_data='pay')],
                [InlineKeyboardButton('Financial Aid',
                                      callback_data='m1_1_3')],
                [InlineKeyboardButton('Scholarships and Awards',
                                      callback_data='m1_1_4')],
                [InlineKeyboardButton('Back',
                                      callback_data='one_year')]
                ]
    return InlineKeyboardMarkup(keyboard)

def cost_menu_message():
    return 'Its really not that expensive to eat and shop in Beijing. However the rent though..'


## why menu

def why_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=why_menu_message(),
                          reply_markup=why_menu_keyboard())
def why_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Entrepreneurial Scene',
                                      callback_data='m1_1_1')],
                [InlineKeyboardButton('Food',
                                      callback_data='m1_1_2')],
                [InlineKeyboardButton('Safety',
                                      callback_data='m1_1_3')],
                [InlineKeyboardButton('Travel',
                                      callback_data='m1_1_4')],
                [InlineKeyboardButton('Back',
                                      callback_data='one_year')]
                ]
    return InlineKeyboardMarkup(keyboard)

def why_menu_message():
    return '''Why NOC Beijing??? Because it's hella L I T here FAM!!!! ''' \
           "There's really so much to do it doesn't make sense lmaoo.."


## jobs menu

def jobs_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=jobs_menu_message(),
                          reply_markup=jobs_menu_keyboard())

def jobs_menu_keyboard():
    keyboard = [[InlineKeyboardButton('???',
                                      callback_data='m1_1_1')],
                [InlineKeyboardButton('???',
                                      callback_data='m1_1_2')],
                [InlineKeyboardButton('???',
                                      callback_data='m1_1_3')],
                [InlineKeyboardButton('???',
                                      callback_data='m1_1_4')],
                [InlineKeyboardButton('Back',
                                      callback_data='one_year')]
                ]
    return InlineKeyboardMarkup(keyboard)

def jobs_menu_message():
    return 'Only honorable jobs!!!'


#### End of Message ###################

def rent_ans(bot, update):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton('Back',
                                      callback_data='rent')]
                ]
    markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=query.message.chat_id,
                     message_id=query.message.message_id,
                     text=' the rent is ~$600 sgd per month',
                     reply_markup=None)
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text='',
                          reply_markup=markup)

def pay_ans(bot, update):
    query = update.callback_query
    keyboard = [[InlineKeyboardButton('Back',
                                      callback_data='cost')]
                ]
    markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=query.message.chat_id,
                     message_id=query.message.message_id,
                     text=' the pay is ~$600 sgd per month',
                     reply_markup=None)
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text= '',
                          reply_markup=markup)

# if __name__ == '__main__':
