import discord
import json
import os
import random
import re

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

global afk_dict
afk_dict = {}
custom_emoji = {}

bot = discord.Bot(intents=intents)
bot.load_extension("fun")
bot.load_extension("utils")

with open('guilds.json') as f:
  guilds = json.load(f)

with open('roles.json') as f:
  roles = json.load(f)


@bot.event
async def on_ready():
  print(f"Logged in as {bot.user} (ID: {bot.user.id if bot.user else None})")
  print("------")

  async for guild in bot.fetch_guilds(limit=10):
    full_guild = bot.get_guild(guild.id)
    if full_guild:
      for emoji in full_guild.emojis:
        custom_emoji[emoji.name] = emoji

  game = discord.Game("Happy Pride! 🏳️‍🌈")
  await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_message(message: discord.Message):
  if bot.user and message.author.id == bot.user.id:
    return
  if message.guild is None:
    return

  member = message.guild.get_member(message.author.id)
  words = re.split(r"[,:. \"'-]+", message.content.lower())
  afk_dict = globals()["afk_dict"]

  # AFK Member Handling
  if message.author.id in afk_dict:
    await message.reply("Welcome back! You are no longer AFK.")
    afk_dict.pop(message.author.id)
  for member in message.mentions:
    if member != message.author and member.id in afk_dict:
      await message.reply(
          content=
          f"{member.mention} is currently AFK: **{afk_dict[member.id]}**",
          delete_after=20)

  # Pridebot responding to a mention of its name aka 'the hotword'
  responses = [
      "hey homie", "sup mate?", "why'd you summon me, mate?",
      "sorry, im busy atm"
  ]
  if "pridebot" in "".join(words):
    await message.reply(responses[random.randint(0, 3)])

  # Responding to pride words
  pride_words = [
      "pride", "proud", "rainbow", "gay", "queer", "lgbt", "love", "june",
      "heart"
  ]

  for word in words:
    if word in pride_words:
      await message.add_reaction("🏳️‍🌈")
      await message.add_reaction(custom_emoji["gaydragon"])
      await message.add_reaction(custom_emoji["prideblahaj"])

      if (type(message.guild) is discord.Guild
          and message.guild.id == guilds["blahajgang"]
          and type(member) is discord.Member
          and member.get_role(roles["proud_friendo"]) is not None):
        await message.add_reaction("🌈")
        await message.add_reaction(custom_emoji["rainbowblahaj"])
        await message.add_reaction(custom_emoji["partyblahaj"])

  # React to different words with custom emoji
  word_reacts = {
      'yee+t': [custom_emoji["blahajyeet"]],
      'mindblowing': ["🤯"],
      'that\'scool': ["🤯"],
      'holyfruit': [custom_emoji["melonblahaj"]],
      'bequiet': ["🤫"],
      'shutup': ["🤫"],
      'neel': [custom_emoji["spaceblahaj"]],
      'tiff': [custom_emoji["royalblahaj"]],
      'blahaj': [custom_emoji["justblahaj"]],
      'shark': [custom_emoji["justblahaj"]],
      'uwu': [custom_emoji["blahajuwu"]],
      'sleep': ["🥱", "😴"],
      'ping': [custom_emoji["angrypinghaj"]],
      'coffee': [custom_emoji["meow_coffee"]],
      'clown': [custom_emoji["catclown"]],
      'dance': [custom_emoji["blobdance"]],
      'code': [custom_emoji["meow_code"]],
      'hack': [custom_emoji["meow_code"]],
      'cat': [custom_emoji["meow_heart"]],
      'kitty': [custom_emoji["meow_heart"]],
      'meow': [custom_emoji["meow_heart"]],
      'sus': [custom_emoji["susblahaj"]],
  }
  for regex, reacts in word_reacts.items():
    if re.search(regex, "".join(message.content.lower().split())) is not None:
      for react in reacts:
        await message.add_reaction(react)

  # identity-specific react map
  identity_reacts = {
      'trans': [custom_emoji["pride_heart_trans"]],
      'poc': [custom_emoji["pride_heart_pocpride"]],
      'pan': [custom_emoji["pride_heart_pan"]],
      'nonbinary': [custom_emoji["pride_heart_nonbinary"]],
      'nb': [custom_emoji["pride_heart_nonbinary"]],
      'lesbian': [custom_emoji["pride_heart_lesbian"]],
      'genderqueer': [custom_emoji["pride_heart_genderqueer"]],
      'gay': [custom_emoji["pride_heart_gay"]],
      'bi': [custom_emoji["pride_heart_bi"]],
      'aro': [custom_emoji["pride_heart_aro"]],
      'ace': [custom_emoji["pride_heart_ace"]],
      'asexual': [custom_emoji["pride_heart_ace"]]
  }

  for substr, reacts in identity_reacts.items():
    if substr in words:
      for react in reacts:
        await message.add_reaction(react)


token = os.environ['TOKEN']
bot.run(token)
