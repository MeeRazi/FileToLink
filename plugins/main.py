from pyrogram import Client, filters
from info import URL, BIN_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(f"**Hello {message.from_user.mention},\n\nI am a Telegram Video Stream Bot. Send me any video and I will give you streaming & download link.**")


@Client.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) , group=4)
async def private_receive_handler(client, message):
    file_id = message.document or message.video or message.audio or message.photo
    msg = await client.send_cached_media(
        chat_id=BIN_CHANNEL,
        file_id=file_id.file_id)
    online = f"{URL}/watch/{msg.id}"
    download = f"{URL}/download/{msg.id}"
    await message.reply_text(
        text=f"**Streaming Link:** \n{online}\n\n**Download Link:** \n{download}",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Watch", url=online),
                InlineKeyboardButton("Download", url=download)
            ]
        ]
    ))
