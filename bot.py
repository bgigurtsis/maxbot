# bot.py
import os
import re

import discord

from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_message(messagetwo):
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

@client.event
# function to check for regex matching a url
async def on_message(message):
    # check for max's user id and if the message match's the above regex
    regex = re.compile('((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*')
    match = regex.search(message.content)#

    if message.author.bot:
        return
    elif message.author.id == 389104618099048468 and match or message.attachments:
        await message.channel.send(file=discord.File('bitch.jpg'))

client.run(os.getenv('TOKEN'))
