import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import get_all_commands

import os, re, time, requests, random, time
from git import Repo

from dotenv import load_dotenv
load_dotenv()

from scripts.keep_alive import keep_alive

from data.ids import role_ids, channel_ids, guild_ids
from data.emojis import default_map, custom_list

# global vars
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

# response = requests.get("https://discord.com/oauth2/849471740052504606")
# remaining_requests = response.headers.get('X-RateLimit-Limit')
# print(remaining_requests)

# various dicts
custom_map = {}
times = {"last_cry_time": 0}

# define the afk dict as part of the client, so it can be accessed anywhere
client.afkdict = {}

#Defines the dictionary with Slashcommand Name:Description as key:value pairs(also as a part of the client)
client.better_commands = {}

# add cogs
client.load_extension("cogs.fun")
client.load_extension("cogs.gifts")
client.load_extension("cogs.utils")

# bot startup and status
@client.event
async def on_ready():
    #for the help command: getting the slashcommands name and description into the better_commands dictionary
    commands = await get_all_commands(client.user.id, os.getenv('TOKEN'))

    #iterating though commands to get name:description pairs
    for command in commands:
        client.better_commands[command["name"]] = command["description"]
    
    print("Bot is ready! Logged in as " + str(client.user))

    repo = Repo("./")
    if 'REPL_OWNER' in os.environ and os.environ['REPL_OWNER'] == "tyffical":
      host = "Production Repl.it Instance"
    else:
      host = "Local Development Instance"
    await client.get_channel(channel_ids["feed"]).send(f'''<a:partyblahaj:828802809565675570> SUCCESS! I'M ALIVEEEEEEEEEE <a:partyblahaj:828802809565675570>

**Started:** <t:{int(time.time())}:R> (<t:{int(time.time())}:F>)

**Current Environment:** {host}

**Current Commit:** `{repo.head.commit.author.name}` - `{repo.head.commit.message}`
''')

    for emoji in custom_list:
        custom_map[emoji] = discord.utils.get(client.emojis, name=emoji)
    client.blahajgang_guild = discord.utils.get(client.guilds, id=guild_ids["blahajgang"]) # BLAHAJGang 

    # Changes the bot's presence
    await client.change_presence(activity=discord.Game("Happy Pride! " + default_map["rainbow_flag"]))

    # Syncs global slash commands
    await slash.sync_all_commands()

