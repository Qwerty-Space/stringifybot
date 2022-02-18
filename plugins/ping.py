import time

from telethon import events

from bepis_bot.runtime import client


@client.on(events.NewMessage(pattern=r'/ping$'))
async def ping(event):
  if event.is_private:
    start = time.time()
    message = await event.reply("**Pong!**")
    delta = time.time() - start
    await message.edit(f"**Pong!**\nTook `{delta:.3f}` seconds")
