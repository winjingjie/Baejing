from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from menu import start, main_menu,one_year_menu,six_months_menu,about_us_menu,\
    curriculum_one_year_menu,cost_menu,why_menu,rent_ans, pay_ans


############################# Handlers #########################################
# updater = Updater(token="951889071:AAGp5NagI0OlDVVsm4D9n08NfPBlnvkUL0M") ## xiaojie old token
updater = Updater("1022877467:AAHEP1tHO3N_5LchUZZ6rJR2WuotawMx8eQ") ## nocbj token

updater.dispatcher.add_handler(CommandHandler('start', start))


updater.dispatcher.add_handler(CallbackQueryHandler(main_menu,
                                                    pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(one_year_menu,
                                                    pattern='one_year'))
updater.dispatcher.add_handler(CallbackQueryHandler(six_months_menu,
                                                    pattern='six_months'))
updater.dispatcher.add_handler(CallbackQueryHandler(about_us_menu,
                                                    pattern='about_us'))
updater.dispatcher.add_handler(CallbackQueryHandler(curriculum_one_year_menu,
                                                    pattern='curriculum_one_year'))
updater.dispatcher.add_handler(CallbackQueryHandler(cost_menu,
                                                    pattern='cost'))
updater.dispatcher.add_handler(CallbackQueryHandler(why_menu,
                                                    pattern='why'))
updater.dispatcher.add_handler(CallbackQueryHandler(rent_ans,
                                                    pattern='rent'))
updater.dispatcher.add_handler(CallbackQueryHandler(pay_ans,
                                                    pattern='pay'))


updater.start_polling()
