from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down.")
        await self.bot.close()

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.send(msg)

    @commands.command()
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Cleared {amount} messages", delete_after=3)

async def setup(bot):
    await bot.add_cog(Admin(bot))