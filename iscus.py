import discord
import os
import requests
import json
import re
from discord.ext import commands
from dotenv import load_dotenv
import math

load_dotenv()

d100s = []
d20s = []
d12s = []
d10s = []
d8s = []
d6s = []
d4s = []
d3s = []
d2s = []

def parse_roll(DiceSides):
  DiceSides = int(DiceSides)
  if DiceSides == 100:
    global d100s
    if len(d100s) > 0:
      RemovedFirstRoll = d100s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d100s = DiceResult
      RemovedFirstRoll = d100s.pop(0)      
      return(RemovedFirstRoll)
  if DiceSides == 20:
    global d20s
    if len(d20s) > 0:
      RemovedFirstRoll = d20s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d20s = DiceResult
      RemovedFirstRoll = d20s.pop(0)      
      return(RemovedFirstRoll)
  if DiceSides == 12:
    global d12s
    if len(d12s) > 0:
      RemovedFirstRoll = d12s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d12s = DiceResult
      RemovedFirstRoll = d12s.pop(0)      
      return(RemovedFirstRoll)
  if DiceSides == 10:
    global d10s
    if len(d10s) > 0:
      RemovedFirstRoll = d10s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d10s = DiceResult
      RemovedFirstRoll = d10s.pop(0)      
      return(RemovedFirstRoll)
  if DiceSides == 8:
    global d8s
    if len(d8s) > 0:
      RemovedFirstRoll = d8s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d8s = DiceResult
      RemovedFirstRoll = d8s.pop(0)      
      return(RemovedFirstRoll)
  if DiceSides == 6:
    global d6s
    if len(d6s) > 0:
      RemovedFirstRoll = d6s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d6s = DiceResult
      RemovedFirstRoll = d6s.pop(0)      
      return(RemovedFirstRoll)
  if DiceSides == 4:
    global d4s
    if len(d4s) > 0:
      RemovedFirstRoll = d4s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d4s = DiceResult
      RemovedFirstRoll = d4s.pop(0)      
      return(RemovedFirstRoll)
  if DiceSides == 3:
    global d3s
    if len(d3s) > 0:
      RemovedFirstRoll = d3s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d3s = DiceResult
      RemovedFirstRoll = d3s.pop(0)      
      return(RemovedFirstRoll)     
  if DiceSides == 2:
    global d2s
    if len(d2s) > 0:
      RemovedFirstRoll = d2s.pop(0)
      return(RemovedFirstRoll)
    else:
      DiceResult = roll_100_dice(DiceSides)
      d2s = DiceResult
      RemovedFirstRoll = d2s.pop(0)      
      return(RemovedFirstRoll)             
  else: #DiceSides isn't allowed
    DiceResult = "only 100, 20, 12, 10, 8, 6, 4, 3, and 2 sided dice are allowed"
    return()

def parse_factor(passFactor):
  if "d" in passFactor: #is a dice expression to evaluate
      DiceNum, DiceSides = passFactor.split('d', 1)
      if int(DiceSides) in [100, 20, 12, 10, 8, 6, 4, 3, 2]: #check that supported sided dice are being asked for
        FactorX = []
        for x in range(0, int(DiceNum)):
          FactorX.append(parse_roll(DiceSides))
        return(FactorX) #if is a dice expression, this rolls the resulting numbers as a list
      else:
        ErrorMsg = 99999 #add a numeric code impossible to be rolled that can be teted for and passed as int
        return(ErrorMsg)
  else: #is a modifier
    ConvertedModifier = [int(passFactor)]
    return(list(ConvertedModifier)) #returns modifier as a list

def roll_1d100(): #get one roll from the list of up to 100 in the variable d100s and delete the first one after using it
  d100 = roll_d100() #get the whole list of 100 rolls
  global d100s 
  RemovedFirstRoll = d100s.pop(0) #remove first value in global d100s variable
  return(RemovedFirstRoll)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"), description="A dice bot using random.org")

def roll_100_dice(DiceSides):
  IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
  APIkey = os.getenv('KEY')
  response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':DiceSides,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
  json_data = json.loads(response.text)
  if DiceSides == 100:
    global d100s
    d100s = list(json_data['result']['random']['data'])
    return(d100s)
  if DiceSides == 20:
    global d20s
    d20s = list(json_data['result']['random']['data'])
    return(d20s)
  if DiceSides == 12:
    global d12s
    d12s = list(json_data['result']['random']['data'])
    return(d12s)
  if DiceSides == 10:
    global d10s
    d10s = list(json_data['result']['random']['data'])
    return(d10s)
  if DiceSides == 8:
    global d8s
    d8s = list(json_data['result']['random']['data'])
    return(d8s)
  if DiceSides == 6:
    global d6s
    d6s = list(json_data['result']['random']['data'])
    return(d6s)
  if DiceSides == 4:
    global d4s
    d4s = list(json_data['result']['random']['data'])
    return(d4s)
  if DiceSides == 3:
    global d3s
    d3s = list(json_data['result']['random']['data'])
    return(d3s)
  if DiceSides == 2:
    global d2s
    d2s = list(json_data['result']['random']['data'])
    return(d2s)
  else:
    return()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you ?roll your fate..."))
    print('{0.user} now weaves your fate...'.format(bot))

