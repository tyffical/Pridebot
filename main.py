import discord
import os
from keep_alive import keep_alive
import re
import time
import requests
import glob, random
from dotenv import load_dotenv

load_dotenv()

# emoji info https://gist.github.com/scragly/b8d20aece2d058c8c601b44a689a47a0
# discord.py docs https://discordpy.readthedocs.io/en/latest/api.html
# emoji codes https://emojiterra.com/
# emoji codes https://emojigraph.org/
# keeping bot alive on repl.it https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz
# change bot status https://python.plainenglish.io/how-to-change-discord-bot-status-with-discord-py-39219c8fceea
# "run on repl.it" button https://replit.com/talk/learn/Configuring-GitHub-repos-to-run-on-Replit-and-contributing-back/23948
# python regex basics https://www.w3schools.com/python/python_regex.asp
# python regex cheatsheet https://cheatography.com/mutanclan/cheat-sheets/python-regular-expression-regex/

#global vars

client = discord.Client()
response = requests.get("https://discord.com/oauth2/849471740052504606")
remaining_requests = response.headers.get('X-RateLimit-Limit')
print(remaining_requests)




pride_words = [
    "pride", "proud", "rainbow", "gay", "queer", "lgbt", "love", "june",
    "heart", "jack"
]

proud_friendo_role_id = 849425044345716756  #for helpful allies

pun_master_role_id = 842825815808409632
roles_map = {}

onlypuns_channel_id = 842807004879650826
rant_channel_id = 838861911374037062
important_init_channel_id = 850119805330653224
sentiment_channel_id = 860347893729460264

times = {"last_cry_time": 0}

blahajgang_guild_id = 825807863146479657

responses = [
    "hey homie", "sup mate?", "why'd you summon me, mate?",
    "sorry, im busy atm"
]

#emojis

#default -> unicode (see https://emojiterra.com for codes)
default_list = [
    "rainbow_flag", "rainbow", "rocket", "sparkles", "night_with_stars",
    "angry", "sunrise", "pirate_flag", "england", "motorboat", "isle_of_man",
    "tada", "regional_indicator_p", "regional_indicator_a",
    "regional_indicator_r", "regional_indicator_t", "regional_indicator_y",
    "white_check_mark", "x", "smiling_face_with_hearts", "watermelon"
]
default_map = {
    "rainbow_flag": "\U0001f3f3\uFE0F\u200D\U0001f308",
    "rainbow": "\U0001f308",
    "rocket": "\U0001f680",
    "sparkles": "\u2728",
    "night_with_stars": "\U0001f303",
    "angry": "\U0001f620",
    "sunrise": "\U0001f305",
    "pirate_flag": "\U0001f3f4\u200D\u2620\uFE0F",
    "england":
    "\U0001f3f4\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f",
    "motorboat": "\U0001f6e5\uFE0F",
    "isle_of_man": "\U0001f1ee\U0001f1f2",
    "tada": "\U0001F389",
    "regional_indicator_p": "\U0001F1F5",
    "regional_indicator_a": "\U0001F1E6",
    "regional_indicator_r": "\U0001F1F7",
    "regional_indicator_t": "\U0001F1F9",
    "regional_indicator_y": "\U0001F1FE",
    "white_check_mark": "\u2705",
    "x": "\u274C",
    "smiling_face_with_hearts": "\U0001f970",
    "watermelon": "\U0001F349",
    "regional_indicator_o": "\U0001f1f4",
    "regional_indicator_l": "\U0001f1f1",
    "o2": "\U0001f17e\uFE0F",
    "flag_us": "\U0001f1fa\U0001f1f8",
    "older_adult":"\U0001f9d3\U0001f3fb",
    "flag_in": "\U0001f1ee\U0001f1f3"

}
#TODO: find a way to automate getting the unicodes (web scraping?)

#custom -> discord.Emoji objects
custom_list = [
    "prideblahaj", "partyblahaj", "justblahaj", "blahajyeet", "rip",
    "melonblahaj", "ryancoin", "angrypinghaj", "blahajcry", "royalblahaj",
    "rainbowblahaj", "spaceblahaj", "blahajoof", "pride_heart_trans",
    "pride_heart_pocpride", "pride_heart_pan", "pride_heart_nonbinary",
    "pride_heart_lesbian", "pride_heart_genderqueer", "pride_heart_gay",
    "pride_heart_bi", "pride_heart_aro", "pride_heart_ace", "initinit",
    "blaheart", "melonBLAHAJ", "yaay","blahajuwu"
]
custom_map = {}

#nqn -> custom emojis from other servers using NotQuiteNitro bot (can be done by sending a message with !react <emoji_name>)
#unfortunately this does not work if sender is a bot :(
#TODO: figure out a way to use nqn anyway?
nqn_list = [
    "elonsmoke", "meow_coffee", "catclown", "LMAO", "crii", "blobdance",
    "meow_code", "meow_heart", "3c"
]
nqn_msg = "!react {}"

#actual bot functions


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    for emoji in custom_list:
        custom_map[emoji] = discord.utils.get(client.emojis, name=emoji)
    blahajgang_guild = discord.utils.get(client.guilds, id=blahajgang_guild_id)
    roles_map["pun_master"] = discord.utils.get(blahajgang_guild.roles,
                                                id=pun_master_role_id)
    await client.change_presence(
        activity=discord.Game("Happy Pride Month! " +
                              default_map["rainbow_flag"]))


