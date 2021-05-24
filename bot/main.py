#bot.py
import os

import discord
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'hello':
        tz = pytz.timezone('Europe/Paris')
        fmt = '%H:%M'
        timeNow = datetime.now(tz)
        if timeNow.hour > 0 and timeNow.hour < 6:
            await message.channel.send('It is ' + f'{timeNow.strftime(fmt)}' + ' <@' + f'{message.author.id}' + '>' + ' why arent you sleeping?' )
        else:
            return

client.run(TOKEN)