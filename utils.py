import discord
from discord import SlashCommand, option
from discord.ext import commands

import main


class Utils(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(
      name="contribute",
      description="here's the repo link to contribute to pride bot!")
  async def contribute(self, ctx: discord.ApplicationContext):
    #todo add a dm message with the tree structure of this repo
    await ctx.send_response(
        content=
        "Want to make Pridebot even better? Feel free to contribute at <https://github.com/tyffical/Pridebot> <a:partyblahaj:828802809565675570>"
    )

  @commands.slash_command(
      name="afk",
      description=
      "set your afk status so that it will show up when you're tagged")
  @option("reason", description="Why are you AFK?", required=False)
  async def afk(self,
                ctx: discord.ApplicationContext,
                reason: str = "No Reason Provided"):
    if ctx.author.id in main.afk_dict:
      main.afk_dict.pop(ctx.author.id)
      await ctx.send_response(content='Welcome back! You are no longer AFK.',
                              ephemeral=True)
    else:
      main.afk_dict[ctx.author.id] = reason
      await ctx.send_response(
          content="You are now AFK. Beware of the real world!", ephemeral=True)

  @commands.slash_command(
      name="help",
      description="Shows a list of all commands and what they do.")
  async def help(self, ctx: discord.ApplicationContext):
    embed = discord.Embed(
        title="Here are all the slash commands you can use with Pride Bot:")
    for command in self.bot.walk_application_commands():
      if type(command) == discord.SlashCommand:
        embed.add_field(name="/" + command.name,
                        value=command.description,
                        inline=False)
    await ctx.send_response(embed=embed, ephemeral=True)


def setup(bot):
  bot.add_cog(Utils(bot))
