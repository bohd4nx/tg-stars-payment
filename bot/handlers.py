import logging
import os
from aiogram import types, Bot
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton, LabeledPrice, PreCheckoutQuery
# from bot.stars_payment import send_payment_invoice, process_pre_checkout_query
from aiogram.utils.exceptions import TelegramAPIError
from cfg import CHANNEL, GITHUB, PORTFOLIO, RESUME

logging.basicConfig(level=logging.INFO)


async def start_command(message: types.Message):
    image_path = os.path.abspath('assets/hello.jpg')
    start_image = InputFile(image_path)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(text="🌐 Portfolio", url=PORTFOLIO),
        InlineKeyboardButton(text="🔗 Channel", url=CHANNEL)
    )
    caption = (
        "👾 This bot is an example of payment integration in `⭐️Stars.`\n\n"
        "🤖 Source: [GitHub Repository](https://github.com/bohd4nx/tg-stars-payment)\n\n"
        "*Available Commands:*\n"
        "/start - Start bot.\n"
        "/about - Learn more about me.\n"
        "/pay - See and test how payment works.\n"
    )

    await message.answer_photo(
        photo=start_image,
        caption=caption,
        parse_mode="Markdown",
        reply_markup=markup
    )


async def about_command(message: types.Message):
    image_path = os.path.abspath('assets/about.jpg')
    about_image = InputFile(image_path)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton(text="👨‍💻 Hire up", url=RESUME),
        InlineKeyboardButton(text="🔗 GitHub", url=GITHUB)
    )

    caption = (
        "👋 *Hello!* \n\n"
        "I'm a Fullstack & Python developer specializing in creating innovative and efficient solutions for various applications. "
        "With a deep passion for coding and a strong background in both front-end and back-end development, I bring a comprehensive approach to every project.\n\n"
        "🔧 *Expertise Includes:*\n"
        "- Fullstack Development 🌐\n"
        "- Python Programming 🐍\n"
        "- API Integrations 🔗\n"
        "- Web3 and Blockchain Technologies 💰\n\n"
        "Let's build something amazing together! 🚀"
    )
    await message.answer_photo(
        photo=about_image,
        caption=caption,
        parse_mode="Markdown",
        reply_markup=markup
    )


async def pay_command(message: types.Message):
    prices = [LabeledPrice(label='Stars', amount=1)]
    await message.bot.send_invoice(
        chat_id=message.chat.id,
        title='Stars Payment Example',
        description='Payment for services via Stars.',
        provider_token="",  # Payment system token, for Telegram Stars we simply send an empty string.
        currency='XTR',  # Payment currency, for Telegram Stars it is XTR
        prices=prices,
        start_parameter='stars-payment',
        payload='stars-payment-payload'  # Payment label. It is not displayed to the user, but can be used to separate payments by their types, etc. Maximum 128 bytes
    )


async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message):
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
