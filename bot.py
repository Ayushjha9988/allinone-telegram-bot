import os, asyncio, yt_dlp
from pyrogram import Client, filters

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS").split(",")))

queues = {}
def add_to_queue(chat_id, item):
    if chat_id not in queues:
        queues[chat_id] = []
    queues[chat_id].append(item)

app = Client("allinonebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("help"))
async def help_cmd(_, message):
    await message.reply("Bot working ✅\nUse /play <song name>")

@app.on_message(filters.command("play"))
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /play <song name>")
    query = " ".join(message.command[1:])
    await message.reply(f"Searching: {query}")

async def main():
    await app.start()
    print("Bot Started Successfully 🚀")
    await asyncio.Event().wait()

asyncio.run(main())
