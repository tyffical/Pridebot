# emoji codes https://emojiterra.com/
# emoji codes https://emojigraph.org/

#emojis

#default -> unicode (see emojiterra or emojigraph for codes)
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
    "flag_in": "\U0001f1ee\U0001f1f3",
    "regional_indicator_m": "\U0001f1f2",
    "regional_indicator_e": "\U0001f1ea",
    "m": "\u24C2\uFE0F",
    "e_mail": "\U0001f4e7",
    "flag_vn": "\U0001f1fb\U0001f1f3",
    "thunder_cloud_rain": "\u26C8",
    "cloud_lightning": "\U0001f329",
    "yawning_face": "\U0001f971",
    "sleeping": "\U0001f634",
    "shushing_face": "\U0001f92b",
    "exploding_head": "\U0001f92f"
    
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
    "blaheart", "melonBLAHAJ", "yaay", "blahajuwu", "mlhblahaj", "gamerhaj", "adam", "awwblahaj"
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