"""Sends the output of `events.message.stringify()`.
"""

import re
import datetime
from bprint import bprint
from .global_functions import log

from telethon import events
from telethon.utils import add_surrogate
from telethon.tl.tlobject import TLObject
import telethon.tl.types as types


class Skip:
    def __init__(self):
        self.items = set()

    def __call__(self, key, val):
        if not val:
            return True
        if key.startswith('_') or callable(val):
            return True
        # print(key, val)
        if key in {"CONSTRUCTOR_ID", "SUBCLASS_OF_ID", "FileLocationToBeDeprecated"}:
            return True
        if isinstance(val, (types.FileLocationToBeDeprecated, )):
            return True

        if key in self.items:
            return True
        self.items.add(key)

        return False

@events.register(events.NewMessage(outgoing=False))
async def stringfy_message(event):
    await log(event)

    msg = event.message
    skip = Skip()
    yaml_text = bprint(msg, stream=str,
                   max_str_len=64, max_bytes_len=64,
                   indent="  ", skip_predicate=skip,
                   maximum_depth=4, inline_singular=True
               )
    sub = re.sub(r"(?m)\n^(\s+).+:$(?!\n?\1\s)$", "", yaml_text)

    await event.reply(f"`{sub}`")
