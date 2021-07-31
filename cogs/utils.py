from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @cog_ext.cog_slash(name="contribute", description="here's the repo link to contribute to pride bot!")
    async def contribute(self, ctx):
        #todo add a dm message with the tree structure of this repo
        await ctx.send(content="Want to make Pridebot even better? Feel free to contribute at https://github.com/tyffical/Pridebot <a:partyblahaj:828802809565675570>", hidden=True)
    
    @cog_ext.cog_slash(name="afk", description="set your afk status so that it will show up when you're tagged", 
    options=[create_option(
            name="reason",
            description="Why will you be afk?",
            option_type=3, #corresponds to STRING
            required=False)
        ])
    async def afk(self, ctx, reason = "They didn't leave a reason!"):
        if ctx.author in self.client.afkdict:
            self.client.afkdict.pop(ctx.author)
            await ctx.send('Welcome back! You are no longer afk.', hidden=True)
        else:
            self.client.afkdict[ctx.author] = reason
            await ctx.send(content="You are now afk. Beware of the real world!", hidden=True)

def setup(bot):
    bot.add_cog(Utils(bot))