import discord
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option
import os
from keep_alive import keep_alive
import re
import time
import requests
import glob, random
from dotenv import load_dotenv
from ids import role_ids, channel_ids, guild_ids
from emojis import default_map, custom_list

load_dotenv()

# emoji info https://gist.github.com/scragly/b8d20aece2d058c8c601b44a689a47a0
# discord.py docs https://discordpy.readthedocs.io/en/latest/api.html
# change bot status https://python.plainenglish.io/how-to-change-discord-bot-status-with-discord-py-39219c8fceea
# "run on repl.it" button https://replit.com/talk/learn/Configuring-GitHub-repos-to-run-on-Replit-and-contributing-back/23948
# python regex basics https://www.w3schools.com/python/python_regex.asp
# python regex cheatsheet https://cheatography.com/mutanclan/cheat-sheets/python-regular-expression-regex/
# discord py slash commands #https://discord-py-slash-command.readthedocs.io/en/latest/gettingstarted.html #https://discord-py-slash-command.readthedocs.io/en/latest/discord_slash.context.html
#https://discord-py-slash-command.readthedocs.io/en/latest/gettingstarted.html?highlight=options#more-in-the-option-give-them-a-choice
#https://discord.com/developers/docs/interactions/slash-commands#application-command-object-application-command-option-type

#global vars

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)
response = requests.get("https://discord.com/oauth2/849471740052504606")
remaining_requests = response.headers.get('X-RateLimit-Limit')
print(remaining_requests)

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

#actual bot functions

#bot startup and status
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    for emoji in custom_list:
        custom_map[emoji] = discord.utils.get(client.emojis, name=emoji)
    blahajgang_guild = discord.utils.get(client.guilds, id=guild_ids["blahajgang"])
    roles_map["pun_master"] = discord.utils.get(blahajgang_guild.roles,
                                                id=role_ids["pun_master"])
    await client.change_presence(
        activity=discord.Game("Happy Pride Month! " +
                              default_map["rainbow_flag"]))

#bot slash commands
guild_ids_list = [guild_ids["blahajgang"]]


@slash.slash(name="contribute", guild_ids=guild_ids_list, description="here's the repo link to contribute to pride bot!")
async def contribute(ctx):
    #todo add a dm message with the tree structure of this repo
    url = "https://github.com/tyffical/Pridebot "
    await ctx.send(content=url)

@slash.slash(name="hug", guild_ids=guild_ids_list, description="hug gif because we all need it <3")
async def hug(ctx):
    hug_url = "https://thumbs.gfycat.com/AromaticWhiteChuckwalla-size_restricted.gif"
    await ctx.send(content=hug_url)
    
@slash.slash(name="elmoash", guild_ids=guild_ids_list, description="gif of ash morphing into elmo")
async def elmoash(ctx):
    gif_url = "https://tenor.com/view/ashwin-rise-elmo-meme-lord-rise-ashwin-meme-lord-rise-gif-22312460"
    await ctx.send(content=gif_url)

@slash.slash(name="gift", guild_ids=guild_ids_list, description="gift a friendo a blahaj!", 
options=[create_option(
          name="recipient",
          description="Who do you want to give this to?",
          option_type=6, #corresponds to USER
          required=False),
        create_option(
          name="reason",
          description="Why are you gifting this to them?",
          option_type=3, #corresponds to STRING
          required=False)
          ])
async def gift(ctx, recipient=None, reason=None):
    mention = recipient.id if recipient else None
    myid = ctx.author_id 
    if not reason:
        reason = "no reason, you simply deserve it. yeet"
    if not mention:
        await ctx.send(content="To whom should I send a gift?")
    elif mention == myid:
        await ctx.send(content="Ha! you can't gift yourself.")
    else:
        await ctx.send(
            content="<@{mention}>, here's a plushie for you!\n reason: {reason}".format(
                mention=mention, reason=reason),
            file=discord.File('giftBlahaj.png'))


#TODO: refactor this function maybe (react func and mention func)
#TODO: map keywords to reacts
#bot message reactions and replies
@client.event
async def on_message(message):
    #ignore bot's own message
    if message.author.id == client.user.id:
        return

    # gift a pride flag
    if message.channel.id != channel_ids["important_init"] and message.content.startswith(
            "colors"):
        mention = message.mentions[0].id if len(message.mentions) >= 1 else None
        myid = message.author.id 
        if not mention:
            await message.reply("whom should I send a gift?")
        elif mention == myid:
            await message.reply("Ha! you can't gift yourself.")
        else:
            path = ["./flags/*.png"]
            random_flag = glob.glob(random.choice(path))
            await message.reply(
                "<@{mention}> Here's a gift from blahaj and {author}:\n".format(
                    mention=mention, author=message.author.mention),
                file=discord.File(random.choice(random_flag)))

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
                file=discord.File('hug.gif'))

    # for some reason blahajgangers wanted to arrest one another?
    if message.channel.id != channel_ids["important_init"] and (
            message.content.startswith("arrest")):
        mention = message.mentions[0].id if len(message.mentions) >= 1 else None
        myid = message.author.id 
        reason = message.content.lower().replace("hug <@" + str(mention) + ">", "") 
        # Basically filtering the content and removing gift and the mention to get the reason
        if reason == "":
            reason = "cuz they can"
        if not mention:
            await message.reply("whom should I arrest?")
        elif mention == myid:
            await message.reply("Ha! you can't arrest yourself.")
        else:
            await message.reply(
                "<@{mention}> You're under arrest!\n reason: {why}".format(
                    mention=mention, why=reason))
        
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

    #identity-specific reacts
    if "trans" in string:
        await message.add_reaction(custom_map["pride_heart_trans"])
    if "poc" in string:
        await message.add_reaction(custom_map["pride_heart_pocpride"])
    if "pan" in string:
        await message.add_reaction(custom_map["pride_heart_pan"])
    if "nonbinary" in string or "nb" in string:
        await message.add_reaction(custom_map["pride_heart_nonbinary"])
    if "lesbian" in string:
        await message.add_reaction(custom_map["pride_heart_lesbian"])
    if "genderqueer" in string:
        await message.add_reaction(custom_map["pride_heart_genderqueer"])
    if "gay" in string:
        await message.add_reaction(custom_map["pride_heart_gay"])
    if "bi" in string:
        await message.add_reaction(custom_map["pride_heart_bi"])
    if "aro" in string:
        await message.add_reaction(custom_map["pride_heart_aro"])
    if "ace" in string or "asexual" in string:
        await message.add_reaction(custom_map["pride_heart_ace"])

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

    #scream for INIT, but reactions only it is too much
    if message.channel.id != channel_ids["important_init"]:
        if "init" in string or "scream" in string:
            # await message.reply("https://tenor.com/view/jonah-hill-shriek-excited-scream-shout-gif-4705306")
            await message.add_reaction(custom_map["initinit"])


keep_alive()
client.run(os.getenv('TOKEN'))
