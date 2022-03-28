import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**ɪᴍ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ʙᴏᴛ**,\nɪ ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇʟ ⚡\nCʟɪᴄᴋ /help ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.",
                    buttons=(
                      [Button.url('👥 ᴍʏ ɢʀᴏᴜᴘ', 'https://t.me/Music_Galaxy_Dl'),
                      Button.url('➕ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ➕', 'http://t.me/Mentionalltgtbot?startgroup=true')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ ᴍᴇɴᴛɪᴏɴᴀʟʟʙᴏᴛ**\n\nCᴏᴍᴍᴀɴᴅ: /all\nYᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.\n**Example:** `/all Good Night 🌃!`\nYᴏᴜ ᴄᴀɴ ᴅᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ.\nBᴏᴛ ᴡɪʟʟ ᴛᴀɢ ᴜsᴇʀs ᴛᴏ ᴛʜᴀᴛ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ.\n\n🌟 Bot maintained by: @HydraLivegrambot\n⭐⭐Bot Creator: <a href="https://github.com/AnjanaMadu">Code Owner</a>"
  await event.reply(helptext, 
                    buttons=(
                      [Button.url('📢 Channel', 'https://t.me/Tg_Galaxy'),
                      Button.url('👥 ɢʀᴏᴜᴘ', 'https://t.me/music_Galaxy_dl')]
                    ),
                    link_preview=False
                   )
  
@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  if event.is_private:
    return await event.respond("Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ʙᴇ ᴜsᴇ ɪɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Oɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ! 😁")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("I ᴄᴀɴ'ᴛ ᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ғᴏʀ ᴏʟᴅᴇʀ ᴍᴇssᴀɢᴇs! (messages which sended before i added to group)")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Give me one argument!__")
  else:
    return await event.respond("Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴍᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs!")
  
  if mode == "text_on_cmd":
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
print(">> BOT STARTED <<")
client.run_until_disconnected()
