#bismilah ar-rohman
import logging
import wikipedia

 
 
from aiogram import Bot, Dispatcher, executor, types
 
API_TOKEN = '5039498860:AAEApFq8nMxuRI4W-SV7XI4HcS1fc4W0x9o'
wikipedia.set_lang("uz")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.message):
   
    await message.reply("salom wikipediya botiga hush kelibsiz")

@dp.message_handler()
async def sendtelegram_bot2(message: types.message):
    try:
        respond = Wikipedia.summary(message.text)
        await masange.answer(respond)
    except:
        await message.answer("boshqa joydan qidiring")

    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 