import discord
import os
import requests
import json
import re
from replit import db
from keep_alive import keep_alive

client = discord.Client()

#call out to random.org to get 100 new 1d100 rolls once DB of previous 100 rolls is exhausted
def roll_d100():
  if "d100" not in db.keys():
    db["d100"] = list()
  d100x100 = db["d100"]
  if d100x100 == []: 
    IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
    APIkey = os.getenv('KEY')
    response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':100,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
    json_data = json.loads(response.text)
    # UNCOMMENT BELOW TO SHOW THE JSON OUTPUT PRETTIFIED
    #print(json.dumps(json_data, sort_keys=True, indent=4, separators=(',', ':')))
    d100x100 = str(json_data['result']['random']['data'])
    store_d100(d100x100)
    return(d100x100)
  else:
    d100x100 = str(db["d100"])
    return(d100x100)
#store the 100 new 1d100 rolls in the database
def store_d100(d100x100):
  if "d100" in db.keys():
    d100 = db["d100"]
    d100.append(d100x100)
    db["d100"] = d100
    #print(d100)
  else:
    db["d100"] = [d100x100]
#below removes the last roll shown in Discord from the database so the next roll chooses the next list value in the database key d100
def delete_d100(d100):
  d100 = d100.split(",")
  del d100[0]
  db["d100"] = d100
#The function below accepts number of dice and rolls that many d100, calling the functions above to remove those rolls from the database, and returns the value of the rolls as a list to the message parser
def roll_xd100(DiceNum):
  result = []
  for i in range(int(DiceNum)):
    d100 = roll_d100()#get all d100 rolls from database
    if "d100" in db.keys():# clean up list
      d100 = d100.replace("[", "")
      d100 = d100.replace("'", "")
      d100 = d100.replace("]", "")
      roll = int(d100.split(",")[0])#use the first d100 roll in the database
      delete_d100(d100)#delete the used roll from the database
      result.append(roll)
  return result

#call out to random.org to get 100 new 1d20 rolls once DB of previous 100 rolls is exhausted
def roll_d20():
  if "d20" not in db.keys():
    db["d20"] = list()
  d20x100 = db["d20"]
  #print(d20x100)
  if d20x100 == []: 
    IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
    APIkey = os.getenv('KEY')
    response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':20,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
    json_data = json.loads(response.text)
    d20x100 = str(json_data['result']['random']['data'])
    store_d20(d20x100)
    return(d20x100)
  else:
    d20x100 = str(db["d20"])
    return(d20x100)
#store the 100 new 1d20 rolls in the database
def store_d20(d20x100):
  if "d20" in db.keys():
    d20 = db["d20"]
    d20.append(d20x100)
    db["d20"] = d20
    #print(d20)
  else:
    db["d20"] = [d20x100]
#remove the used d20 roll from the database
def delete_d20(d20):
  d20 = d20.split(",")
  del d20[0]
  db["d20"] = d20
#The function below accepts number of dice and rolls that many d20, calling the functions above to remove those rolls from the database, and returns the value of the rolls as a list to the message parser
def roll_xd20(DiceNum):
  result = []
  for i in range(int(DiceNum)):
    d20 = roll_d20()#get all d20 rolls from database
    if "d20" in db.keys():# clean up list
      d20 = d20.replace("[", "")
      d20 = d20.replace("'", "")
      d20 = d20.replace("]", "")
      roll = int(d20.split(",")[0])#use the first d20 roll in the database
      delete_d20(d20)#delete the used roll from the database
      result.append(roll)
  return result

#call out to random.org to get 100 new 1d12 rolls once DB of previous 100 rolls is exhausted
def roll_d12():
  if "d12" not in db.keys():
    db["d12"] = list()
  d12x100 = db["d12"]
  #print(d12x100)
  if d12x100 == []: 
    IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
    APIkey = os.getenv('KEY')
    response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':12,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
    json_data = json.loads(response.text)
    d12x100 = str(json_data['result']['random']['data'])
    store_d12(d12x100)
    return(d12x100)
  else:
    d12x100 = str(db["d12"])
    return(d12x100)
#store the 100 new 1d12 rolls in the database
def store_d12(d12x100):
  if "d12" in db.keys():
    d12 = db["d12"]
    d12.append(d12x100)
    db["d12"] = d12
    #print(d12)
  else:
    db["d12"] = [d12x100]
