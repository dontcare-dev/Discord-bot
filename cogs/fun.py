from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        await ctx.send(random.choice(["Heads", "Tails"]))

    @commands.command()
    async def dice(self, ctx):
        await ctx.send(random.randint(1, 6))

    @commands.command()
    async def joke(self, ctx):
        jokes = ["Why did the bot crash? Too many commands."]
        await ctx.send(random.choice(jokes))

async def setup(bot):
    await bot.add_cog(Fun(bot))