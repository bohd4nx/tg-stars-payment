# from aiogram import Bot
# from aiogram.types import LabeledPrice
#
#
# async def pay_command(message: types.Message):
#     prices = [LabeledPrice(label='Stars', amount=1)]
#     await message.bot.send_invoice(
#         chat_id=message.chat.id,
#         title='Stars Payment Example',
#         description='Payment for services via Stars.',
#         provider_token="",  # Payment system token, for Telegram Stars we simply send an empty string.
#         currency='XTR',  # Payment currency, for Telegram Stars it is XTR
#         prices=prices,
#         start_parameter='stars-payment',
#         payload='stars-payment-payload'  # Payment label. It is not displayed to the user, but can be used to separate payments by their types, etc. Maximum 128 bytes
#     )
#
#
# async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
#     await pre_checkout_query.bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
