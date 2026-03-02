from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member, *, reason=None):
        await ctx.send(f"Kicked {member}")

    @commands.command()
    async def ban(self, ctx, member, *, reason=None):
        await ctx.send(f"Banned {member}")

    @commands.command()
    async def mute(self, ctx, member):
        await ctx.send(f"Muted {member}")

    @commands.command()
    async def warn(self, ctx, member, *, reason):
        await ctx.send(f"Warned {member}: {reason}")

async def setup(bot):
    await bot.add_cog(Moderation(bot))