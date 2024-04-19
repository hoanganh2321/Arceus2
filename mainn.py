import discord
from discord.ext import commands
import requests

BotToken = ' MTIzMDgyMjMwNTg3NDA1MTEwMw.Gf_fGg.IMBRy_V-BDsU9730n5En9hAEV7RE25w4fkqAzI '
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("==========================")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Code by Kaioshin"))

@bot.command(name="key", description="Bypass arceusx Key For Your")
async def fluxus(ctx, link: str):
    hwid = link.split("hwid=")[-1].split("&")[0]  
    
    url = f"https://stickx.top/api-arceusx/?hwid={hwid}&api_key=E99l9NOctud3vmu6bPne"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        await ctx.reply(f" > # _ {data['key']}_")
        
    else:
        print(f"Failed to retrieve data from API with status code {response.status_code}")
        await ctx.reply(f"Failed to retrieve data from API with status code {response.status_code}") 

bot.run(BotToken)
