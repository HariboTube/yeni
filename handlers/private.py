from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Star Müzik tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://images.app.goo.gl/ZV9ySkukJLbvMckX6",
                caption=(f"""**Hello** {message.from_user.mention} \n\n**I'm a Security Bot I can protect your group from any kind of damage !** \n\n**Add me to the Group Make it an Admin and Then use the /reload Command !** \n\n **Commands** : \n- /ActiveBot =  The security measure is activated \n- /NegativeBot = All measures disabled \n- /id = User id"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add Me to Group ➕", url=f"https://t.me/ProtectrontBot?startgroup=true"
                    )
                ]
                
           ]
        ),
    )



@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>🇹🇷 Tüm Komutlar : \n\n» /vbul => ᴠɪᴅᴇᴏ ɪɴᴅɪʀ . \n» /bul => ᴍᴜᴢɪᴋ ɪɴᴅɪʀ . \n» /oynat => ᴍᴜᴢɪᴋ ᴏʏɴᴀᴛ . \n» /durdur => ᴍᴜᴢɪɢɪ ᴅᴜʀᴅᴜʀ . \n» /devam => ᴍᴜᴢɪɢɪ sᴜʀᴅᴜʀ . \n» /atla =>  ᴍᴜᴢɪɢɪ ᴀᴛʟᴀ . \n» /son => ᴍᴜᴢɪɢɪ sᴏɴʟᴀɴᴅɪʀ . \n» /katil => ᴀsɪsᴛᴀɴɪ ɢʀᴜʙᴀ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ . \n» /reload => ᴀᴅᴍɪɴ ʟɪsᴛᴇsɪɴɪ ɢᴜɴᴄᴇʟʟᴇʀ . \n\n» /auth => ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʏᴏɴᴇᴛɪᴄɪ ᴏʟᴍᴀᴅɪɢɪ ʜᴀʟᴅᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀsɪɴᴀ ɪᴢɪɴ ᴠᴇʀɪʀ .  \n\n» /unauth => ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ʏᴏɴᴇᴛɪᴄɪ ᴏʟᴍᴀᴅɪɢɪ ʜᴀʟᴅᴇ ᴋᴏᴍᴜᴛʟᴀʀɪ ᴋᴜʟʟᴀɴᴍᴀsɪɴɪ ᴇɴɢᴇʟʟᴇʀ . </b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🇹🇷 𝖠𝗌𝗂𝗌𝗍𝖺𝗇", url="https://t.me/StarMuzikAsistan"
                     ),
                     InlineKeyboardButton(
                         "🧑🏻‍💻 𝖮𝗐𝗇𝖾𝗋", url="https://t.me/Hayiboo"
                     )
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ 𝖦𝖾𝗋𝗂 ⬅️", callback_data="cbstart")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""● **𝖬𝖾𝗋𝗁𝖺𝖻𝖺** {query.from_user.mention} \n\n● **𝖡𝖾𝗇** {bot} !\n\n● **𝖲𝖾𝗌𝗅𝗂 𝖲𝗈𝗁𝖻𝖾𝗍𝗅𝖾𝗋𝖽𝖾 müzik 𝖢𝖺𝗅𝖺𝖻𝗂𝗅𝖾𝗇 𝖡𝗈𝗍𝗎𝗆 . . !** \n\n● **𝖡𝖺𝗇 𝖸𝖾𝗍𝗄𝗂𝗌𝗂𝗓, 𝖲𝖾𝗌 𝖸𝗈𝗇𝖾𝗍𝗂𝗆 𝖸𝖾𝗍𝗄𝗂𝗌𝗂 𝗏𝖾𝗋𝗂𝗉 𝖠𝗌𝗂𝗌𝗍𝖺𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾𝗒𝗂𝗇 . . !**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎉 𝖡𝖾𝗇𝗂 𝖦𝗋𝗎𝖻𝖺 𝖤𝗄𝗅𝖾 🎉", url=f"https://t.me/StarMuzikBot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 𝖪𝗈𝗆𝗎𝗍𝗅𝖺𝗋" , callback_data= "herkes"
                    ),
                    InlineKeyboardButton(
                        "🇹🇷 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url=f"https://t.me/StarBotKanal"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧑🏻‍💻 ɢɪᴛʜᴜʙ ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ 🧑🏻‍💻", url="https://github.com/MehmetAtes21/music"
                    )
                ]
                
           ]
        ),
    )
