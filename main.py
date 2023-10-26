import logging
from aiogram import Bot, Dispatcher, types, executor
from youtube_downloader import *
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def get_bot_name():
    bot_info = await bot.me
    bot_name = bot_info.username
    return bot_name

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    chat_id = message.chat.id
    bot_name = await get_bot_name()
    await bot.send_message(chat_id, f"""🌟 Welcome to {bot_name}! 🤖

{bot_name} is a multi-functional bot ready to help you with various tasks:

🔸 /start - Start bot.
🔸 /help - Get help and a list of available commands.
🔸 /info - Get information about the bot and author.
🔸 /download - Download videos from Youtube, Tik-Tok, Instagram
🔸 /convert - Easily convert the files 
🔸 /search - Search for information on GPT-4.0 or other AI.
🔸 /translate - Translate text with deepl api.
🔸 /updates - Read the latest updates.    

Enjoy using it! 🚀""")

@dp.message_handler(commands=["download"])
async def text_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Enter link:")
    global waiting_for_link
    waiting_for_link = True

@dp.message_handler(lambda message: waiting_for_link)
async def process_link(message: types.Message):
    chat_id = message.chat.id
    link = message.text

    if link.startswith("https://www.youtube.com/") or link.startswith("https://youtu.be/"):
        await bot.send_message(chat_id, "Processing...")
        await yt_downloader(link, message, bot)
    ##elif link.startswith("https://www.tiktok.com/") or link.startswith("https://vm.tiktok.com/")  or link.startswith("https://vt.tiktok.com/"):




    else:
        await bot.send_message(chat_id, "Invalid link. Please provide a valid link.")
    global waiting_for_link
waiting_for_link = False






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
