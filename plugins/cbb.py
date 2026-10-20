#Coded by @Its_Tartaglia_Childe

from pyrogram import Client 
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"<b>Bot Cammands\n❏ Commands For BOT Admins\n├/start : start the bot or get posts\n├/batch : Create Group Message\n├/genlink : create link for one post\n├/users : view bot statistics\n├/broadcast : broadcast Message\n└/stats : checking your bot uptime\n\n👨‍💻 Developed by <a href=https://t.me/Its_Oreki_Hotarou>Hōᴛᴀʀō Oʀᴇᴋɪ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💥​ᴄʟᴏꜱᴇ​💥", callback_data="close"),
                        InlineKeyboardButton("⚡ᴀʙᴏᴜᴛ⚡", callback_data="about")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>Hi there this is a file store bot which is convert any file to link...\nthen you can access this file through a specific link...!\n\nCreator - @Its_Oreki_Hotarou\nMy Channel - @Anime_pirates\nDicsussion Group - @Hunters_Discussion</a>\n\n👨‍💻 Developed by @Its_Oreki_Hotarou</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💥​ᴄʟᴏꜱᴇ​💥", callback_data="close"),
                        InlineKeyboardButton("🚀ʜᴇʟᴘ🚀", callback_data="help")
                    ]
                ]
            )
        )
    elif data == "how_verify":
        await query.answer(
            "1. Tap ✅ Verify Now\n2. Watch the ad until the timer ends\n3. Your files arrive automatically\n\nAd not loading? Switch WiFi/mobile data and try again.",
            show_alert=True
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
