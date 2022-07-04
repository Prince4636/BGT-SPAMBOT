from Bikashhalder import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from Bikashhalder import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/860117bc941734b04265c.jpg"

BGT_Help = "🔥 🇧𝗚𝗧 🇸𝗣𝗔𝗠 🇧𝗢𝗧 🔥\n\n"
 
BGT_Help += f"☜🇧𝗚𝗧 🇸𝗣𝗔𝗠 🇧𝗢𝗧 𝗔𝗟𝗟 𝗖𝗠𝗗𝗦 ☞\n\n"

BGT_Help += f" ∨ 𝑺ƤƛM ƁƠƬ ƇMƊƧ ∨\n\n"

BGT_Help += f" `$ping` - ƇӇЄƇƘ ƤƖƝƓ\n `$alive` - ƇӇЄƇƘ ƁƠƬ ƛԼƖƔЄ/ƔЄƦƧƖƠƝ ( ƠƝԼƳ 1ƧƬ ƧƤƛMƝƠƬ ƦЄƤԼƳ)\n .`$restart` - ƦЄƧƬƛƦƬ ƛԼԼ ƁƠƬƧ \n `$addecho` -  ƬƠ ƛƊƊ ЄƇӇƠ \n `$rmecho` - ƬƠ ƦЄMƠƔЄ ЄƇӇƠ \n `$addsudo` - ƬƠ ƛƊƊ ƧƲƊƠ ƲƧЄƦ ƲƧƖƝƓ ƧƤƛM ƁƠƬƧ \n\n"
 
BGT_Help += f" ᐁ ԼЄƛƔЄ ƇƠMMƛƊ ᐁ\n\n"

BGT_Help += f" `$leave` - ƬƠ ԼЄƛƔЄ ƛƝƳ ƇӇƝƝƝЄԼ ƠƦ ƓƦƠƲƤ \n\n"
 
BGT_Help += f" ࿇ƛԼԼ ƧƤƛM ƇƠMMƛƝƊ ࿇ \n\n"

BGT_Help += f" `$raid` - ƬƠ ƦƛƖƊ\n `$replyraid` - ƛƇƬƖƔЄ ƦЄƤԼƳ ƦƛƖƊ\n `$dreplyraid` -ƊЄ-ƛƇƬƖƔЄ ƦЄƤԼƳ ƦƛƖƊ\n `$spam` - ƬӇƖƧ ƇMƊ ƲƧЄ ƠƝԼƳ ƝƠƦMƛԼ ƧƤƛM\n `$bigspam` - ƲƧЄ ƬƠ ƁƖƓ ƧƤƛM\n `$uspam` - ƲƧЄ ƠƝԼƳ ƲƝԼƖMƖƬЄƊ ƧƤƛM Ʋ ƜƛƝƬ ƧƬƠƤ ƧƤƛM ƬЄƝ ƦЄƧƬƛƦƬ ƁƠƬƧ!!\n `$bgtspam` - ƬӇƖƧ ƇMƊ ƲƧЄ ƠƝԼƳ 18+ƲƧЄƦ\n\n"

BGT_Help += f" $bgtopspam -  ƊƠƝ'Ƭ ƲƧЄ ƬӇƖƧ ƇƠMMƛƝƊ 〠᯼\n\n"

BGT_Help += f"♕︎ƠƜƝЄƦ♕︎ @BikashHalder\n"

BGT_Help += f"♕︎ƠƜƝЄƦ♕︎ @AdityaHalder\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=BGT_Help,
                                  buttons=[
        [
        Button.url("𝐂𝐡𝐚𝐧𝐧𝐞𝐥", "https://t.me/BikashGedgetsTech"),
        Button.url("𝐊𝐖", "https://t.me/Kaalware")
        ] 
        ]
        )                                                         
