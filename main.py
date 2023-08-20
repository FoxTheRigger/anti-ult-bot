# Bro tried to flex his steam games on me lmao
import discord
from discord.ext import commands

token = " " # Add your bot token
ult = "ULT'S ID" # without the " "  

bot = commands.Bot(command_prefix="ult!", intents=discord.Intents.all()) 

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}, ready to attack ult')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="TELLING ULT TO STFU"))

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    if message.author.id == ult:
        await message.channel.send(f'{message.author.mention} STFU!') # The message you want your bot to send
        await message.delete() # Delete his messages to annoy him

    await bot.process_commands(message)

bot.run(token)