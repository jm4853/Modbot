import GUIS
import discord
import modFileManager as fm
import asyncio
import discipline as dspln

Colors = discord.Colour


async def disciplinePanel(rawEventData, bot):
    # Gets discord objects from raw data:
    channel = bot.get_channel(rawEventData.channel_id)
    
    title = "Discipline Module"
    desc = "Would you like to:\n1️⃣ - Edit the blacklist.\n2️⃣ - Edit server strikes.\n3️⃣ - Ban or unban members\n4️⃣ - Mute or unmute members."
    color = Colors.dark_teal()
    
    disciplineEmbed = discord.Embed(title = title, description = desc, color = color)
    panel = await channel.send(embed = disciplineEmbed)
    
    reactionList = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '❌']
    for emoji in reactionList:
        await panel.add_reaction(emoji)
    def check(reaction, user):
        #print(str(reaction))
        return str(reaction)== '1️⃣' or str(reaction) == '2️⃣' or str(reaction) == '3️⃣' or str(reaction) == '4️⃣' or str(reaction) == '❌' and user != panel.author
    
    switch = {
        "1️⃣": blacklistRoutine,
        "2️⃣": strikesRoutine,
        "3️⃣": banRoutine,
        "4️⃣": muteRoutine,
        "❌": GUIS.purgeChannel
        }
    
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    else:
        if str(reaction) in switch:
            await switch[str(reaction)](rawEventData, bot, panel)            
        else:
            channel.send("Not a valid emoji.")
            asyncio.sleep(2)
            await GUIS.purgeChannel(rawEventData, bot)
            await disciplinePanel(rawEventData, bot)

def updatedBlacklistEmbed(guildID):
    guildData = fm.getServerData(guildID)
    title = "Discipline Module"
    desc = "Here are the current words on the blacklist:"
    for word in guildData["blacklist"]:
        desc+="\n" + word
    desc+="\nYou can react with ✅ to add words or ⭕ to remove words (❌ to exit)."
    color = Colors.dark_teal()
    
    blacklistEmbed = discord.Embed(title = title, description = desc, color = color)
    return blacklistEmbed

async def blacklistRoutine(rawEventData, bot, panel):
    await panel.clear_reactions()
    guildID = rawEventData.guild_id
    channel = bot.get_channel(rawEventData.channel_id)
    
    disciplineEmbed = updatedBlacklistEmbed(guildID)
    
    await panel.edit(embed = disciplineEmbed)
    
    reactionList = ['✅', '⭕', '❌']
    for emoji in reactionList:
        await panel.add_reaction(emoji)
    
    def check(reaction, user):
        #print(str(reaction))
        return str(reaction)== '✅' or str(reaction) == '⭕' or str(reaction) == '❌' and user != panel.author
    
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
        else:
            if str(reaction) == '✅':
                await panelAddWord(rawEventData, bot)
                await panel.edit(embed = updatedBlacklistEmbed(guildID))

            elif str(reaction) == '⭕':
                await panelRemoveWord(rawEventData, bot)
                await panel.edit(embed = updatedBlacklistEmbed(guildID))

            elif str(reaction) == '❌':
                await GUIS.purgeChannel(rawEventData, bot)
                await disciplinePanel(rawEventData, bot)
        
        await panel.clear_reactions()
        for emoji in reactionList:
            await panel.add_reaction(emoji)
    

def updatedStrikesEmbed(guildID):
    guildData = fm.getServerData(guildID)
    title = "Discipline Module"
    desc = "Here are the current strikes:"
    for user, strikes in guildData["strikes"].items():
        desc+=f"\n{user} has {strikes} strike(s)"
    desc+="\nYou can react with ✅ to add strikes or ⭕ to remove strikes (❌ to exit)."
    color = Colors.dark_teal()
    
    strikesEmbed = discord.Embed(title = title, description = desc, color = color)
    return strikesEmbed

async def strikesRoutine(rawEventData, bot, panel):
    await panel.clear_reactions()
    guildID = rawEventData.guild_id
    channel = bot.get_channel(rawEventData.channel_id)
    
    disciplineEmbed = updatedStrikesEmbed(guildID)
    
    await panel.edit(embed = disciplineEmbed)
    
    reactionList = ['✅', '⭕', '❌']
    for emoji in reactionList:
        await panel.add_reaction(emoji)
    
    def check(reaction, user):
        #print(str(reaction))
        return str(reaction)== '✅' or str(reaction) == '⭕' or str(reaction) == '❌' and user != panel.author
    
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
        else:
            if str(reaction) == '✅':
                await panelAddStrike(rawEventData, bot)
                await panel.edit(embed = updatedStrikesEmbed(guildID))

            elif str(reaction) == '⭕':
                await panelRemoveStrike(rawEventData, bot)
                await panel.edit(embed = updatedStrikesEmbed(guildID))

            elif str(reaction) == '❌':
                await GUIS.purgeChannel(rawEventData, bot)
                await disciplinePanel(rawEventData, bot)
        
        await panel.clear_reactions()
        for emoji in reactionList:
            await panel.add_reaction(emoji)



async def banRoutine(rawEventData, bot, panel):
    guildID = rawEventData.guild_id
    channelID = rawEventData.channel_id
    
    
    await GUIS.purgeChannel(rawEventData, bot)
    await disciplinePanel(rawEventData, bot)

