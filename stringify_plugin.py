"""Sends the output of `events.message.stringify()`.
"""

import re
from telethon import events
from telethon.utils import add_surrogate
from telethon.tl.types import MessageEntityPre
from .global_functions import log


def parse_pre(text):
    """Custom parser that turns an entire message into a pre block"""
    text = text.strip()
    return (
        text,
        [MessageEntityPre(offset=0, length=len(add_surrogate(text)), language="")]
    )


@events.register(events.NewMessage(pattern=r"(?s)^(?!/(start|ping|help))(.+)?$", outgoing=False))
async def stringfy_message(event):
    if event.is_private:
        replied_msg = re.sub(r"(?<=.{100}).+", "...'", event.message.stringify())
        await event.reply(replied_msg, parse_mode=parse_pre)
        await log(event)
