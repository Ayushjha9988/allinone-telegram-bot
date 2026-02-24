from pyrogram import Client, filters
import os

# Railway Environment Variable se BOT_TOKEN lega
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Simple Bot Client (API_ID / API_HASH ki zarurat nahi)
app = Client(
    "mybot",
    bot_token=BOT_TOKEN
)

# /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "🔥 All In One Bot Running Successfully 🚀"
    )

# /ping command
@app.on_message(filters.command("ping"))
async def ping(client, message):
    await message.reply_text("🏓 Pong!")

# Bot start
app.run()
