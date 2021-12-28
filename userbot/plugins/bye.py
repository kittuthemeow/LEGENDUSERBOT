import asyncio
from userbot.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from . import *
@bot.on(admin_cmd(pattern="byeall"))
async def _(event):
	await event.edit("ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ᴄʜᴜᴄᴋʏ sᴇʀᴠᴇʀ")
	await asyncio.sleep(3)
	await event.edit("""
╭━━┳╮╱╱╭┳━━━┳━━━┳╮╱╱╭╮
┃╭╮┃╰╮╭╯┃╭━━┫╭━╮┃┃╱╱┃┃
┃╰╯╰╮╰╯╭┫╰━━┫┃╱┃┃┃╱╱┃┃
┃╭━╮┣╮╭╯┃╭━━┫╰━╯┃┃╱╭┫┃╱╭╮
┃╰━╯┃┃┃╱┃╰━━┫╭━╮┃╰━╯┃╰━╯┃
╰━━━╯╰╯╱╰━━━┻╯╱╰┻━━━┻━━━╯
       [⚡️ᴛʜᴇ ᴋɪᴛᴛᴜ ᴘʀᴏ ⚡️](https://t.me/chucky_support)
""")
CmdHelp("byeall").add_command(
	'byeall', None, 'Say Bye to U all in anmation'
).add()
