from discord.ext import commands
import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uptime(self, ctx):
        await ctx.send("Bot is running.")

    @commands.command()
    async def serverinfo(self, ctx):
        await ctx.send(ctx.guild.name)

    @commands.command()
    async def userinfo(self, ctx):
        await ctx.send(ctx.author.name)

async def setup(bot):
    await bot.add_cog(Utility(bot))