#TODO: refactor this function maybe (react func and mention func)
#TODO: map keywords to reacts
@client.event
async def on_message(message):
    #ignore bot's own message
    if message.author.id == client.user.id:
        return
    sentiment = os.environ['sentiment']
    #sentiment analysis
    r = requests.post(
        "https://api.deepai.org/api/sentiment-analysis",
        data={
            'text': message.content,
        },
        headers={'api-key': sentiment})
    print(str(message.content))
    print(r.json()) #prints out id and output: formated as array of ['verypositive/positive/neutral/negative/verynegative']
    if message.channel.id == sentiment_channel_id:
        sentiment = str(r.json()["output"][0]).lower()
        #switch to match-case (aka switch) statements for python 3.10
        if sentiment == "verypositive" or sentiment == "positive":
            await message.add_reaction(custom_map["blaheart"])
        elif sentiment == "neutral":
            await message.add_reaction(custom_map["melonBLAHAJ"])
        else:
            await message.add_reaction(custom_map["yaay"])


    #react with melon because melon is amazing -adam
    #only in #dis-for-important-linkz-n-messages-init tho to prevent spam -tiff
    if message.channel.id == important_init_channel_id:
        await message.add_reaction(default_map["watermelon"])

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
                if role.id == proud_friendo_role_id:
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
    if message.channel.id != important_init_channel_id:
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
    if message.channel.id != rant_channel_id:
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

    #per hana's request
    if "hana" in string:
        await message.add_reaction(default_map["sparkles"])

    #tiffany having fun
    # if "code" in string or "hack" in string:
    #     await message.reply(nqn_msg.format("meow_code"))
    # if "cat" in string or "kitty" in string or "meow" in string:
    #     await message.reply(nqn_msg.format("meow_heart"))
    if "tiff" in string:
        # await message.reply(nqn_msg.format("3c"))
        await message.add_reaction(custom_map["royalblahaj"])

    if "ash" in string:
        await message.add_reaction(default_map["regional_indicator_y"])
        await message.add_reaction(default_map["regional_indicator_o"])
        await message.add_reaction(default_map["regional_indicator_l"])
        await message.add_reaction(default_map["o2"])

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
    if message.channel.id == onlypuns_channel_id:
        if "pun" in string:
            not_pun_master = True
            #prevent pinging the pun master if they made the msg
            for role in message.author.roles:
                if role.id == pun_master_role_id:
                    not_pun_master = False
                    break
            #ping pun master to deliver a needed pun
            if not_pun_master:
                await message.reply(roles_map["pun_master"].mention)

    #react to msgs in #rant-here-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa but only if it has been more than an hour since last cry react, per neel's request
    if message.channel.id == rant_channel_id:
        if time.time() > times["last_cry_time"] + 3600:
            await message.add_reaction(custom_map["blahajcry"])
            times["last_cry_time"] = time.time()

    #scream for INIT, but reactions only it is too much
    if message.channel.id != important_init_channel_id:
        if "init" in string or "scream" in string:
            # await message.reply("https://tenor.com/view/jonah-hill-shriek-excited-scream-shout-gif-4705306")
            await message.add_reaction(custom_map["initinit"])

    # gift a pride flag
    message.content = message.content.lower()
    if message.channel.id != important_init_channel_id and message.content.startswith(
            "colors"):
        mention = string.split('colors')
        print(mention)
        myid = message.author.id  #improvement -> this line gets your id, we want it to get the mentioned person's id
        res = re.split("[!<>@]", mention[1])
        reason = re.split("[!<>@\d+]", mention[1])
        res = res[3]
        reason = list(filter(None, reason))
        # print(reason)
        if not mention[1]:
            await message.reply("whom should I send a gift?")
        elif int(res) == myid:
            await message.reply("Ha! you can't gift yourself.")
        else:
            path = ["./flags/*.png"]
            random_flag = glob.glob(random.choice(path))
            await message.reply(
                "{mention} Here's a gift from blahaj and {author}:\n".format(
                    mention=mention[1], author=message.author.mention),
                file=discord.File(random.choice(random_flag)))

    # gift blahaj for good work or anyway coz why not
    message.content = message.content.lower()
    if message.channel.id != important_init_channel_id and (
            message.content.startswith("gift")):
        mention = string.split('gift')
        myid = message.author.id  #improvement -> this line gets your id, we want it to get the mentioned person's id
        res = re.split("[!<>@]", mention[1])
        reason = re.split("[!<>@\d+]", mention[1])
        res = list(filter(None, res))
        res = res[0]
        reason = list(filter(None, reason))
        if not reason:
            reason = "no reason, you simply deserve it. yeet"
        else:
            reason = reason[0]
        # print(reason)
        if not mention[1]:
            await message.reply("whom should I send a gift?")
        elif int(res) == myid:
            await message.reply("Ha! you can't gift yourself.")
        else:
            await message.reply(
                "{mention} Here's a plushie for you:\n reason: {why}".format(
                    mention=mention[1], why=reason),
                file=discord.File('giftBlahaj.png'))
        print(reason)
        member = message.mentions[0]
        print(member)


keep_alive()
client.run(os.getenv('TOKEN'))
