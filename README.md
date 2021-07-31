<h1 align="center">Pridebot</h1>
<br>
<p align="center">
  <a href="https://github.com/tyffical/Pridebot/issues"><img src="https://img.shields.io/github/issues/tyffical/Pridebot"></a>
  <a href="https://github.com/tyffical/Pridebot/network/members"><img src="https://img.shields.io/github/forks/tyffical/Pridebot"></a>
  <a href="https://github.com/tyffical/Pridebot/stargazers"><img src="https://img.shields.io/github/stars/tyffical/Pridebot"></a>
  <a href="https://github.com/tyffical/Pridebot/blob/main/LICENSE"><img src="https://img.shields.io/github/license/tyffical/Pridebot"></a>
</p>
<p align="center">
  <a href="https://blahaj.lol/discord"><img alt="Pride Bot" title="Pride Bot" src="./images/flags/1.png" width="400" align="center"></a>
</p>

<p align="center">
  BLAHAJGang's custom-made pride-themed Discord bot that reacts to pride-related messages with pride emojis, as well as some other Blahaj-tastic Easter eggs!
  <br>
  <br>
  <a href="https://discord.com/api/oauth2/authorize?client_id=864548443234107402&permissions=2148002880&scope=bot">Click here to invite the bot!</href>
</p>

<details open="open">
<summary>Table of Contents</summary>

- [Invite the Bot](#invite-the-bot)
- [Quickstart](#quickstart)
  - [Local](#local)
    - [Prerequisites](#prerequisites)
    - [Manual Setup](#manual-setup)
  - [On Replit](#on-replit)
- [Contributing](#contributing)
  - [Resources](#resources)
- [Maintainers](#maintainers)
- [Other Major Contributors](#other-major-contributors)
- [Special Thanks](#special-thanks)
- [Support](#support)
- [License](#license)

</details>

---

# Quickstart

## Selfhosting

### Prerequisites

- [Python 3.8 or above](https://www.python.org/downloads/)
  - [PIP (Python Package Manager)](https://pip.pypa.io/en/stable/installation/)
- [Command Line Git](https://git-scm.com/downloads)
  - [Or Github Desktop, if you prefer](https://desktop.github.com)
- [A Discord Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html)

### Manual Setup

_Note: Right now, you will have to edit `ids.py` to contain role IDs and channel IDs from your test server; otherwise the bot may not function properly._

1. To run the bot locally, clone and `cd` into the repository.
   ```
   git clone https://github.com/tyffical/Pridebot.git
   cd Pridebot
   ```
2. (OPTIONAL) Create and activate a new Python virtual environment.
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the requirements using `pip`.
   ```
   pip install -r requirements.txt
   ```
4. Copy the `.env.example` file to `.env`, and edit it to include your Discord bot token. Your bot token can be found in the "Bot" settings of your [application settings.](https://discord.com/developers/applications)
   ```
   cp .env.example .env
   ```
5. Run the main file.
   ```
   python3 main.py
   ```
6. And congratulations! You're good to go!

### On Replit

[![Run on Repl.it](https://repl.it/badge/github/tyffical/Pridebot)](https://repl.it/github/tyffical/Pridebot)

Make sure to add your bot token by clicking on the padlock symbol on the left sidebar, and then inserting "TOKEN" into the `key` text field and your bot token into the `value` text field.

You can turn on the `Always On` setting (found by clicking on the repl name) to keep the bot continuously running!

# Contributing

**First off: thanks for contributing to Pridebot!** As a BLAHAJGang community project, we welcome any and all contributions by members and are so excited to see you grow as a developer!

Any contributions, no matter how big or small, will benefit the bot and are greatly appreciated!

To get started, head over to the [BLAHAJGang Discord Server](https://blahaj.lol/discord) and ask one of the bot's maintainers to walk you through the repository and how to set the bot up locally.

Then, read the [Code of Conduct](https://github.com/tyffical/Pridebot/blob/main/CODE_OF_CONDUCT.md) and [Contribution Guidelines](https://github.com/tyffical/Pridebot/blob/main/CONTRIBUTING.md) to brush up on how to properly contribute to the bot! Make sure you have the prerequisite knowledge of Python and Discord.py if you plan on contributing to the code itself.

When you open an issue or pull request, ping one (or more) of the bot's maintainers in the BLAHAJGang Discord Server to go over it with you and formally review it! They're usually available during the day (EST) and will be more than happy to help you out.

After that, you're good to go! Happy coding <3

## Contribution Resources

Some resources for contributing are listed below:

- [Discord.py Documentation](https://discordpy.readthedocs.io/en/latest/api.html)
- [Information on Discord Emojis](https://gist.github.com/scragly/b8d20aece2d058c8c601b44a689a47a0)
- [Hosting on Repl.it](https://replit.com/talk/learn/Configuring-GitHub-repos-to-run-on-Replit-and-contributing-back/23948)
- [Python Regex Basics](https://www.w3schools.com/python/python_regex.asp)
- [Python Regex Cheatsheet](https://cheatography.com/mutanclan/cheat-sheets/python-regular-expression-regex/)
- [Discord.py Slash Commands](https://discord-py-slash-command.readthedocs.io/en/latest/gettingstarted.html)
- [Discord.py Slash Command Context](https://discord-py-slash-command.readthedocs.io/en/latest/discord_slash.context.html)

---

## Maintainers

- [Tiffany Trinh](https://tyffic.al)
- [Neel Adwani](https://neeltron.com)
- [Adam Drummond](https://adamd.fyi/)
- [Michael Cao](https://m.omg.lol)
- [Ashwin Kumar Uppala](https://github.com/ashwinexe)

## Special Thanks

- [Jacklyn Biggin](https://poly.work/jacklynbiggin)
  - Creator of BLAHAJGang &#x2764;&#xFE0F;
- [BLAHAJ](https://www.ikea.com/us/en/p/blahaj-soft-toy-shark-90373590/)
  - We wouldn't be a cult without you &#x2764;&#xFE0F;
- [BLAHAJGang](https://blahajgang.lol/)
  - For being an awesome community! &#x2764;&#xFE0F;
- The LGBTQ+ Community
  - Happy Pride! &#x1F3F3;&#xFE0F;&#x200D;&#x1F308; Thanks for being awesome! &#x2764;&#xFE0F;

## Support

For support, reach out to us on [our Discord server](https://blahaj.lol/discord) in the #pride-bot-requests-and-contributions channel.

## License

This repository is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.