# bot message reactions and replies
@client.event
async def on_message(message):
    # ignore bot's own message
    if message.author.id == client.user.id:
        return
    
    # afk stuff
    if message.author in client.afkdict:
        await message.channel.send("Welcome back! You are no longer afk.")
        client.afkdict.pop(message.author)
    for member in message.mentions:  
        if member != message.author and member in client.afkdict:  
            await message.reply(content=f"Oh noes! {member.mention} is currently AFK.\nReason: **{client.afkdict[member]}**", delete_after=20)
            await message.reply(content=f"This bitch afk. YEET [*source* <https://www.youtube.com/watch?v=2Bjy5YQ5xPc>]", delete_after=20)

    # split by spaces, commas, periods, etc to get the words in the string
    string = re.split(r"[,:. \"'-!\?]+", message.content.lower())
    
    #pridebot responding to a mention of its name aka 'the hotword'
    responses = ["hey homie", "sup mate?", "why'd you summon me, mate?", "sorry, im busy atm"]
    hotword = "".join(string) 
    if "pridebot" in hotword:
        r = requests.head(url="https://discord.com/api/v2/")
        try:
            await message.reply(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes until activity")
        except:
            await message.reply(responses[random.randint(0, 3)])

    # TODO: see if computer vision can be used to detect text or rainbows in images
    # general pride react map
    pride_words = ["pride", "proud", "rainbow", "gay", "queer", "lgbt", "love", "june", "heart", "jack"]

    for word in pride_words:
        if word in string:
            await message.add_reaction(default_map["rainbow_flag"])
            await message.add_reaction(custom_map["prideblahaj"])

            # check if author not "Member" (i.e. bot) -> they have no roles
            if not isinstance(message.author, discord.Member):
                break

            friendo_role = discord.utils.get(client.blahajgang_guild.roles, id=role_ids["proud_friendo"])
            if friendo_role in message.author.roles:
                # proud friendo gets extra reacts, per jack's request
                await message.add_reaction(default_map["rainbow"])
                await message.add_reaction(custom_map["rainbowblahaj"])
                await message.add_reaction(custom_map["partyblahaj"])

    # regex react map for whitespace-sensitive reactions
    regex_reacts = {
        'yee+t': [custom_map["blahajyeet"]],
        'partyisland:thevirtualexperience': [
            default_map["regional_indicator_p"],
            default_map["regional_indicator_a"],
            default_map["regional_indicator_r"],
            default_map["regional_indicator_t"],
            default_map["regional_indicator_y"],
            default_map["white_check_mark"],
            default_map["x"]
        ],
        'mindblowing': [default_map["exploding_head"]],
        'that\'scool': [default_map["exploding_head"]],
        'holyfruit': [custom_map["melonblahaj"]],
        'bequiet': [default_map["shushing_face"]],
        'shutup': [default_map["shushing_face"]],
    }
    for regex, reacts in regex_reacts.items():
        if re.search(regex, "".join(message.content.lower().split())) != None:
            for react in reacts:
                await message.add_reaction(react)

    # identity-specific react map
    identity_reacts = {
        'trans': [custom_map["pride_heart_trans"]],
        'poc': [custom_map["pride_heart_pocpride"]],
        'pan': [custom_map["pride_heart_pan"]],
        'nonbinary': [custom_map["pride_heart_nonbinary"]],
        'nb': [custom_map["pride_heart_nonbinary"]],
        'lesbian': [custom_map["pride_heart_lesbian"]],
        'genderqueer': [custom_map["pride_heart_genderqueer"]],
        'gay': [custom_map["pride_heart_gay"]],
        'bi': [custom_map["pride_heart_bi"]],
        'aro': [custom_map["pride_heart_aro"]],
        'ace': [custom_map["pride_heart_ace"]],
        'asexual': [custom_map["pride_heart_ace"]]
    }

    for substr, reacts in identity_reacts.items():
        if substr in string:
            for react in reacts:
                await message.add_reaction(react)
    
    # people-specific react map
    people_reacts = {
        'ryan': [custom_map["ryancoin"]],
        'neel': [custom_map["spaceblahaj"]],
        'vik': [custom_map["mlhblahaj"]],
        'electron': [default_map["zap"]],
        'bailey': [custom_map["awwblahaj"], default_map["flag_vn"]],
        'tiff': [custom_map["royalblahaj"]],
        'tyff': [custom_map["royalblahaj"]],
        'adi': [custom_map["gamerhaj"]],
        'hana': [default_map["sparkles"]],
        'ash': [default_map["regional_indicator_m"], default_map["regional_indicator_e"], default_map["m"], default_map["e_mail"]],
        'mara': [default_map["smiling_face_with_hearts"]],
        'adam': [default_map["isle_of_man"], custom_map["adam"]],
        'rico': [default_map["flag_us"], default_map["flag_in"]],
        'nandan': [default_map["face_exhaling"]]
    }

    for substr, reacts in people_reacts.items():
        if substr in string:
            for react in reacts:
                await message.add_reaction(react)
    
    # only do fun or emotion reacts if we're not in the rant channel
    if message.channel.id != channel_ids["rant"]:
        # fun-specific react map
        fun_reacts = {
            'iom': [default_map["isle_of_man"], custom_map["adam"]],
            'straight': [default_map["pirate_flag"]],
            'blahaj': [custom_map["justblahaj"]],
            'shark': [custom_map["justblahaj"]],
            'melon': [custom_map["melonblahaj"]],
            'holy fruit': [custom_map["melonblahaj"]],
            'uwu': [custom_map["blahajuwu"]],
            'boomer': [default_map["older_adult"]],
            'rain': [default_map["cloud_lightning"], default_map["thunder_cloud_rain"]],
            'thunderstorm': [default_map["cloud_lightning"], default_map["thunder_cloud_rain"]],
            'thunder': [default_map["cloud_lightning"], default_map["thunder_cloud_rain"]],
            'sleep': [default_map["yawning_face"], default_map["sleeping"]],
            'space': [default_map["rocket"]],
            'innovation': [default_map["rocket"]],
            'motivation': [default_map["rocket"]],
            'night': [default_map["night_with_stars"]],
            'morning': [default_map["sunrise"]],
            'ping': [custom_map["angrypinghaj"]],
            'innit': [default_map["england"]],
            'bruv': [default_map["england"]],
            'manannan': [default_map["motorboat"]],
            'initinit': [custom_map["initinit"]],
            'scream': [custom_map["initinit"]],
            'india': [default_map["flag_in"]],
            'usa': [default_map["flag_us"]],
            'party': [default_map["isle_of_man"], default_map["tada"], custom_map["partyblahaj"]],
            'pizza': [default_map["pizza"]],
            'watermelon': [default_map["watermelon"]],
            'pls': [default_map["pleading_face"]],
            'please': [default_map["pleading_face"]],
            'uh': [default_map["expressionless"]],
            'elon': [custom_map["elonsmoke"]],
            'musk': [custom_map["elonsmoke"]],
            'coffee': [custom_map["meow_coffee"]],
            'clown': [custom_map["catclown"]],
            'dance': [custom_map["blobdance"]],
            'code': [custom_map["meow_code"]],
            'hack': [custom_map["meow_code"]],
            'cat': [custom_map["meow_heart"]],
            'kitty': [custom_map["meow_heart"]],
            'meow': [custom_map["meow_heart"]],
            'sus': [custom_map["susblahaj"]],
            'smart': [custom_map["blasmart"]],
        }

        for substr, reacts in fun_reacts.items():
            if substr in string:
                for react in reacts:
                    await message.add_reaction(react)

        # emotion-specific react map
        emotion_reacts = {
            'rip': [custom_map["rip"]],
            'oof': [custom_map["blahajoof"]],
            'angry': [default_map["angry"]],
            'anger': [default_map["angry"]],
            'mad': [default_map["angry"]],
            'cry': [custom_map["blahajcrying"], custom_map["crii"]],
            'cri': [custom_map["blahajcrying"], custom_map["crii"]],
            'sad': [custom_map["blahajcry"], custom_map["crii"]],
            'alone': [custom_map["blahajcrying"]],
            'shush': [default_map["shushing_face"]],
            'lmao': [custom_map["LMAO"]]
        }

        for substr, reacts in emotion_reacts.items():
            if substr in string:
                for react in reacts:
                    await message.add_reaction(react)

    

    #restricted to #onlypuns channel, per vijay's request
    if message.channel.id == channel_ids["onlypuns"] and "pun" in string:
        pun_role = discord.utils.get(client.blahajgang_guild.roles, id=role_ids["pun_master"])
        #prevent pinging the pun master if they made the msg
        if pun_role not in message.author.roles:
            #ping pun master to deliver a needed pun
            await message.reply(pun_role.mention)

    if message.channel.id == channel_ids["onlypuns"] and "rate" in string:
        pun_role = discord.utils.get(client.blahajgang_guild.roles, id=role_ids["pun_master"])
        #prevent pinging the pun master if they made the msg
        if pun_role not in message.author.roles:
            #ping pun master to deliver a needed pun
            await message.reply(pun_role.mention + " rate 0-10")

    #react to msgs in #rant-here-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa but only if it has been more than an hour since last cry react, per neel's request
    if message.channel.id == channel_ids["rant"]:
        if time.time() > times["last_cry_time"] + 3600:
            await message.add_reaction(custom_map["blahajcry"])
            times["last_cry_time"] = time.time()

keep_alive()
client.run(os.getenv('TOKEN'))