#remove the used d12 roll from the database
def delete_d12(d12):
  d12 = d12.split(",")
  del d12[0]
  db["d12"] = d12
#roll a set number of d12 as called by Discord message parser
def roll_xd12(DiceNum):
  result = []
  for i in range(int(DiceNum)):
    d12 = roll_d12()#get all d12 rolls from database
    if "d12" in db.keys():# clean up list
      d12 = d12.replace("[", "")
      d12 = d12.replace("'", "")
      d12 = d12.replace("]", "")
      roll = int(d12.split(",")[0])#use the first d12 roll in the database
      delete_d12(d12)#delete the used roll from the database
      result.append(roll)
  return result

#call out to random.org to get 100 new 1d10 rolls once DB of previous 100 rolls is exhausted
def roll_d10():
  if "d10" not in db.keys():
    db["d10"] = list()
  d10x100 = db["d10"]
  #print(d10x100)
  if d10x100 == []: 
    IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
    APIkey = os.getenv('KEY')
    response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':10,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
    json_data = json.loads(response.text)
    d10x100 = str(json_data['result']['random']['data'])
    store_d10(d10x100)
    return(d10x100)
  else:
    d10x100 = str(db["d10"])
    return(d10x100)
#store the 100 new 1d10 rolls in the database
def store_d10(d10x100):
  if "d10" in db.keys():
    d10 = db["d10"]
    d10.append(d10x100)
    db["d10"] = d10
    #print(d10)
  else:
    db["d10"] = [d10x100]
#remove the used d10 roll from the database
def delete_d10(d10):
  d10 = d10.split(",")
  del d10[0]
  db["d10"] = d10
#roll a set number of d10 as called by Discord message parser
def roll_xd10(DiceNum):
  result = []
  for i in range(int(DiceNum)):
    d10 = roll_d10()#get all d10 rolls from database
    if "d10" in db.keys():# clean up list
      d10 = d10.replace("[", "")
      d10 = d10.replace("'", "")
      d10 = d10.replace("]", "")
      roll = int(d10.split(",")[0])#use the first d10 roll in the database
      delete_d10(d10)#delete the used roll from the database
      result.append(roll)
  return result

#call out to random.org to get 100 new 1d8 rolls once DB of previous 100 rolls is exhausted
def roll_d8():
  if "d8" not in db.keys():
    db["d8"] = list()
  d8x100 = db["d8"]
  #print(d8x100)
  if d8x100 == []: 
    IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
    APIkey = os.getenv('KEY')
    response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':8,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
    json_data = json.loads(response.text)
    d8x100 = str(json_data['result']['random']['data'])
    store_d8(d8x100)
    return(d8x100)
  else:
    d8x100 = str(db["d8"])
    return(d8x100)
#store the 100 new 1d8 rolls in the database
def store_d8(d8x100):
  if "d8" in db.keys():
    d8 = db["d8"]
    d8.append(d8x100)
    db["d8"] = d8
    #print(d8)
  else:
    db["d8"] = [d8x100]
#remove the used d8 roll from the database
def delete_d8(d8):
  d8 = d8.split(",")
  del d8[0]
  db["d8"] = d8
#roll a set number of d8 as called by Discord message parser
def roll_xd8(DiceNum):
  result = []
  for i in range(int(DiceNum)):
    d8 = roll_d8()#get all d8 rolls from database
    if "d8" in db.keys():# clean up list
      d8 = d8.replace("[", "")
      d8 = d8.replace("'", "")
      d8 = d8.replace("]", "")
      roll = int(d8.split(",")[0])#use the first d8 roll in the database
      delete_d8(d8)#delete the used roll from the database
      result.append(roll)
  return result

#call out to random.org to get 100 new 1d6 rolls once DB of previous 100 rolls is exhausted
def roll_d6():
  if "d6" not in db.keys():
    db["d6"] = list()
  d6x100 = db["d6"]
  #print(d6x100)
  if d6x100 == []: 
    IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
    APIkey = os.getenv('KEY')
    response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':6,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
    json_data = json.loads(response.text)
    d6x100 = str(json_data['result']['random']['data'])
    store_d6(d6x100)
    return(d6x100)
  else:
    d6x100 = str(db["d6"])
    return(d6x100)