#bot help command
@bot.command(name='about', help='Responds with info about using the bot')
async def about(ctx):
    helpfile = """
    __**Iscus, The Lady of Our Fate, is a dice bot for Discord**__
      *All rolls are drawn from RANDOM.ORG*
      *See: https://www.random.org/*

    **How to use:**
      > Type a message beginning with ?roll followed by a dice expression. Example: ?roll 1d100
      > A maximum of four combinations of dice and/or modifiers are permitted per roll, in any order, such as ?roll 2d8+2-1d4+1, or ?roll 1d100+1d20+2d10-4d6.  Each factor must be separated by a plus (+) or minus (-) symbol.
      > You can add a comment to a roll by adding a space after the roll expression and typing whatever you want, like: ?roll 1d100 Job Trident(85)
      > Type ?help about or just ?about to see this info later

   **New Features in v2.1:**
      > Added the command ?skill that will calculate your degree of success based on your skill % like: ?skill 46 Swim
      
    **New Features in v2.0:**
      > She now will respond in threads!
      > *roll changed to ?roll to make it one less tap from a mobile phone
      > No more need to type a * before a roll comment, you can now just leave a space like: ?roll 1d100 Job Sanity(92)
      > Now supports minus signs in roll expressions like 2d6+1d4+2-1d3
      > Added support for rolling d2's
      > Better help documentation with ?help and ?help roll
      > Added support for @Iscus ping or ?ping commands (replies if online/alive)
      > Added some error handling to catch fat fingered roll formulas
      > Improved uptime from: 1) Code change to reduce chance of bot going offline due to Discord API rate limiting, 2) Bot now hosted on a Docker container on Job's network, rather than on Replit.com's free service

    **Known issues:**
      > Discord.py v2.x beta library used... Breaking changes may occur when the official version is released
      > Not all error handling cases discovered yet; I'm sure your fat fingers will point out bugs before long...
      > Only these dice types are supported: d100,d20, d12, d10, d8, d6, d4, d3, and d2.  You can't roll a d7 for example.

May Chael ever watch over your rolls and Phyth never weave them for you... Enjoy!
    """
    await ctx.send(helpfile)

