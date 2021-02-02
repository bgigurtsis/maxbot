# bot.py
import os
import discord
import io 
import aiohttp

from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event

#function to check for regex matching a url
def match_url(url):
       regex = re.compile(
           "(([\w]+:)?//)?(([\d\w]|%[a-fA-f\d]{2,2})+(:([\d\w]|%[a-fA-f\d]{2,2})+)?@)?([\d\w][-\d\w]{0,253}[\d\w]\.)+[\w]{2,63}(:[\d]+)?(/([-+_~.\d\w]|%[a-fA-f\d]{2,2})*)*(\?(&?([-+_~.\d\w]|%[a-fA-f\d]{2,2})=?)*)?(#([-+_~.\d\w]|%[a-fA-f\d]{2,2})*)?"
       )
       if regex.match(url):
           return True
       else:
           return False

async def on_message(message):

	#check for max's user id and if the message match's the above regex
	if message.id == 389104618099048468 and match_url(message) = true:

		#download the image and send it, it's much easier if you upload the image from your pc vs from a url
		async with aiohttp.ClientSession() as session:
    		async with session.get(https://i.imgur.com/XHBa71T.jpg) as resp:
        		if resp.status != 200:
            		return await channel.send('Could not download file...')
        		data = io.BytesIO(await resp.read())
        		await channel.send(file=discord.File(data, 'bitch.png'))

client.run(os.getenv('TOKEN'))