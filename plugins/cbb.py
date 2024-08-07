#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐎ᴡɴᴇʀ : <a href='https://t.me/WhiteBeard_sama'>𝐖𝐃𝐆 - 𝟓</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Shirohige_Animes'>𝐒ʜɪʀᴏʜɪɢᴇ 𝐀ɴɪᴍᴇ</a>\n○ 𝐎ɴɢᴏɪɴɢ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Ongoing_Anime_WDG_5'>𝐎ɴɢᴏɪɴɢ 𝐖𝐃𝐆 - 𝟓</a>\n○ 𝐇ᴇᴍᴛᴀɪ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/+zPM3HDvFOvg5Yjg1'>𝐃𝐒𝐇 - 𝐁𝐀𝐂𝐊𝐔𝐏</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ Cʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🧑‍💻 Dᴇᴠᴇʟᴏᴘᴇʀs', url='https://t.me/Straw_hat_bots')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


#⋗  ᴛᴇʟᴇɢʀᴀᴍ - @Codeflix_bots

#- ᴄʀᴇᴅɪᴛ - Github - @Codeflix-bots , @erotixe
#- ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
#- ᴛʜᴀɴᴋ ʏᴏᴜ ᴄᴏᴅᴇғʟɪx ʙᴏᴛs ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
#- ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ @Codeflix-bots  
#- ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ -> ᴛᴇʟᴇɢʀᴀᴍ @codeflix_bots Community @Otakflix_Network </b>
