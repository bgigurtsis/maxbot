# bot.py
import os
import re

import discord

from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
# function to check for regex matching a url
async def on_message(message):

    emoji = '<:timeout2:806320653451001856>'
    regex = re.compile('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')
    match = regex.search(message.content)#

    if message.author.bot:
        return
    elif message.author.id == 389104618099048468 and match or message.attachments: 
        await message.add_reaction(emoji)

client.run(os.getenv('TOKEN'))


