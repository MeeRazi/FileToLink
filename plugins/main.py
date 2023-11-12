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

    file_name = file_id.file_name.replace("_", " ").replace(".mp4", "").replace(".mkv", "").replace(".", " ")

    online = f"{URL}/watch/{msg.id}"
    download = f"{URL}/download/{msg.id}"

    link = f"{URL}/watch/{msg.id}"
    await client.send_message(text=f"<b>Requested By: {message.from_user.mention}\n\nLink:</b>\n{link}", chat_id=BIN_CHANNEL, disable_web_page_preview=True)

    await message.reply_text(
        text=f"<b>Here Is Your Streamable Link\n\nFile Name</b>:\n<code>{file_name}</code>\n\n<b>Powered By - <a href=https://t.me/iPRIMEHUB>©𝐏𝐫𝐢𝐦𝐞𝐇𝐮𝐛™</a></b>",
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
    await message.reply_text(f"**Dude! Send me a video file.**")