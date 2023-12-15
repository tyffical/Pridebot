import discord
from discord import option
from discord.ext import commands


class Fun(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(name="hug",
                          description="everyone needs a hug once in a while <3"
                          )
  @option("recipient",
          discord.User,
          description="Whom do you want to hug?",
          required=False)
  @option("reason", description="Why do you want to hug them?", required=False)
  async def hug(self, ctx: discord.ApplicationContext,
                recipient: discord.Member, reason: str):
    mention = recipient.id if recipient else None
    if not reason:
      reason = "no reason, you simply deserve it. yeet"
    if not mention:
      await ctx.send_response(content="Who do you want to hug?")
    elif mention == ctx.author.id:
      await ctx.send_response(
          content=
          "Does someone need a hug? [*source* <https://www.youtube.com/watch?v=TIMj0s5dvpA>]"
      )
    else:
      await ctx.send_response(
          "<@{mention}> Everbody needs a hug. It changes your metabolism:\n Reason: {reason}"
          .format(mention=mention, reason=reason),
          file=discord.File('images/hug.gif')
      )  # change this back to the right gif at some point

  @commands.slash_command(name="yeet",
                          description="yeet someone... you know you want to")
  @option("recipient",
          discord.User,
          description="Who do you want to yeet?",
          required=False)
  @option("reason",
          description="Why do you want to yeet them?",
          required=False)
  async def yeet(self, ctx: discord.ApplicationContext,
                 recipient: discord.Member, reason: str):
    mention = recipient.id if recipient else None
    myid = ctx.author.id
    if not reason:
      reason = "'Not every yeet has a reason' - Blahajamin Franklin"
    if not mention:
      await ctx.send_response(content="Okay, but who do you want to yeet?")
    elif mention == myid:
      await ctx.send_response(
          content="You yeet yourself. Congratulations, you played yourself...")
    else:
      await ctx.send_response(
          "<@{mention}> ya been yeeted, friendo! Enjoy the flight!\n Reason: {reason}"
          .format(mention=mention, reason=reason),
          file=discord.File('./images/yeet-rafiki.gif'))


def setup(bot):
  bot.add_cog(Fun(bot))
