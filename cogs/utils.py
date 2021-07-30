from discord.ext import commands
from discord_slash import cog_ext

from info.ids import guild_ids
guild_ids_list = [guild_ids["blahajgang"]]

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @cog_ext.cog_slash(name="contribute", guild_ids=guild_ids_list, description="here's the repo link to contribute to pride bot!")
    async def contribute(self, ctx):
        #todo add a dm message with the tree structure of this repo
        await ctx.send(content="Want to make Pridebot even better? Feel free to contribute at https://github.com/tyffical/Pridebot <a:partyblahaj:828802809565675570>")

def setup(bot):
    bot.add_cog(Utils(bot))