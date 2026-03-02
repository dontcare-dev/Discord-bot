from discord.ext import commands

class Massive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def generate_command(i):
        async def cmd(self, ctx):
            await ctx.send(f"Command {i} executed")
        return cmd

# Create 100 commands automatically
for i in range(1, 101):
    setattr(
        Massive,
        f"cmd{i}",
        commands.command(name=f"cmd{i}")(generate_command(i))
    )

async def setup(bot):
    await bot.add_cog(Massive(bot))