#bot roll command
@bot.command(name='roll', help='Responds with a roll result based on the dice or modifier formula input like: ?roll 2d8+1+1d4-1d3')
async def roll(ctx, RollPattern):
  #store each roll factor in a List and test how many factors there are in the RollPattern, a factor being a number of dice like 3d6 or a modifier separated by a + or -
  RollFactors = re.split('(\\+|\\-)', RollPattern)
  FactorCount = int(len(RollFactors))
  #check that there aren't more than the maximum 7 factors (4 rolls or modifiers)
  if 'd' not in RollFactors[0]:
    ErrorMsg = "Your dice expression must begin with a dice roll in the format 1d100, 2d8, 3d6, etc."
    await ctx.send(ErrorMsg)
  if FactorCount > 7:
      ErrorMsg = "Sorry, you may only roll a maximum of 4 dice or modifiers in any combination like: ?roll 1d8+1+1d4+2-1d3"
      await ctx.send(ErrorMsg)
  else: #the roll expression is valid, parse it
    if FactorCount == 1: #there is only one roll factor e.g. 1d100
      DiceNum, DiceSides = RollFactors[0].split('d', 1)
      #check that supported sided dice are being asked for
      if int(DiceSides) in [100, 20, 12, 10, 8, 6, 4, 3, 2]:
        Factor1 = []
        for x in range(0, int(DiceNum)):
          Factor1.append(parse_roll(DiceSides))
        sumFactor1 = sum(Factor1)
        await ctx.send("{} rolls {} = {}".format(ctx.message.author.display_name, Factor1, sumFactor1))
        return
      else: 
        ErrorMsg = "Only d100, d20, d12, d10, d8, d6, d4, d3, d2 are supported."
        await ctx.send(ErrorMsg)
        return
    if FactorCount == 3: #there are two factors joined by a + or - like 1d8+1 or 1d6+1d4
      passFactor = RollFactors[0]
      Factor1 = parse_factor(passFactor)
      passFactor = RollFactors[2]
      Factor2 = parse_factor(passFactor)
      Operator1 = RollFactors[1]
      if Factor1 == 99999 or Factor2 == 99999:
        ErrorMsg = "Only d100, d20, d12, d10, d8, d6, d4, d3, d2 are supported." 
        await ctx.send(ErrorMsg)
        return
      elif "+" in Operator1:
        RollSum = sum(Factor1 + Factor2)
      else: 
        RollSum = int(sum(Factor1)) - int(sum(Factor2))
      await ctx.send("{} rolls {} {} {} = {}".format(ctx.message.author.display_name, Factor1, Operator1, Factor2, RollSum))
      return
    if FactorCount == 5: #there are three factors joined by a + or - like 1d8+1d4-3
      passFactor = RollFactors[0]
      Factor1 = parse_factor(passFactor)
      passFactor = RollFactors[2]
      Factor2 = parse_factor(passFactor)
      passFactor = RollFactors[4]
      Factor3 = parse_factor(passFactor)
      Operator1 = RollFactors[1]
      Operator2 = RollFactors[3]
      if Factor1 == 99999 or Factor2 == 99999 or Factor3 == 99999:
        ErrorMsg = "Only d100, d20, d12, d10, d8, d6, d4, d3, d2 are supported." 
        await ctx.send(ErrorMsg)
        return
      elif "+" in Operator1:
        F1F2Sum = sum(Factor1 + Factor2)
      else: 
        F1F2Sum = int(sum(Factor1)) - int(sum(Factor2))
      if "+" in Operator2:
        RollSum = F1F2Sum + int(sum(Factor3))
      else: 
        RollSum = int(F1F2Sum) - int(sum(Factor3))
      await ctx.send("{} rolls {} {} {} {} {} = {}".format(ctx.message.author.display_name, Factor1, Operator1, Factor2, Operator2, Factor3, RollSum))
      return
    if FactorCount == 7: #there are four factors joined by a + or - like 3d8-1d4+13-1d3
      passFactor = RollFactors[0]
      Factor1 = parse_factor(passFactor)
      passFactor = RollFactors[2]
      Factor2 = parse_factor(passFactor)
      passFactor = RollFactors[4]
      Factor3 = parse_factor(passFactor)
      passFactor = RollFactors[6]
      Factor4 = parse_factor(passFactor)
      Operator1 = RollFactors[1]
      Operator2 = RollFactors[3]
      Operator3 = RollFactors[5]
      if Factor1 == 99999 or Factor2 == 99999 or Factor3 == 99999 or Factor4 == 99999:
        ErrorMsg = "Only d100, d20, d12, d10, d8, d6, d4, d3, d2 are supported." 
        await ctx.send(ErrorMsg)
        return
      elif "+" in Operator1:
        F1F2Sum = sum(Factor1 + Factor2)
      else: 
        F1F2Sum = int(sum(Factor1)) - int(sum(Factor2))
      if "+" in Operator2:
        F1F2F3Sum = F1F2Sum + int(sum(Factor3))
      else: 
        F1F2F3Sum = int(F1F2Sum) - int(sum(Factor3))
      if "+" in Operator3:
        RollSum = F1F2F3Sum + int(sum(Factor4))
      else: 
        RollSum = int(F1F2F3Sum) - int(sum(Factor4))
      await ctx.send("{} rolls {} {} {} {} {} {} {} = {}".format(ctx.message.author.display_name, Factor1, Operator1, Factor2, Operator2, Factor3, Operator3, Factor4, RollSum))
      return
    else: 
      ErrorMsg = "Oops, I think you typed something wrong: your roll should end in a dice or a modifier, not a + or -"
      await ctx.send(ErrorMsg)

#debug functions reply to ping
@bot.command(name='ping', help='Check to see if the bot is listening')
async def ping(ctx):
  messageReply = "I await your actions to reveal your fate..."
  await ctx.send(messageReply)

#bot skill command
@bot.command(name='skill', help='accepts a skill % as a number and responds with the degree of success or failure based on a 1d100 roll.')
async def skill(ctx, Skill):
  #ensure that an integer was entered after the word skill
  try: 
    int(Skill)
  except ValueError:
    messageReply = "To roll vs. your skill you must enter your skill % as a number like ?skill 51"
    await ctx.send(messageReply)
  finally: #roll 1d100 vs the skill
    DiceSides = 100
    Skill = int(Skill)
    Roll = int(parse_roll(DiceSides))
    if Roll <= int(math.ceil(Skill/20)) or Roll == 1: #was a Critical rolled rounding up?
      emoji = '<:crit:872962421097123931>'
      await ctx.send("{} rolls a {}, Critical! {}".format(ctx.message.author.display_name, Roll, emoji))
    elif Roll >= (101-(100-Skill)/20) or Roll==100: #was a Fumble rolled rounding down?
      emoji = '<:fumble:877603035742879804>'
      await ctx.send("{} rolls a {}... {}".format(ctx.message.author.display_name, Roll, emoji)) 
    elif Roll <= int(math.ceil(Skill/5)): #was a Special rolled?
      emoji = '<:special:872964395330863144>'
      await ctx.send("{} rolls a {}, Special! {}".format(ctx.message.author.display_name, Roll, emoji))
    elif Roll <= Skill: #was a Success rolled?
      emoji = ':thumbsup:'
      await ctx.send("{} rolls a {}, Success! {}".format(ctx.message.author.display_name, Roll, emoji)) 
    elif Roll > Skill: #was a Failure rolled?
      emoji = '<:fail:815657879931191337>'
      await ctx.send("{} rolls a {}... {}".format(ctx.message.author.display_name, Roll, emoji)) 
    else:
      messageReply = "Oops, something went wrong"
      await ctx.send(messageReply)

bot.run(os.getenv('TOKEN'))