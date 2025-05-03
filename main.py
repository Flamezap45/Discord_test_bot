import discord
from discord.ext import commands
from webserver import start_server
from threading import Thread
import os

# starts the webserver
Thread(target=start_server).start()

# defines discord intentions
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# defines bot command prefix 
bot = commands.Bot(command_prefix='!', intents=intents)

# prints when the bot is ready
@bot.event
async def on_ready(): 
  print(f"Logged in as {bot.user}")

# ping command
@bot.command()
async def ping(ctx):
  await ctx.send('pong')

bot.run(os.environ['DISCORD_TOKEN'])