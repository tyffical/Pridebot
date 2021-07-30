import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

from info.ids import role_ids, channel_ids, guild_ids
from info.emojis import default_map, custom_list

import os, re, time, requests, random

from scripts.keep_alive import keep_alive
from dotenv import load_dotenv
load_dotenv()

# global vars
client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
response = requests.get("https://discord.com/oauth2/849471740052504606")
remaining_requests = response.headers.get('X-RateLimit-Limit')
# print(remaining_requests)

# various dicts
pride_words = [
    "pride", "proud", "rainbow", "gay", "queer", "lgbt", "love", "june",
    "heart", "jack"
]

roles_map = {}

custom_map = {}

times = {"last_cry_time": 0}

responses = [
    "hey homie", "sup mate?", "why'd you summon me, mate?",
    "sorry, im busy atm"
]

guild_ids_list = [guild_ids["blahajgang"]]

# add cogs
client.load_extension("cogs.fun")
client.load_extension("cogs.gifts")
client.load_extension("cogs.utils")

#bot startup and status
@client.event
async def on_ready():
    print("Bot is ready! Logged in as " + str(client.user))
    for emoji in custom_list:
        custom_map[emoji] = discord.utils.get(client.emojis, name=emoji)
    blahajgang_guild = discord.utils.get(client.guilds, id=guild_ids["blahajgang"])
    roles_map["pun_master"] = discord.utils.get(blahajgang_guild.roles,
                                                id=role_ids["pun_master"])
    await client.change_presence(
        activity=discord.Game("Happy Pride Month! " + default_map["rainbow_flag"]))

# afk slash command
# TODO: Move it to a cog once I figure out a database - Michael
# !afk command so ->If I use the command and add the reason when ever someone tags me it should show <myname> is afk reason: So and so (krish)
afkdict = {} #defines all the ppl afk
@slash.slash(name="afk", guild_ids=guild_ids_list, description="set your afk status so that it will show up when you're tagged", 
options=[create_option(
          name="reason",
          description="Why will you be afk?",
          option_type=3, #corresponds to STRING
          required=False)
          ])#afk command body 
async def afk(ctx, reason = "They didn't leave a reason!"):
    global afkdict

    if ctx.author in afkdict:
        afkdict.pop(ctx.author)
        await ctx.send('Welcome back! You are no longer afk.')

    else:
        afkdict[ctx.author] = reason
        await ctx.send("You are now afk. Beware of the real world!")

