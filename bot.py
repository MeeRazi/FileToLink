
from pyrogram import Client, __version__
from info import API_ID, API_HASH, BOT_TOKEN, PORT
from utils import temp
from aiohttp import web
from web.route import web_server


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="FileToLinkBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=10,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        temp.BOT = self
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", PORT).start()

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")
    
app = Bot()
app.run()
