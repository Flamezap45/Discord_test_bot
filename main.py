import discord
from discord.ext import commands
from webserver import keep_alive  # Import the correct function
import os

# Start Flask server (critical for Koyeb health checks)
keep_alive()  # Uses the renamed `run()` function from webserver.py

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(os.environ['DISCORD_TOKEN'])