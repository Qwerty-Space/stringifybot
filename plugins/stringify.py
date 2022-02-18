from bprint import bprint

from telethon import events
from telethon.utils import add_surrogate, del_surrogate
import telethon.tl.types as types

from bepis_bot.runtime import client


def parse_pre(text):
  text = text.strip()
  return (
    text,
    [types.MessageEntityPre(offset=0, length=len(add_surrogate(text)), language='')]
  )

class Skip:
  def __init__(self):
    self.items = set()

  def __call__(self, key, val):
    if key.startswith('_') or callable(val):
      return True
    if key in {"CONSTRUCTOR_ID", "SUBCLASS_OF_ID", "FileLocationToBeDeprecated"}:
      return True
    if not val and key not in ["length", "offset", "user_id"]:
      return True

    if key in self.items:
      return True

    if not key in ["length", "offset", "user_id"]:
      self.items.add(key)

    return False

@client.on(events.NewMessage())
async def stringfy_message(event):
  msg = event.message
  output = [msg]

  raw_text = add_surrogate(msg.raw_text)
  for e in (event.entities or []):
    mention = None
    if isinstance(e, types.MessageEntityMention):
      mention = del_surrogate(raw_text[e.offset:e.offset + e.length])
    if isinstance(e, types.MessageEntityMentionName):
      mention = e.user_id

    if not mention:
      continue

    try:
      received_entity = await event.client.get_entity(mention)
    except:
      continue
    output.append(received_entity)

  yaml_text = str()
  for l in output:
    skip = Skip()
    yaml_text += bprint(
      l,
      stream=str,
      max_str_len=64,
      max_bytes_len=64,
      indent="  ",
      skip_predicate=skip,
      maximum_depth=4,
      inline_singular=True,
      skip_cyclic=False
    )

  await event.reply(yaml_text, parse_mode=parse_pre)
