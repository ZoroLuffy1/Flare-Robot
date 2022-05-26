import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot


PHOTO = "https://telegra.ph/file/c48c88cc0f159a83a69ee.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = "**♡ I,m Ruka ʀᴏʙᴏᴛ 愛** \n\n"
    TEXT += f"**♡ I'm Working With sᴇxʏ Speed** \n\n"
    TEXT += f"**♡ Ruka: LATEST Version** \n\n"
    TEXT += f"**♡ My Creator: [kirito](http://t.me/asta_est)** \n\n"
    TEXT += f"**♡ ᴀɴʏ ɪssᴜᴇs ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ @rukaxSuport** \n\n"
    TEXT += "**♡ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ 💘💘💘**"
    BUTTON = [
        [
            Button.url("📢 Updates", "https://t.me/rukaxupdate"),
            Button.url("🚑 Support", "https://t.me/rukaxsuport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
