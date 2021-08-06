#Iscus, The Lady of Our Fate, is a dice bot for Discord
---
      All rolls are drawn from RANDOM.ORG
      See: (https://www.random.org/)
      This bot is designed to run in memory on a server or container of your choice

**How to use:**
      
* Type a message beginning with ?roll followed by a dice expression. Example: ?roll 1d100
* A maximum of four combinations of dice and/or modifiers are permitted per roll, in any order, such as ?roll 2d8+2-1d4+1, or ?roll 1d100+1d20+2d10-4d6.  Each factor must be separated by a plus (+) or minus (-) symbol.
* You can add a comment to a roll by adding a space after the roll expression and typing whatever you want, like: ?roll 1d100 Ragnar Trident(85)
* Type ?help about or just ?about to see this info in Discord

**New Features in v2.0:**
      
* Now will respond in Discord threads! Requires installing [Discord.py](https://github.com/Rapptz/discord.py) beta v2.x or higher like: 
'''pip install -U git+https://github.com/Rapptz/discord.py'''
* *roll changed to ?roll to make it one less tap from a mobile phone
* No more need to type a * before a roll comment, you can now just leave a space like: ?roll 1d100 Ragnar Sanity(92)
* Now supports minus signs in roll expressions like 2d6+1d4+2-1d3
* Added support for rolling d2's
* Better help documentation with ?help and ?help roll
* Added support for @Iscus ping or ?ping commands (replies if online/alive)
* Added some error handling to catch fat fingered roll formulas
* Improved uptime from switching discord.Client() with on_message(message)to commands.Bot to reduce Discord API rate limiting
    
**Known issues:**
      
* Discord.py v2.x beta library used... Breaking changes may occur when the official verion is released
* Not all error handling cases discovered yet; I'm sure your fat fingers will point out bugs before long...
* Only these dice types are supported: d100,d20, d12, d10, d8, d6, d4, d3, and d2.  You can't roll a d7 for example.

May Chael ever watch over your rolls and Phyth never weave them for you... Enjoy!
