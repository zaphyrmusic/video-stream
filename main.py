import asyncio

from program import LOGS
from pytgcalls import idle
from driver.core import calls, bot, user


async def start_bot():
    await bot.start()
    LOGS.info("[INFO]: BOT & USERBOT CLIENT STARTED !!")
    await calls.start()
    LOGS.info("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("VeezSupportGroup")
    await user.join_chat("levinachannel")
    await idle()
    LOGS.info("[INFO]: BOT & USERBOT CLIENT STOPPED !!")
    await bot.stop()


asyncio.run(start_bot())
