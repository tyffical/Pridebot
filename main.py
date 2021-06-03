import discord
import os
from keep_alive import keep_alive
# from dotenv import load_dotenv
# load_dotenv('---.env')
# emoji info https://gist.github.com/scragly/b8d20aece2d058c8c601b44a689a47a0
# discord.py docs https://discordpy.readthedocs.io/en/latest/api.html
# emoji codes https://emojiterra.com/
# keeping bot alive on repl.it https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz
# change bot status https://python.plainenglish.io/how-to-change-discord-bot-status-with-discord-py-39219c8fceea
# "run on repl.it" button https://replit.com/talk/learn/Configuring-GitHub-repos-to-run-on-Replit-and-contributing-back/23948

#global vars

client = discord.Client()

pride_words = ["pride", "proud", "rainbow", "gay", "queer", "lgbt", "love", "june", "heart", "jack"]

proud_friendo_role_id = 849425044345716756 #for helpful allies

#emojis

#default -> unicode (see https://emojiterra.com for codes)
default_list = ["rainbow_flag", "rainbow", "rocket", "sparkles"]
default_map = {"rainbow_flag": "\U0001f3f3\uFE0F\u200D\U0001f308", "rainbow": "\U0001f308", "rocket": "\U0001f680", "sparkles": "\u2728"}
#TODO: find a way to automate getting the unicodes

#custom -> discord.Emoji objects
custom_list = ["prideblahaj", "partyblahaj", "justblahaj", "blahajyeet", "rip", "melonblahaj", "ryancoin"]
custom_map = {}

#nqn -> custom emojis from other servers using NotQuiteNitro bot (can be done by sending a message with !react <emoji_name>)
nqn_list = ["elonsmoke", "meow_coffee", "catclown", "LMAO", "crii", "blobdance", "meow_code", "meow_heart", "3c"]
nqn_msg = "!react :{}:"

#actual bot functions

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    for emoji in custom_list:
        custom_map[emoji] = discord.utils.get(client.emojis, name=emoji)
    await client.change_presence(activity=discord.Game("Happy Pride Month! " + default_map["rainbow_flag"]))

@client.event 
async def on_message(message): 
    #ignore bot's own message
    if message.author.id == client.user.id:
      return

    string = "".join(message.content.lower().split()) #strip whitespace
    for word in pride_words:
        if word in string:
            await message.add_reaction(default_map["rainbow_flag"])
            await message.add_reaction(custom_map["prideblahaj"])
            #TODO: check if bot/"User" object instead of "Member", no roles for them
            for role in message.author.roles:
                if role.id == proud_friendo_role_id:
                    await message.add_reaction(default_map["rainbow"])
                    await message.add_reaction(custom_map["partyblahaj"])
            break
    
    if "blahaj" in string:
        await message.add_reaction(custom_map["justblahaj"])
    
    if "yeet" in string:
        #TODO: yeets with an arbitrary number of e's (same for gaaaay)
        await message.add_reaction(custom_map["blahajyeet"])

    if "rip" in string:
        await message.add_reaction(custom_map["rip"])

    if "melon" in string:
        await message.add_reaction(custom_map["melonblahaj"])
    
    if "ryan" in string:
        await message.add_reaction(custom_map["ryancoin"])
    
    #per neel's request
    if "space" in string or "innovation" in string or "motivation" in string:
        await message.add_reaction(default_map["rocket"])
    if "elon" in string:
        await message.reply(nqn_msg.format("elonsmoke"))
    if "coffee" in string:
        await message.reply(nqn_msg.format("meow_coffee"))
    if "clown" in string:
        await message.reply(nqn_msg.format("catclown"))
    if "lmao" in string:
        await message.reply(nqn_msg.format("LMAO"))
    if "cry" in string or "cri" in string:
        await message.reply(nqn_msg.format("crii"))
    if "dance" in string:
        await message.reply(nqn_msg.format("blobdance"))

    #per hana's request
    if "hana" in string:
        await message.add_reaction(default_map["sparkles"]) 

    #tiffany having fun
    if "code" in string or "hack" in string:
        await message.reply(nqn_msg.format("meow_code"))
    if "cat" in string or "kitty" in string or "meow" in string:
        await message.reply(nqn_msg.format("meow_heart"))
    if "tiff" in string:
        await message.reply(nqn_msg.format("3c"))

keep_alive()
client.run(os.getenv('TOKEN'))
