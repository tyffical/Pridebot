import discord
import os
from keep_alive import keep_alive
# from dotenv import load_dotenv
# load_dotenv('---.env')
# emoji info https://gist.github.com/scragly/b8d20aece2d058c8c601b44a689a47a0
# discord.py docs https://discordpy.readthedocs.io/en/latest/api.html
# emoji codes https://emojiterra.com/rainbow/
# keeping bot alive on repl.it https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz
# change bot status https://python.plainenglish.io/how-to-change-discord-bot-status-with-discord-py-39219c8fceea
# "run on repl.it" button https://replit.com/talk/learn/Configuring-GitHub-repos-to-run-on-Replit-and-contributing-back/23948


client = discord.Client()

words = ["pride", "proud", "rainbow", "gay", "queer", "lgbt", "love", "june", "heart", "jack"]

#TODO: refactor emojis to two lists: default (unicode) and custom (Emoji objects)
#TODO: get emojis from other servers using nqn (send message with command in order to use nqn to react)
emoji_list = ["rainbow_flag", "prideblahaj", "rainbow", "partyblahaj", "justblahaj", "blahajyeet", "rip", "melonblahaj", "ryancoin"]
emoji_map = {}



proud_friendo_role_id = 849425044345716756

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    for emoji in emoji_list:
        emoji_map[emoji] = discord.utils.get(client.emojis, name=emoji)
    await client.change_presence(activity=discord.Game("Happy Pride Month! " + "\U0001f3f3\uFE0F\u200D\U0001f308"))

@client.event 
async def on_message(message): 
    string = "".join(message.content.lower().split()) #strip whitespace
    for word in words:
        if word in string:
            await message.add_reaction("\U0001f3f3\uFE0F\u200D\U0001f308") #rainbow flag emoji
            await message.add_reaction(emoji_map["prideblahaj"])
            #TODO: check if bot/"User" object instead of "Member", no roles for them
            for role in message.author.roles:
                if role.id == proud_friendo_role_id:
                    await message.add_reaction("\U0001f308") #rainbow emoji
                    await message.add_reaction(emoji_map["partyblahaj"])
            break
    
    if "blahaj" in string:
        await message.add_reaction(emoji_map["justblahaj"])
    
    if "yeet" in string:
        #TODO: yeets with an arbitrary number of e's (same for gaaaay)
        await message.add_reaction(emoji_map["blahajyeet"])

    if "rip" in string:
        await message.add_reaction(emoji_map["rip"])

    if "melon" in string:
        await message.add_reaction(emoji_map["melonblahaj"])
    
    if "ryan" in string:
        await message.add_reaction(emoji_map["ryancoin"])
    
    #per neel's request
    if "space" in string or "innovation" in string or "motivation" in string:
        await message.add_reaction("\U0001f680") #rocket emoji

    #per hana's request
    if "hana" in string:
        await message.add_reaction("\u2728") #sparkles emoji

keep_alive()
client.run(os.getenv('TOKEN'))
