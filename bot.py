import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def main():
    app = Client(
        "mybot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )

    @app.on_message(filters.command("start"))
    async def start(client, message):
        await message.reply_text("Bot is running on Render 🚀")

    await app.start()
    print("Bot Started Successfully!")
    await idle()

from pyrogram import idle

if __name__ == "__main__":
    asyncio.run(main())
