"""
This script is based on the guide from Habr:
https://habr.com/ru/articles/821415/

The code sets up a Telegram bot using Aiogram that handles payments through Telegram Stars.
It includes features such as sending an invoice and handling successful payments.
"""

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice, PreCheckoutQuery, ContentType
from aiogram.utils import executor
import aiohttp

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_pay_command(message: types.Message):
    prices = [LabeledPrice(label='Stars Payment', amount=1)]
    await bot.send_invoice(
        message.chat.id,
        title='Stars Payment Example',
        description='Payment for services via Stars.',
        provider_token="",
        currency='XTR',
        prices=prices,
        start_parameter='stars-payment',
        payload='stars-payment-payload'
    )


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    payment_info = message.successful_payment
    amount_in_stars = payment_info.total_amount
    currency = payment_info.currency
    transaction_id = payment_info.provider_payment_charge_id

    await message.reply(
        f"*🎉 Payment successful!*\n"
        f"💲 *Amount:* {amount_in_stars}⭐️\n"
        # f"*Currency:* {currency}\n"
        f"🆔 *Transaction ID:* `{transaction_id}`",
        parse_mode='Markdown'
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
