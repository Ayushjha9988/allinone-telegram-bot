import os
import asyncio
from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.filters import command

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start_handler(client, message):
    await message.reply_text("Bot running on Render 🚀")

async def main():
    app = Client(
        "mybot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )

    app.add_handler(MessageHandler(start_handler, command("start")))

    await app.start()
    print("Bot Started Successfully!")
    await idle()

from pyrogram import idle

if __name__ == "__main__":
    asyncio.run(main())
