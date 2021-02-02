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
    def match_url(url):
        regex = re.compile(
            "(([\w]+:)?//)?(([\d\w]|%[a-fA-f\d]{2,2})+(:([\d\w]|%[a-fA-f\d]{2,2})+)?@)?([\d\w][-\d\w]{0,253}[\d\w]\.)+[\w]{2,63}(:[\d]+)?(/([-+_~.\d\w]|%[a-fA-f\d]{2,2})*)*(\?(&?([-+_~.\d\w]|%[a-fA-f\d]{2,2})=?)*)?(#([-+_~.\d\w]|%[a-fA-f\d]{2,2})*)?","",str()
        )
        if regex.match(url):
            return True
        else:
            return False
    # check for max's user id and if the message match's the above regex
    if message.author.id == 143161331866927104:
        print('test condition 1')
        if match_url(message):
            print('test condition 2')
            await discord.channel.send(file=discord.File('bitch.jpg'))

client.run(os.getenv('TOKEN'))