# bot message reactions and replies
# TODO: refactor this function (react func and mention func)
@client.event
async def on_message(message):
    #ignore bot's own message
    if message.author.id == client.user.id:
        return
    
    #afk stuff
    global afkdict
    if message.author in afkdict:
       await message.channel.send("Welcome back! You are no longer afk.")
       afkdict.pop(message.author)
    for member in message.mentions:  
        if member != message.author:  
            if member in afkdict:  
                afkmsg = afkdict[member]  
                # await message.reply(f"Oh noes! <@{member.id}> is afk. Reason-> {afkmsg}")  #commented out original
                await message.reply(f"This bitch afk. YEET [*source*](https://www.youtube.com/watch?v=2Bjy5YQ5xPc)")
                await message.reply(f"Reason-> {afkmsg}")

    # Who doesn’t need a hug every now and again?
    if message.channel.id != channel_ids["important_init"] and (
            message.content.startswith("hug")):
        mention = message.mentions[0].id if len(message.mentions) >= 1 else None
        myid = message.author.id 
        reason = message.content.lower().replace("hug <@" + str(mention) + ">", "") 
        # Basically filtering the content and removing gift and the mention to get the reason
        if reason == "":
            reason = "no reason, you simply deserve it. yeet"
        if not mention:
            await message.reply("whom do you want to hug?")
        elif mention == myid:
            await message.reply("Ha! you can't hug yourself.")
        else:
            await message.reply(
                "<@{mention}> Everbody needs a hug. It changes your metabolism:\n Reason: {reason}".format(
                    mention=mention, reason=reason),
                file=discord.File('./images/hug.gif'))

        
    #strip whitespace and change to lowercase
    string = "".join(message.content.lower().split())

    #split by spaces, commas, periods, etc to get the words in the string
    words = re.split(r"[,:. \"'-]+", message.content.lower())

    #TODO: see if computer vision can be used to detect text or rainbows in images
    #pride reacts
    for word in pride_words:
        if word in string:
            await message.add_reaction(default_map["rainbow_flag"])
            await message.add_reaction(custom_map["prideblahaj"])

            #check if author not "Member" (i.e. bot) -> they have no roles
            if not isinstance(message.author, discord.Member):
                break

            #proud friendo gets extra reacts, per jack's request
            for role in message.author.roles:
                if role.id == role_ids["proud_friendo"]:
                    await message.add_reaction(default_map["rainbow"])
                    await message.add_reaction(custom_map["rainbowblahaj"])
                    await message.add_reaction(custom_map["partyblahaj"])

            break

    #identity-specific react map
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

    #pridebot responding to a mention of its name
    if message.channel.id != channel_ids["important_init"]:
        if "pridebot" in string:
            r = requests.head(url="https://discord.com/api/v2/")
            try:
                await message.reply(
                    f"Rate limit {int(r.headers['Retry-After']) / 60} minutes until activity"
                )
            except:
                rn = random.randint(0, 3)
                await message.reply(responses[rn])

    #miscellaneous reacts

    if "straight" in string:
        await message.add_reaction(default_map["pirate_flag"])

    if "blahaj" in string or "shark" in string:
        await message.add_reaction(custom_map["justblahaj"])

    #matches yeets with an arbitrary number of e's
    if re.search("yee+t", string) != None:
        await message.add_reaction(custom_map["blahajyeet"])

    if "rip" in string:
        await message.add_reaction(custom_map["rip"])

    #only cry if not in rant channel
    if message.channel.id != channel_ids["rant"]:
        if "cry" in string or "cri" in string or "sad" in string or "alone" in string:
            await message.add_reaction(custom_map["blahajcry"])

    if "oof" in string:
        await message.add_reaction(custom_map["blahajoof"])

    if "angry" in words or "anger" in words or "mad" in words:
        await message.add_reaction(default_map["angry"])

    if "melon" in string:
        await message.add_reaction(custom_map["melonblahaj"])

    if "ryan" in string:
        await message.add_reaction(custom_map["ryancoin"])
    
    if "uwu" in string:
        await message.add_reaction(custom_map["blahajuwu"])

    if "boomer" in string:
        await message.add_reaction(default_map["older_adult"])
        
    if "rain" in string or "thunderstorm" in string or "thunder" in string:
        await message.add_reaction(default_map["cloud_lightning"])
        await message.add_reaction(default_map["thunder_cloud_rain"])
        
    if "sleep" in string:
        await message.add_reaction(default_map["yawning_face"])
        await message.add_reaction(default_map["sleeping"])
        
    # gamerhaj react for pro blahaj gamer
    if "adi" in string:
        await message.add_reaction(custom_map["gamerhaj"])

    #per neel's request
    if "space" in string or "innovation" in string or "motivation" in string:
        await message.add_reaction(default_map["rocket"])
    # if "elon" in string:
    #     await message.reply(nqn_msg.format("elonsmoke"))
    # if "coffee" in string:
    #     await message.reply(nqn_msg.format("meow_coffee"))
    # if "clown" in string:
    #     await message.reply(nqn_msg.format("catclown"))
    # if "lmao" in string:
    #     await message.reply(nqn_msg.format("LMAO"))
    # if "cry" in string or "cri" in string or "sad" in string:
    #     await message.reply(nqn_msg.format("crii"))
    # if "dance" in string:
    #     await message.reply(nqn_msg.format("blobdance"))
    if "neel" in string:
        await message.add_reaction(custom_map["spaceblahaj"])
    
    # yes i added this myself
    # i just want cool reaction, okay?
    # why are you looking at me like that
    # stop it
    if "vik" in string:
        await message.add_reaction(custom_map["mlhblahaj"])
        
    # i added this myself :)
    if "bailey" in string:
        await message.add_reaction(custom_map["awwblahaj"])
        await message.add_reaction(default_map["flag_vn"])

    #per hana's request
    if "hana" in string:
        await message.add_reaction(default_map["sparkles"])

    #tiffany having fun
    # if "code" in string or "hack" in string:
    #     await message.reply(nqn_msg.format("meow_code"))
    # if "cat" in string or "kitty" in string or "meow" in string:
    #     await message.reply(nqn_msg.format("meow_heart"))
    if "tiff" in string or "tyff" in string:
        # await message.reply(nqn_msg.format("3c"))
        await message.add_reaction(custom_map["royalblahaj"])

    if "ash" in string:
        await message.add_reaction(default_map["regional_indicator_m"])
        await message.add_reaction(default_map["regional_indicator_e"])
        await message.add_reaction(default_map["m"])
        await message.add_reaction(default_map["e_mail"])

    #per mara's request
    if "mara" in string:
        await message.add_reaction(default_map["smiling_face_with_hearts"])
        
    #per Rico's Request
    if "rico" in string:
        await message.add_reaction(default_map["flag_us"])
        await message.add_reaction(default_map["flag_in"])

    if "night" in string:
        await message.add_reaction(default_map["night_with_stars"])
    if "morning" in string:
        await message.add_reaction(default_map["sunrise"])

    if "ping" in string:
        await message.add_reaction(custom_map["angrypinghaj"])

    if "innit" in string or "bruv" in string:
        await message.add_reaction(default_map["england"])

    #per adam's request
    if "manannan" in string:
        await message.add_reaction(default_map["motorboat"])

    if "adam" in string or "iom" in string:
        await message.add_reaction(default_map["isle_of_man"])
        await message.add_reaction(custom_map["adam"])
    
    if "india" in string:
        await message.add_reaction(default_map["flag_in"])

    if  "usa" in message.content.lower().split(): #now it checks only for the word 'us' AND NOW IT CHECKS FOR USA BECAUSE ADAM ANNOYED
        await message.add_reaction(default_map["flag_us"])

    #added by Adam in the club
    if "party" in string:
        await message.add_reaction(default_map["isle_of_man"])
        await message.add_reaction(default_map["tada"])
        await message.add_reaction(custom_map["partyblahaj"])

    #also added by adam but not in the club
    if "partyisland:thevirtualexperience" in string:
        await message.add_reaction(default_map["regional_indicator_p"])
        await message.add_reaction(default_map["regional_indicator_a"])
        await message.add_reaction(default_map["regional_indicator_r"])
        await message.add_reaction(default_map["regional_indicator_t"])
        await message.add_reaction(default_map["regional_indicator_y"])
        await message.add_reaction(default_map["white_check_mark"])
        await message.add_reaction(default_map["x"])

    #restricted to #onlypuns channel, per vijay's request
    if message.channel.id == channel_ids["onlypuns"]:
        if "pun" in string:
            
            not_pun_master = True
            #prevent pinging the pun master if they made the msg
            for role in message.author.roles:
                if role.id == role_ids["pun_master"]:
                    not_pun_master = False
                    break
            #ping pun master to deliver a needed pun
            if not_pun_master:
                await message.reply(roles_map["pun_master"].mention)

    #react to msgs in #rant-here-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa but only if it has been more than an hour since last cry react, per neel's request
    if message.channel.id == channel_ids["rant"]:
        if time.time() > times["last_cry_time"] + 3600:
            await message.add_reaction(custom_map["blahajcry"])
            times["last_cry_time"] = time.time()

    #scream for INIT
    if "init" in string or "scream" in string:
        await message.add_reaction(custom_map["initinit"])


keep_alive()
client.run(os.getenv('TOKEN'))
