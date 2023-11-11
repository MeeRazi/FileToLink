from pyrogram import Client, filters
from info import URL, BIN_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(f"**Hello {message.from_user.mention},\nI am a Telegram Video Stream Bot. Send me any video and I will give you streaming & download link.**")


@Client.on_message((filters.private) & (filters.document | filters.video) , group=4)
async def private_receive_handler(client, message):
    file_id = message.document or message.video

    msg = await message.forward(
        chat_id=BIN_CHANNEL)

        #file_id=file_id.file_id,
        #caption=f"**File Name:** {file_id.file_name}\n**User:** {message.from_user.mention}",)

    online = f"{URL}/watch/{msg.id}"
    download = f"{URL}/download/{msg.id}"
    await message.reply_text(
        text=f"<b>File Name</b>:\n<code>{file_id.file_name}</code>\n\n<b>Streaming Link:</b>\n{online}\n\n<b>Download Link:</b>\n{download}",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Watch", url=online),
                InlineKeyboardButton("Download", url=download)
            ]
        ]
    ),
    disable_web_page_preview=True)

@Client.on_message((filters.private) & (filters.photo | filters.audio) , group=4)
async def photo_audio_erorr(client, message):
    await message.reply_text(f"**Error! Send me a video file.**")