from Bikashhalder import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from Bikashhalder import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/860117bc941734b04265c.jpg"

BGT_Help = "🔥 🇧𝗚𝗧 🇸𝗣𝗔𝗠 🇧𝗢𝗧 🔥\n\n"
 
BGT_Help += f"🇧𝗚𝗧 🇸𝗣𝗔𝗠🇧𝗢𝗧 𝗔𝗟𝗟 𝗖𝗠𝗗𝗦 ➪\n\n"

BGT_Help += f" ᐁ 𝐒𝐩𝐚𝐦 𝐁𝐨𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝'𝐒 ᐁ\n\n"

BGT_Help += f" `$ping` - ᴄʜᴇᴄᴋ ᴘɪɴɢ\n `$alive` - ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ/ᴠɪʀsɪᴏɴ ( ᴏɴʟʏ 1sᴛ sᴘᴀᴍʙᴏᴛ ᴡɪʟʟ ʀᴇᴘʟʏ )\n .`$restart` - ʀᴇsᴛᴀʀᴛ ᴀʟʟ ʙᴏᴛs \n `$addecho` -  ᴛᴏ ᴀᴅᴅ ᴇᴄʜᴏ \n `$rmecho` - ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴇᴄʜᴏ \n `$addsudo` - ᴛᴏ ᴀᴅᴅ sᴜᴅᴏ ᴜsᴇʀ ᴜsɪɴɢ sᴘᴀᴍ ʙᴏᴛs \n\n"
 
BGT_Help += f" ᐁ 𝐋𝐞𝐚𝐯𝐞 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 ᐁ\n\n"

BGT_Help += f" `$leave` - ᴛᴏ ʟᴇᴀᴠᴇ ᴀɴʏ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ \n\n"
 
BGT_Help += f" ࿇𝐀𝐥𝐥 𝐒𝐩𝐚𝐦 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 ࿇ \n\n"

BGT_Help += f" `$raid` - ᴛᴏ ʀᴀɪᴅ\n `$replyraid` - ᴀᴄᴛɪᴠᴇ ʀᴇᴘʟʏ ʀᴀɪᴅ\n `$dreplyraid` -ᴅᴇ-ᴀᴄᴛɪᴠᴇ ʀᴇᴘʟʏ ʀᴀɪᴅ\n `$spam` - ᴛᴏ  ɴᴏʀᴍᴀʟ sᴘᴀᴍ\n `$bigspam` - ᴜsᴇ ᴛᴏ ʙɪɢ sᴘᴀᴍ\n `$uspam` - ᴜsᴇ ᴏɴʟʏ ᴜɴʟɪᴍɪᴛᴇᴅ sᴘᴀᴍ ᴜ ᴡᴀɴᴛ sᴛᴏᴘ sᴘᴀᴍ ᴛʜᴇɴ ʀᴇsᴛᴀʀᴛ ʙᴏᴛs!!\n `$bgtspam` - ᴛʜɪs sᴘᴀᴍ ᴜsᴇ ᴏɴʟʏ 18+ Usᴇʀ (ᴘᴏʀɴ)\n\n"

BGT_Help += f" `$bgtopspam` -  ᴏɴʟʏ sʜᴏᴡ ᴛʜɪs ʜᴇʟᴘ 〠᯼\n\n"

BGT_Help += f"♕︎𝐂𝐫𝐞𝐚𝐭𝐨𝐫♕︎ @BikashHalder\n"

BGT_Help += f"♕︎𝐂𝐫𝐞𝐚𝐭𝐨𝐫♕︎ @AdityaHalder\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=BGT_Help,
                                  buttons=[
        [
        Button.url("𝐁𝐆𝐓", "https://t.me/BikashGedgetsTech"),
        Button.url("𝐊𝐖", "https://t.me/Kaalware")
        ] 
        ]
        )                                                         
