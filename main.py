import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from bot.handlers import start_command, about_command, pay_command, successful_payment, process_pre_checkout_query
from cfg import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(about_command, commands=['about'])
dp.register_message_handler(pay_command, commands=['pay'])
dp.register_message_handler(successful_payment, content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
dp.register_pre_checkout_query_handler(process_pre_checkout_query)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