#store the 100 new 1d6 rolls in the database
def store_d6(d6x100):
  if "d6" in db.keys():
    d6 = db["d6"]
    d6.append(d6x100)
    db["d6"] = d6
    #print(d6)
  else:
    db["d6"] = [d6x100]
#remove the used d6 roll from the database
def delete_d6(d6):
  d6 = d6.split(",")
  del d6[0]
  db["d6"] = d6
#roll a set number of d6 as called by Discord message parser
def roll_xd6(DiceNum):
  result = []
  for i in range(int(DiceNum)):
    d6 = roll_d6()#get all d6 rolls from database
    if "d6" in db.keys():# clean up list
      d6 = d6.replace("[", "")
      d6 = d6.replace("'", "")
      d6 = d6.replace("]", "")
      roll = int(d6.split(",")[0])#use the first d6 roll in the database
      delete_d6(d6)#delete the used roll from the database
      result.append(roll)
  return result

#call out to random.org to get 100 new 1d4 rolls once DB of previous 100 rolls is exhausted
def roll_d4():
  if "d4" not in db.keys():
    db["d4"] = list()
  d4x100 = db["d4"]
  #print(d4x100)
  if d4x100 == []: 
    IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
    APIkey = os.getenv('KEY')
    response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':4,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
    json_data = json.loads(response.text)
    d4x100 = str(json_data['result']['random']['data'])
    store_d4(d4x100)
    return(d4x100)
  else:
    d4x100 = str(db["d4"])
    return(d4x100)
#store the 100 new 1d4 rolls in the database
def store_d4(d4x100):
  if "d4" in db.keys():
    d4 = db["d4"]
    d4.append(d4x100)
    db["d4"] = d4
    #print(d4)
  else:
    db["d4"] = [d4x100]
#remove the used d4 roll from the database
def delete_d4(d4):
  d4 = d4.split(",")
  del d4[0]
  db["d4"] = d4
#roll a set number of d4 as called by Discord message parser
def roll_xd4(DiceNum):
  result = []
  for i in range(int(DiceNum)):
    d4 = roll_d4()#get all d4 rolls from database
    if "d4" in db.keys():# clean up list
      d4 = d4.replace("[", "")
      d4 = d4.replace("'", "")
      d4 = d4.replace("]", "")
      roll = int(d4.split(",")[0])#use the first d4 roll in the database
      delete_d4(d4)#delete the used roll from the database
      result.append(roll)
  return result

#call out to random.org to get 100 new 1d3 rolls once DB of previous 100 rolls is exhausted
def roll_d3():
  if "d3" not in db.keys():
    db["d3"] = list()
  d3x100 = db["d3"]
  #print(d3x100)
  if d3x100 == []: 
    IscusHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain', 'User-Agent': 'Iscus Discord Bot, joshsays@gmail.com'}
    APIkey = os.getenv('KEY')
    response = requests.post('https://api.random.org/json-rpc/2/invoke', json={'jsonrpc':'2.0','method':'generateIntegers','params':{'apiKey':APIkey,'n':100,'min':1,'max':3,'replacement':True,'base':10},'id':42},headers=IscusHeaders)
    json_data = json.loads(response.text)
    d3x100 = str(json_data['result']['random']['data'])
    store_d3(d3x100)
    return(d3x100)
  else:
    d3x100 = str(db["d3"])
    return(d3x100)
#store the 100 new 1d3 rolls in the database
def store_d3(d3x100):
  if "d3" in db.keys():
    d3 = db["d3"]
    d3.append(d3x100)
    db["d3"] = d3
    #print(d3)
  else:
    db["d3"] = [d3x100]
#remove the used d3 roll from the database
def delete_d3(d3):
  d3 = d3.split(",")
  del d3[0]
  db["d3"] = d3
#roll a set number of d3 as called by Discord message parser
def roll_xd3(DiceNum):
  result = []
  for i in range(int(DiceNum)):
    d3 = roll_d3()#get all d3 rolls from database
    if "d3" in db.keys():# clean up list
      d3 = d3.replace("[", "")
      d3 = d3.replace("'", "")
      d3 = d3.replace("]", "")
      roll = int(d3.split(",")[0])#use the first d3 roll in the database
      delete_d3(d3)#delete the used roll from the database
      result.append(roll)
  return result

