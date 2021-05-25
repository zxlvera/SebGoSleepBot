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
    
    if message.author.id == '772254027656200222':
        tz = pytz.timezone('Europe/Paris')
        fmt = '%H:%M'
        timeNow = datetime.now(tz)
        if timeNow.hour > 0 and timeNow.hour < 6:
            await message.channel.send('It is ' + f'{timeNow.strftime(fmt)}' + ' <@' + f'{message.author.id}' + '>' + ' why arent you sleeping?' )
        else:
            return

    if message.content.lower() == 'oui':
        number_res = 4
        emojis = ["🇫🇷", "🥖", "🥐", "🍷"]
        for i in range(number_res):
            await message.add_reaction(emojis[i])

client.run(TOKEN)
