from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "ShizukaXMusic",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def start(client, message):
    await message.reply_text("👋 Hello! I am ShizukaX Music Bot.")

app.run()
sss