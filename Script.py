class script(object):   
    HELP_TXT = """<b>𝖧𝖺𝗒 {}    
ഈ ഒരു ബോട്ട് [@cinema_flix_updates] ൻ്റെ Auto Filter Bot ആണ്, ബോട്ട് Owner ഡെ പർമ്മിഷൻ ഇല്ലാതെ മറ്റു ഗ്രൂപ്പുകളിൽ ഒന്നും ഈ ബോട്ടിനെ യൂസ് ചെയ്യാൻ കഴിയില്ല..!!🤗⚠</b>"""

    ABOUT_TXT = """<b>╭────[⚠️ About Me ⚠️]────⍟
│
├<b>🤖 My Name: {}</b>
├<b>🧑‍💻 Creator: <a href=tg://settings>My Friend</b></a>  
├<b>👀 Developers: <a href=https://t.me/TG_x_filter>🇮🇳❍ 𝖒𝖆𝖓𝖙𝖎𝖘 ❍™◢ ◤</b></a>
├<b>📋 Language: Python3</b>
├<b>📡 DataBase: MongoDB</b>
├<b>📢 Movie Updates:  <a href=https://t.me/cinema_flix_updates>Join Here</b></a>
│
╰─────────────────────⍟</b>"""

    STATUS_TXT = """<b>╭────[♻️Status Board♻️]────⍟
│
├<b>📁 Total Files: <code>{}</code></b>
├<b>👥 Total Members: <code>{}</code></b>
├<b>♻️ Total Chats: <code>{}</code></b>
├<b>🗃 Used Storage: <code>{}</code> MB</b>
│
╰─────────────────────⍟</b>"""
    LOG_TEXT_G = """#AddNewGroup
    
<b>⪼ 👥 𝖦𝗋𝗈𝗎𝗉 : {a}</b>
<b>⪼ 🆔 𝖦𝗋𝗈𝗎𝗉 𝖨𝖣 : <code>{b}</code></b>
<b>⪼ 🧲 𝖦𝗋𝗈𝗎𝗉 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : @{c}</b>
<b>⪼ 🕵️‍♂️ 𝖳𝗈𝗍𝖺𝗅 𝖬𝖾𝗆𝖻𝖾𝗋𝗌 : {d}</b>
<b>⪼ 👨‍💻 𝖠𝖽𝖽𝖾𝖽 𝖡𝗒 :{e}</b>

<b>⪼🍃 𝖡𝗈𝗍 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : {f}</b>
"""
    LOG_TEXT_P = """#StartNewUser
    
<b>⪼ 🆔 𝖨𝖣 : <code>{}</code></b>
<b>⪼ 😎 𝖭𝖺𝗆𝖾 : {}</b>
<b>⪼ ♻️ 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : @{}</b>

<b>⪼ 🍃 𝖡𝗈𝗍 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 : @{}</b> """   

    CUSTOM_FILE_CAPTION = """<b><code>{file_name}</code></b>
   
  ◽️[𝐌𝐨𝐯𝐢𝐞 𝐆𝐫𝐨𝐮𝐩](https://t.me/Mallu_Movie_Hub_Group)  
  ◽️[𝐁𝐚𝐜𝐤𝐮𝐩 𝐆𝐫𝐨𝐮𝐩](https://t.me/+iEbhY7mM4oE1OTVl)
  ◽️[𝐎𝐭𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥](https://t.me/cinema_flix_updates)  
   ♡ ㅤ    ❍ㅤ     ⎙      ⌲
  ᶦᵏᵉ   ᶜᵒᵐᵐᵉⁿᵗ   ˢᵃᵛᵉ  ˢʰᵃʳᵉ</b>"""

    HOWTOUES_TXT = """<b>‼️ <u>Instructions</u> ‼️</b>

<b>How to add me in your group?</b>

• Copy my username or Click on add Group » Go to your Group administrator settings » Click Add admin » Give all permissions » Click tick mark » Done
• Then use /connect command in your group
• Connected Successfully I Will Provide Films In Your Group

<b>‼️ <u>നിർദ്ദേശങ്ങൾ</u> ‼️</b>

<b>നിങ്ങളുടെ ഗ്രൂപ്പിൽ എന്നെ എങ്ങനെ ചേർക്കാം?</b>

• എന്റെ ഉപയോക്തൃനാമം പകർത്തുക അല്ലെങ്കിൽ ആഡ് ഗ്രൂപ്പ് ക്ലിക്ക് ചെയ്യുക » നിങ്ങളുടെ ഗ്രൂപ്പ് അഡ്മിനിസ്ട്രേറ്റർ ക്രമീകരണങ്ങളിലേക്ക് പോകുക » അഡ്മിനെ ചേർക്കുക ക്ലിക്ക് ചെയ്യുക » എല്ലാ അനുമതികളും നൽകുക » ടിക്ക് മാർക്ക് ക്ലിക്ക് ചെയ്യുക » പൂർത്തിയായി
• തുടർന്ന് നിങ്ങളുടെ ഗ്രൂപ്പിൽ /connect കമാൻഡ് ഉപയോഗിക്കുക
• വിജയകരം നിങ്ങളുടെ ഗ്രൂപ്പ് അംഗങ്ങൾക്കായി ഞാൻ സിനിമകൾ നൽകുന്നതാണ്"""
    
    
