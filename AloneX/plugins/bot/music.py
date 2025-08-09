from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneX import app
from config import BOT_USERNAME
#from AloneX.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ 𝗧ɢ 𝗡ᴀᴍᴇ - [⏤͟͟͞͞𓆩 𝐊ɪɴɢ ꭙ 𓆪](https://t.me/ofline_king)
│├ 𝗙ᴜʟʟ 𝗜ɴғᴏ - [𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ](https://t.me/AboutBotMaker)
│├─────────────────╯
├┼─────────────────⦿
│├─────────────────╮
│├ 𝗢ᴡɴᴇʀ│ [𝐀ʟᴏɴᴇ 𝗖ᴏᴅᴇʀ](https://t.me/NobiCreator)
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("\x41\x4C\x4F\x4E\x45\x20\x43\x4F\x44\x45\x52", url=f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x68\x75\x56\x61\x69")
        ],
        [
          InlineKeyboardButton("\x41\x4C\x4C\x20\x52\x45\x50\x4F", url="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x55\x70\x64\x61\x74\x65\x73\x2F\x31\x30\x37"),
          InlineKeyboardButton("\x52\x45\x50\x4F", url="\x68\x74\x74\x70\x73\x3A\x2F\x2F\x67\x69\x74\x68\x75\x62\x2E\x63\x6F\x6D\x2F\x54\x65\x61\x6D\x41\x6C\x6F\x6E\x65\x4F\x70\x2F\x41\x6C\x6F\x6E\x65\x58"),
          ],
               [
                InlineKeyboardButton("\x41\x4C\x4F\x4E\x45\x20\x4E\x45\x54\x57\x4F\x52\x4B", url=f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x55\x70\x64\x61\x74\x65\x73"),
],
[
InlineKeyboardButton("\x4F\x46\x46\x49\x43\x49\x41\x4C\x20\x42\x4F\x54", url=f"\x68\x74\x74\x70\x73\x3A\x2F\x2F\x74\x2E\x6D\x65\x2F\x41\x6C\x6F\x6E\x65\x58\x4D\x75\x73\x69\x63\x42\x6F\x74"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/bjs367.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
