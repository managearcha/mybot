from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='delete_my_data')
    async def delete_my_data(self, ctx):
        """The command used to clear all of your data from the bot."""
        # ...existing code...
        pass

    @commands.command(name='donate')
    async def donate(self, ctx):
        """Shares a link to donate to the bot"""
        # ...existing code...
        pass

    @commands.command(name='help')
    async def help(self, ctx, command_name: str = None):
        """Show the help for all the commands available in the bot"""
        # ...existing code...
        pass

    @commands.command(name='invite')
    async def invite(self, ctx):
        """Shares the details of how to add the bot"""
        # ...existing code...
        pass

    @commands.command(name='stats')
    async def stats(self, ctx):
        """Shows a selection of bot stats including ping, player count, guild count etc."""
        # ...existing code...
        pass

    @commands.command(name='support')
    async def support(self, ctx):
        """Shares a link to the support server"""
        # ...existing code...
        pass

async def setup(bot):
    await bot.add_cog(Help(bot))