async def muteRoutine(rawEventData, bot, panel):
    guildID = rawEventData.guild_id
    channelID = rawEventData.channel_id
    
    
    await GUIS.purgeChannel(rawEventData, bot)
    await disciplinePanel(rawEventData, bot)


def inServer(members, lookFor):
    for member in members:
        if member.name == lookFor[0]:
            if member.discriminator == lookFor[1]:
                return True
    return False

async def panelAddStrike(rawEventData, bot):
    guildID = rawEventData.guild_id
    guildObj = bot.get_guild(rawEventData.guild_id)
    members = guildObj.members
    
    channel = bot.get_channel(rawEventData.channel_id)
    # Gets the stored data from getServerData
    server_object = fm.getServerData(guildID)
    # Sets strikeDict to the dictionary stored at key "strikes"
    strikeDict = server_object["strikes"]
    
    await channel.send("Enter the user you would like to add strikes too, followed by the number of strikes. Ex: user#1234 1")
    try: 
        message = await bot.wait_for('message', timeout = 180)
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    else:
        wordsRaw = message.content
        parts = wordsRaw.split(" ")
        user = parts[0]
        userTuple = tuple(user.split("#"))
        numberOfStrikes = int(parts[1])
        
        # Gets server data
        server_object = fm.getServerData(guildID)
        
        if inServer(members, userTuple):       
            for strike in range(numberOfStrikes):
                # If this user has not gotten any other strikes, it adds them
                if not str(user) in strikeDict.keys():
                    strikeDict.update({str(user): 1})
                # If they are in the dict than it just adds 1
                else:
                    strikeDict[str(user)] += 1

            # Sets the value of strikes to the strike dictionary
            server_object["strikes"] = strikeDict

            # Sends server dictionary back the be stored
            fm.storeServerData(server_object)
            # Once strikes are stored check for possible kick/ban
            await dspln.enforceStrikes(channel, user, strikeDict)
            
            if numberOfStrikes == 1:
                await channel.send('Added 1 strike to ' + str(user))
            else:
                await channel.send('Added ' + str(numberOfStrikes) + ' strikes to ' + str(user))
        
        
        


async def panelRemoveStrike(rawEventData, bot):
    guildID = rawEventData.guild_id
    guildObj = bot.get_guild(rawEventData.guild_id)
    members = guildObj.members
    
    channel = bot.get_channel(rawEventData.channel_id)
    # Gets the stored data from getServerData
    server_object = fm.getServerData(guildID)
    # Sets strikeDict to the dictionary stored at key "strikes"
    strikeDict = server_object["strikes"]
    
    await channel.send("Enter the user you would like to remove strikes from, followed by the number of strikes. Ex: user#1234 1")
    try: 
        message = await bot.wait_for('message', timeout = 180)
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    else:
        wordsRaw = message.content
        parts = wordsRaw.split(" ")
        user = parts[0]
        userTuple = tuple(user.split("#"))
        numberOfStrikes = int(parts[1])
        
        # Gets server data
        server_object = fm.getServerData(guildID)
        strikeDict = server_object["strikes"]
        
        if not str(user) in strikeDict.keys():
            await channel.send(f"{user} has no strikes.")
        else:
            if int(numberOfStrikes) > int(strikeDict[user]):
                await channel.send(f"Remove {strikeDict[user]} strike(s) from {user}")
                strikeDict[user] = 0
            else:
                await channel.send(f"Remove {numberOfStrikes} strike(s) from {user}")
                strikeDict[user]-=numberOfStrikes

            # Sets the value of strikes to the strike dictionary
            server_object["strikes"] = strikeDict

            # Sends server dictionary back the be stored
            fm.storeServerData(server_object)
            # Once strikes are stored check for possible kick/ban
            await dspln.enforceStrikes(channel, user, strikeDict)






async def panelAddWord(rawEventData, bot):
    # get variables
    guildID = rawEventData.guild_id
    channel = bot.get_channel(rawEventData.channel_id)
    await channel.send("Enter the words you would like to add to the blacklist (separated by a space).")
    
    try: 
        message = await bot.wait_for('message', timeout = 180)
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    else:
        wordsRaw = message.content
        
        # Gets server data
        server_object = fm.getServerData(guildID)
        
        #Splits the words via spaces
        wordsList = wordsRaw.split(' ')
        
        blackList = server_object["blacklist"]
        
        #Iterates through the list of words and appends each one to the blacklist seperately 
        for word in wordsList:
            blackList.append(word)
            

        # Sets the object data for blacklist to new blacklist
        server_object["blacklist"] = blackList

        # Stores data
        fm.storeServerData(server_object)
        
        

async def panelRemoveWord(rawEventData, bot):
    # get variables
    guildID = rawEventData.guild_id
    channel = bot.get_channel(rawEventData.channel_id)
    await channel.send("Enter the words you would like to remove from the blacklist (separated by a space).")
    
    try: 
        message = await bot.wait_for('message', timeout = 180)
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    else:
        wordsRaw = message.content
        
        # Gets server data
        server_object = fm.getServerData(guildID)
        
        #Splits the words via spaces
        wordsList = wordsRaw.split(' ')
        
        blacklist = server_object["blacklist"]
        
        #Iterates through the list of words and appends each one to the blacklist seperately 
        for word in wordsList:
            if word in blacklist:
                blacklist.pop(word)
            else:
                channel.send(f"The word \"{word}\" is not in the blacklist.")

        # Sets the object data for blacklist to new blacklist
        server_object["blacklist"] = blacklist

        # Stores data
        fm.storeServerData(server_object)