import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from Bikashhalder import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID

BGT_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/55e7f313222edd0a94b5c.jpg"

Bgt_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/BikashGedgetsTech")
        ],
        [
        Button.url("• ᴍᴀɪɴᴛᴀɪɴ ʙʏ •", "https://t.me/Bikashhalder")
        ],
        [
        Button.url("• ᴍᴀɪɴᴛᴀɪɴ ʙʏ •", "https://t.me/Adityahalder")
        ]
        ]
               
BgtX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/BikashGedgetsTech"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Bgt_Chat")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/BgtUserbot/BGT-SPAMBOT")
        ]
        ]
        
        
#USERS 


@BOT0.on(events.NewMessage(pattern="/start"))
@BOT1.on(events.NewMessage(pattern="/start"))
@BOT2.on(events.NewMessage(pattern="/start"))
@BOT3.on(events.NewMessage(pattern="/start"))
@BOT4.on(events.NewMessage(pattern="/start"))
@BOT5.on(events.NewMessage(pattern="/start"))
@BOT6.on(events.NewMessage(pattern="/start"))
@BOT7.on(events.NewMessage(pattern="/start"))
@BOT8.on(events.NewMessage(pattern="/start"))
@BOT9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       BgtBot = await event.client.get_me()
       bot_id = BgtBot.first_name
       bot_username = BgtBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheBgt = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheBgt,
                  BGT_IMG,
                  caption=ownermsg, 
                  buttons=Bgt_Button)
       else:
            await event.client.send_file(TheBgt,
                  BGT_IMG,
                  caption=usermsg, 
                  buttons=BgtX_Button)
                
