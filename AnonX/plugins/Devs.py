import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
import random
@app.on_message(
    command(["صورص","سييي","سورسيي","سورس سبارك", "السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/839cbe67ff070e5ff3b72.jpg",
        caption=f"""
 [𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙋𝘼𝙍𝙆](https://t.me/ZZZ7iZ)
 —————————————
 [𝙃 𝘼 𝙈 𝘿 ](https://t.me/IIIlIIv)
 
 [𓏺𓌹 𝐻𝑀𝑂𝐷 ᥫ᭡ ‌](https://t.me/IIIlIIv)
  
 [⍟𓏺𝙒𝞝𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙎𝙊𝙐𝙍𝘾𝙀 𝙎𝙋𝘼𝙍𝙆](https://t.me/ZZZ7iZ)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/ZZZ7iZ"), 
                ],[
                    InlineKeyboardButton(
                        "‹ مطور السورس ›", url=f"https://t.me/IIIlIIv"),
                ],

            ]

        ),

    )

@app.on_message(command([f"غنيلي", "غني", "غ", "{BOT_USERNAME} غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/iV_P_Nl/{rl}"
    await client.send_voice(message.chat.id,url,caption="[¦ تـم اختيـار الاغـنـية لـك](https://t.me/ZZZ7iZ)",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صوره","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="[💕 ¦ تـم اختيـار الصوره لـك]()https://t.me/ZZZ7iZ",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        

