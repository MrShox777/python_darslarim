from aiogram  import Dispatcher, Bot
from aiogram.dispatcher.filter import command
from aiogram.types.message import Message
from config import bot_token

bot = Bot(bot_token)
dp = Dispatcher(bot)

@dp.message_handler()
async def lalala(message: Message):
	if  massage.text == "/start":
		bot.send_massage(chat_id=massage.from_user.id, text="Salom")
	else:
		bot.send_massage(chat_id=massage from_user.id, text=massage.text)	