@client.event
async def on_ready():
  print('{0.user} now weaves your fate...'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you *roll your fate..."))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  user = message.author.display_name

#parse user roll formula
  if msg == "*roll help":
    helpfile = """
    __**Iscus, The Lady of Our Fate, is a dice bot for Discord**__
      *All rolls are drawn from RANDOM.ORG*
      *See: https://www.random.org/*

    **How to use:**
      > Type a message beginning with *roll followed by a dice expression (that's an asterisk, or shift+8 on your keyboard before the word roll). Example: *roll 1d100
      > A maximum of four combinations of dice and/or modifiers are permitted per roll, in any order, such as *roll 2d8+2+1d4+1, or *roll 1d100+1d20+2d10+4d6.  Each factor must be separated by a plus (+) symbol.
      > You can add a comment to a roll by adding a space and an asterisk after the roll expression so everyone knows what you're rolling for before the result is known, all in one line, like: *roll 1d100 *Job Trident(85)
      > Type *roll help to see this info later

    **Known issues:**
      > No error handling built in yet... If you type sloppy she won't respond.  Spaces matter, BRIAN and PAUL :)
      > Dice expressions with minuses in them, like *roll 1d3-1, aren't (yet) supported
      > Only standard dice types are supported, e.g. d100,d20, d12, d10, d8, d6, d4.  You can't roll a d7 for example. Exception: d3 has now been added.

May Chael ever watch over your rolls and Phyth never weave them for you... Enjoy!
    """
    await message.channel.send(helpfile)

# Export all d100 rolls in the database (debugging)
  if msg == "*roll d100dump":
    value = db["d100"]
    await message.channel.send(value)
    return
    
# main listener
  if msg.startswith("*roll "):
    comment = 0
    for i in msg: 
      if i == '*': 
        comment = comment + 1
    if comment > 1:
      #this means that the message has a comment
      prefix, FactorsPlusComment = msg.split('*roll ', 1)
      Factors, Commentxt = FactorsPlusComment.split(' *', 1)
      #Factors now holds just the roll expression
    else: 
        dumpStat, Factors = msg.split('*roll ', 1)
    countplus = 0
    for i in Factors: 
      if i == '+': 
        countplus = countplus + 1
    countminus = 0
    for i in Factors: 
      if i == '-': 
        countminus = countminus + 1
    NumFactors = countplus + countminus
    #NumFactors how holds the total number of + or - in the dice expression
    """ 
    if user == "Dom":
      await message.channel.send('Iscus is offended by your disparaging remarks about her and refuses to answer your prayers.  Instead, your fate must now be goverened by pseudo-random rolls of Dice Maiden or Dice Golem, good luck...')
      return
    
    if user == "The Rust":
      await message.channel.send('That bitch Ulrik is fired. https://discord.com/channels/723614458676641943/735513833598091344/836479435389534228  Iscus ignores his prayers and his fate must now be goverened by the pseudo-random rolls of Dice Maiden or Dice Golem, good luck...')
      return
   """
    if NumFactors == 3: 
      #this is the most complex expression supported, something like *roll 2d6+2+1d4-1 * some comment
        minus = re.compile('-') 
        if(minus.search(Factors) == None): 
          #test that the expression doesn't contain a minus, and if id doesn't break it into each part
          FactorOne, FactorTwo, FactorThree, FactorFour = re.split('\\+', Factors, 4)
          if "d" in FactorOne: #FactorOne is a dice roll, find how many of what size
              DiceNum, DiceType = FactorOne.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorOne = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorOne = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorOne = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorOne = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorOne = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorOne = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorOne = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorOne = roll_xd3(DiceNum)
          #else: #FactorOne is a modifier, not a roll
          if "d" in FactorTwo: #FactorTwo is a dice roll, find how many of what size
              DiceNum, DiceType = FactorTwo.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorTwo = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorTwo = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorTwo = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorTwo = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorTwo = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorTwo = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorTwo = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorTwo = roll_xd3(DiceNum)                
          #else: #FactorTwo is a modifier, not a roll
          if "d" in FactorThree: #FactorThree is a dice roll, find how many of what size
              DiceNum, DiceType = FactorThree.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorThree = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorThree = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorThree = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorThree = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorThree = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorThree = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorThree = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorThree = roll_xd3(DiceNum)                
          #else: #FactorThree is a modifier, not a roll
          if "d" in FactorFour: #FactorFour is a dice roll, find how many of what size
              DiceNum, DiceType = FactorFour.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorFour = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorFour = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorFour = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorFour = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorFour = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorFour = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorFour = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorFour = roll_xd3(DiceNum)                
          #else: #FactorFour is a modifier, not a roll
        else:
          await message.channel.send('sorry, minuses are not currently supported because Job got lazy and did not finish coding this bot')
          return
        #tally up the results and send output to Discord
        """
        print(FactorOne)
        print(type(FactorOne))
        print(FactorTwo)
        print(type(FactorThree))
        print(FactorThree)
        print(type(FactorFour))
        print(FactorFour)
        print(type(FactorFour))
        """        
        if type(FactorOne) is list:
            sumFactorOne = sum(FactorOne)
        else: 
            sumFactorOne = FactorOne
        if type(FactorTwo) is list:
            sumFactorTwo = sum(FactorTwo)
        else: 
            sumFactorTwo = FactorTwo
        if type(FactorThree) is list:
            sumFactorThree = sum(FactorThree)
        else: 
            sumFactorThree = FactorThree
        if type(FactorFour) is list:
            sumFactorFour = sum(FactorFour)
        else: 
            sumFactorFour = FactorFour           
        RollSum = int(sumFactorOne)+int(sumFactorTwo)+int(sumFactorThree)+int(sumFactorFour)
        FactorOne = str(FactorOne)
        FactorTwo = str(FactorTwo)
        FactorThree = str(FactorThree)
        FactorFour = str(FactorFour)
        returnroll = str(user) + " rolls " + FactorOne + "+" + FactorTwo + "+" + FactorThree + "+" + FactorFour + " = " + str(RollSum)
        await message.channel.send(returnroll)
        return

    if NumFactors == 2:
        #this is the second-most complex expression supported, something like *roll 2d6+2+1d4 * some comment
        #print('3 factors') 
        minus = re.compile('-') 
        if(minus.search(Factors) == None): 
          #test that the expression doesn't contain a minus, and if id doesn't break it into each part
          FactorOne, FactorTwo, FactorThree = re.split('\\+', Factors, 3)
          if "d" in FactorOne: #FactorOne is a dice roll, find how many of what size
              DiceNum, DiceType = FactorOne.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorOne = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorOne = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorOne = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorOne = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorOne = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorOne = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorOne = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorOne = roll_xd3(DiceNum)                
          #else: #FactorOne is a modifier, not a roll
          if "d" in FactorTwo: #FactorTwo is a dice roll, find how many of what size
              DiceNum, DiceType = FactorTwo.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorTwo = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorTwo = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorTwo = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorTwo = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorTwo = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorTwo = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorTwo = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorTwo = roll_xd3(DiceNum)                
          #else: #FactorTwo is a modifier, not a roll
          if "d" in FactorThree: #FactorThree is a dice roll, find how many of what size
              DiceNum, DiceType = FactorThree.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorThree = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorThree = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorThree = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorThree = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorThree = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorThree = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorThree = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorThree = roll_xd3(DiceNum)                
          #else: #FactorThree is a modifier, not a roll
        else:
          await message.channel.send('sorry, minuses are not currently supported because Job got lazy and did not finish coding this bot')
          return
        #tally up the results and send output to Discord
        if type(FactorOne) is list:
            sumFactorOne = sum(FactorOne)
        else: 
            sumFactorOne = FactorOne
        if type(FactorTwo) is list:
            sumFactorTwo = sum(FactorTwo)
        else: 
            sumFactorTwo = FactorTwo
        if type(FactorThree) is list:
            sumFactorThree = sum(FactorThree)
        else: 
            sumFactorThree = FactorThree   
        RollSum = int(sumFactorOne)+int(sumFactorTwo)+int(sumFactorThree)
        FactorOne = str(FactorOne)
        FactorTwo = str(FactorTwo)
        FactorThree = str(FactorThree)
        returnroll = str(user) + " rolls " + FactorOne + "+" + FactorTwo + "+" + FactorThree  + " = " + str(RollSum)
        await message.channel.send(returnroll)
        return     

    if NumFactors == 1:
        #this is the third-most complex expression supported, something like *roll 2d6+2 * some comment
        #print('2 factors')  
        minus = re.compile('-') 
        if(minus.search(Factors) == None): 
          #test that the expression doesn't contain a minus, and if id doesn't break it into each part
          FactorOne, FactorTwo = re.split('\\+', Factors, 2)
          if "d" in FactorOne: #FactorOne is a dice roll, find how many of what size
              DiceNum, DiceType = FactorOne.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorOne = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorOne = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorOne = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorOne = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorOne = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorOne = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorOne = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorOne = roll_xd3(DiceNum)                
          #else: #FactorOne is a modifier, not a roll
          if "d" in FactorTwo: #FactorTwo is a dice roll, find how many of what size
              DiceNum, DiceType = FactorTwo.split('d', 1)
              DiceType = int(DiceType)
              DiceNum = int(DiceNum)
              if DiceType == 100:
                FactorTwo = roll_xd100(DiceNum)
              if DiceType == 20:
                FactorTwo = roll_xd20(DiceNum)
              if DiceType == 12:
                FactorTwo = roll_xd12(DiceNum)
              if DiceType == 10:
                FactorTwo = roll_xd10(DiceNum)
              if DiceType == 8:
                FactorTwo = roll_xd8(DiceNum)
              if DiceType == 6:
                FactorTwo = roll_xd6(DiceNum)
              if DiceType == 4:
                FactorTwo = roll_xd4(DiceNum)
              if DiceType == 3:
                FactorTwo = roll_xd3(DiceNum)                
          #else: #FactorTwo is a modifier, not a roll
        else:
          await message.channel.send('sorry, minuses are not currently supported because Job got lazy and did not finish coding this bot')
          return
        #tally up the results and send output to Discord
        if type(FactorOne) is list:
            sumFactorOne = sum(FactorOne)
        else: 
            sumFactorOne = FactorOne
        if type(FactorTwo) is list:
            sumFactorTwo = sum(FactorTwo)
        else: 
            sumFactorTwo = FactorTwo
        RollSum = int(sumFactorOne)+int(sumFactorTwo)
        FactorOne = str(FactorOne)
        FactorTwo = str(FactorTwo)
        returnroll = str(user) + " rolls " + FactorOne + "+" + FactorTwo + " = " + str(RollSum)
        await message.channel.send(returnroll)
        return  

    if NumFactors == 0:
      #this is the simplest expression supported, something like *roll 2d6 * some comment
      #print('1 factors')
      FactorOne = Factors 
      if "d" in FactorOne: #FactorOne is a dice roll, find how many of what size
        DiceNum, DiceType = FactorOne.split('d', 1)
        DiceType = int(DiceType)
        DiceNum = int(DiceNum)
        if DiceType == 100:
          FactorOne = roll_xd100(DiceNum)
        if DiceType == 20:
          FactorOne = roll_xd20(DiceNum)
        if DiceType == 12:
          FactorOne = roll_xd12(DiceNum)
        if DiceType == 10:
          FactorOne = roll_xd10(DiceNum)
        if DiceType == 8:
          FactorOne = roll_xd8(DiceNum)
        if DiceType == 6:
          FactorOne = roll_xd6(DiceNum)
        if DiceType == 4:
          FactorOne = roll_xd4(DiceNum)
        if DiceType == 3:
          FactorOne = roll_xd3(DiceNum)        
      #else: #FactorOne is a modifier, not a roll
      #tally up the results and send output to Discord
      if type(FactorOne) is list:
        sumFactorOne = sum(FactorOne)
      else: 
        sumFactorOne = FactorOne
      RollSum = int(sumFactorOne)
      FactorOne = str(FactorOne)
      returnroll = str(user) + " rolls " + FactorOne + " = " + str(RollSum)
      await message.channel.send(returnroll)
      return  

"""
#below is a debug function to show the values that remain in the d100 database key after a roll is shown and a value deleted
  if msg.startswith("*list_d100"):
    d100 = []
    if "d100" in db.keys():
      d100 = str(db["d100"])
    d100 = d100.replace("[", "")
    d100 = d100.replace("'", "")
    d100 = d100.replace("]", "")
    await message.channel.send(d100)
"""
keep_alive()
client.run(os.getenv('TOKEN'))