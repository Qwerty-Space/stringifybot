"""Sends the output of new message events and certain entities via [telethon](https://github.com/LonamiWebs/Telethon).
Formatted using [bprint](https://github.com/Lonami/bprint)
"""

import re
from bprint import bprint
from .global_functions import log

from telethon import events
from telethon.utils import add_surrogate
import telethon.tl.types as types


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

@events.register(events.NewMessage())
async def stringfy_message(event):
    await log(event)

    msg = event.message
    entities = event.entities
    output = [msg]

    if entities:
        mentions = list()
        mention = None
        for e in entities:
            if isinstance(e, types.MessageEntityMention):
                e_start = e.offset
                e_end = e_start + e.length
                mention = msg.raw_text[e_start:e_end]
            if isinstance(e, types.MessageEntityMentionName):
                mention = e.user_id

            if not mention:
                continue

            received_entity = await event.client.get_entity(mention)
            output.append(received_entity)

    yaml_text = str()
    for l in output:
        skip = Skip()
        yaml_text += bprint(l, stream=str,
                        max_str_len=64, max_bytes_len=64,
                        indent="  ", skip_predicate=skip,
                        maximum_depth=4, inline_singular=True
                    )
    sub = re.sub(r"(?m)\n^(\s+).+:$(?!\n?\1\s)$", "", yaml_text)

    await event.reply(sub, parse_mode=parse_pre)
