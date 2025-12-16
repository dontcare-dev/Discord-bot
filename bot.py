import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

bot.run(os.getenv("MTQ1MDQzMDQ3Nzk2OTEzMzc0NQ.GpnHfj.sm62w4hVmmPO7tbp4wxuKEMwLKQISkNBgY-ACw"))
