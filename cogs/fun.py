import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="hug", description="everyone needs a hug once in a while <3", 
    options=[create_option(
            name="recipient",
            description="Whom do you want to hug?",
            option_type=6, #corresponds to USER
            required=False),
            create_option(
            name="reason",
            description="Why do you want to hug them?",
            option_type=3, #corresponds to STRING
            required=False)
            ])
    async def hug(self, ctx, recipient=None, reason=None):
        mention = recipient.id if recipient else None
        myid = ctx.author_id 
        if not reason:
            reason = "no reason, you simply deserve it. yeet"
        if not mention:
            await ctx.send(content="Who do you want to hug?")
        elif mention == myid:
            await ctx.send(content="Does someone need a hug? [*source* <https://www.youtube.com/watch?v=TIMj0s5dvpA>]")
        else:
            await ctx.send("<@{mention}> Everbody needs a hug. It changes your metabolism:\n Reason: {reason}".format(
                mention=mention, reason=reason),
                file=discord.File('./images/hug.gif'))
                
    @cog_ext.cog_slash(name="arrest", description="for some reason blahajgangers wanted to arrest one another?", 
    options=[create_option(
            name="recipient",
            description="Whom do you want to arrest?",
            option_type=6, #corresponds to USER
            required=False),
            create_option(
            name="reason",
            description="Why should they be arrested?",
            option_type=3, #corresponds to STRING
            required=False)
            ])
    async def arrest(self, ctx, recipient=None, reason=None):
        mention = recipient.id if recipient else None
        myid = ctx.author_id 
        if not reason:
            reason = "yeet! just for fun :)"
        if not mention:
            await ctx.send(content="Whom should I arrest?")
        elif mention == myid:
            await ctx.send(content="Ha! you can't arrest yourself.")
        else:
            await ctx.send(
                content="<@{mention}>, You're under arrest! \n reason: {reason}".format(
                    mention=mention, reason=reason))
            
    @cog_ext.cog_slash(name="yeet", description="yeet someone... you know you want to", 
    options=[create_option(
            name="recipient",
            description="Who do you want to yeet?",
            option_type=6, #corresponds to USER
            required=False),
            create_option(
            name="reason",
            description="Why do you want to yeet them?",
            option_type=3, #corresponds to STRING
            required=False)
            ])
    async def yeet(self, ctx, recipient=None, reason=None):
        mention = recipient.id if recipient else None
        myid = ctx.author_id 
        if not reason:
            reason = "'Not every yeet has a reason' - Blahajamin Franklin"
        if not mention:
            await ctx.send(content="Okay, but who do you want to yeet?")
        elif mention == myid:
            await ctx.send(content="You yeet yourself. Congratulations, you played yourself...")
        else:
            await ctx.send("<@{mention}> ya been yeeted, friendo! Enjoy the flight!\n Reason: {reason}".format(
                mention=mention, reason=reason),
                file=discord.File('./images/yeet-rafiki.gif'))

    @cog_ext.cog_slash(name="elmoash", description="gif of ash morphing into elmo")
    async def elmoash(self, ctx):
        await ctx.send(content="https://tenor.com/view/ashwin-rise-elmo-meme-lord-rise-ashwin-meme-lord-rise-gif-22312460")
        
    @cog_ext.cog_slash(name="whereismyblahaj", description="find your blahaj (great ad for a dating site)")
    async def whereismyblahaj(self, ctx):
        mention = ctx.author_id
        await ctx.send("<@{mention}> I found your Blahaj but you may not like where it is...".format(mention=mention), file=discord.File('./images/WHEREISMYBLAHAJ.png'))

def setup(bot):
    bot.add_cog(Fun(bot))
