#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><blockquote>◈ Creator : <a href=https://t.me/aaashu_202>ashu</a>\n◈ Founder : <a href=https://t.me/Dramafilez>Dramafilez</a>\n◈ Series Channel : <a href=https://t.me/As_Movies_Bot_Disscussion>AS Movies Group</a>\n◈ Support Group :  <a href='https://t.me/+5dYQcJbrLkRmODJl'>Click here</a>\n</blockquote></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
