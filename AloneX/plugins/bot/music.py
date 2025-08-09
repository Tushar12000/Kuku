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
          InlineKeyboardButton("👑 𝘽𝙊𝙏 𝙈𝘼𝙎𝙏𝙀𝙍", url="https://t.me/ofline_king"),]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/bjs367.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
