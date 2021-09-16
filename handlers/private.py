from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/ed4f68f51b48861989d6e.jpg")
    await message.reply_text(
        f"""**Hey, I'm 『𝙿𝚁𝙸𝙽_𝚂𝙴𝙲𝙲✰』 | Mᴜsɪᴄ Bᴏᴛ |🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Developed by [『𝙿𝚁𝙸𝙽_𝚂𝙴𝙲𝙲✰』](https://t.me/PRIN_SECC)

Add me to your group and play music freely😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ", url="https://t.me/AQUAMAN_XD")
                  ],[
                    InlineKeyboardButton(
                        "🛡 SUPPORT GROUP 🛡", url="https://t.me/AQUAMAN_XD_WORLD"
                    ),
                ],[ 
                    InlineKeyboardButton(
                        "GROUP ME LEJAO 😆", url="https://t.me/AQUAMAN_MUSIC_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**BOT IS WORKING**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛡 SUPPORT 🛡", url="https://t.me/AQUAMAN_XD_WORLD")
                ]
            ]
        )
   )


