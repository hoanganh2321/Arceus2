import discord
from discord.ext import commands
import requests

BotToken = 'MTE1ODMxMTY0NDYzNjY0NzQzNA.GTNJS3.mS7d55vtwdJXD9RYdgNKwGfPxyfgPJjXHKpsHY'
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("==========================")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="StickX"))

@bot.command(name="key", description="Bypass Fluxus Key For Your")
async def fluxus(ctx, link: str):
    hwid = link.split("HWID=")[-1]
    url = f"https://stickx.top/api-fluxus/?hwid={hwid}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        await ctx.reply(f"{data['key']}")
    else:
        print(f"Failed to retrieve data from API with status code {response.status_code}")
        await ctx.reply(f"Failed to retrieve data from API with status code {response.status_code}") 

bot.run(BotToken)