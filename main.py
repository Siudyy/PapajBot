import os
import json
import random
import asyncio
from typing import Final
from dotenv import load_dotenv
from nextcord import Intents
from nextcord.ext import commands
from datetime import datetime, timedelta


load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

links = json.load(open("Storage.json"))

@bot.command(name="kremowka")
async def SendMessage(ctx):
    await ctx.send("Jeszcze Jak!")

@bot.command(name="2137")
async def Papajowa(ctx):
    await ctx.send(random.choice(links["storage"]))
    
async def daily_2137():
    while True:
        now = datetime.now()
        then = now + timedelta(days=1)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)
        channel = bot.get_channel(1284164179586056232)
        await channel.send(random.choice(links["storage"]))
        
@bot.event
async def on_ready():
    print("PAPIEŻO BOT")
    await daily_2137()

async def daily_2137():
    while True:
        now = datetime.now().replace(second=0, microsecond=0)
        then = now.replace(hour=21, minute=37, second=0, microsecond=0)
        wait_time = (then-now).total_seconds()
        
        if wait_time < 0:
            wait_time += timedelta(days=1).total_seconds()

        await asyncio.sleep(wait_time)
        channel = bot.get_channel(1284164179586056232)
        await channel.send(random.choice(links["storage"]))
        await asyncio.sleep(120)

if __name__ == "__main__":
    bot.run(token=TOKEN)
