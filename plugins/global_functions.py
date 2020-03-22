from collections import defaultdict
from random import random
import inspect
import logging
import asyncio
import time


# Logging
async def log(event, info=""):
    sender = await event.get_sender()
    # Get the name of the command sent to the bot:
    command = inspect.currentframe().f_back.f_code.co_name
    logging.info(
        f"""[{event.date.strftime('%c')}]:
    [{sender.id}]@[{event.chat_id}] {sender.first_name}@{sender.username}: {command}
    {info}""".rstrip())
