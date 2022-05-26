import GUIS
import discord
import modFileManager as fm
import asyncio
import discipline as dspln
import re 

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
    
def banEmbed(guildID):
    guildData = fm.getServerData(guildID)
    title = "Discipline Module"
    desc = "Here are the currently temp banned users:"
    for user, strikes in guildData["strikes"].items():
        if strikes == -1:
            desc+= f"\n {user}"
    color = Colors.dark_teal()
    
    banEmbed = discord.Embed(title = title, description = desc, color = color)
    return banEmbed

def banUpdatedEmbed(guildID):
    guildData = fm.getServerData(guildID)
    title = "Discipline Module"
    desc = "Send the Name and Discriminator of the User you would like to Temp-Ban/Un-Temp-Ban(ex. jon#0001)."
    color = Colors.dark_teal()
    
    banUpdatedEmbed = discord.Embed(title = title, description = desc, color = color)
    return banUpdatedEmbed

def muteEmbed(guildID):
    guildData = fm.getServerData(guildID)
    title = "Discipline Module"
    desc = "Here are the currently muted users:"
    for user, strikes in guildData["strikes"].items():
        if strikes < -10:
            desc+= f"\n {user}"
    color = Colors.dark_teal()
    
    muteEmbed = discord.Embed(title = title, description = desc, color = color)
    return muteEmbed

def muteUpdatedEmbed(guildID):
    guildData = fm.getServerData(guildID)
    title = "Discipline Module"
    desc = "Send the Name and Discriminator of the User you would like to Mute/Un-Mute(ex. jon#0001)."
    color = Colors.dark_teal()
    
    muteUpdatedEmbed = discord.Embed(title = title, description = desc, color = color)
    return muteUpdatedEmbed
    

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
    await panel.clear_reactions()
    guildID = rawEventData.guild_id
    channelID = rawEventData.channel_id
    channel = bot.get_channel(rawEventData.channel_id)
    disciplineEmbed = banEmbed(guildID)
    
    await panel.edit(embed = disciplineEmbed)
    
    reactionList  = ['🔨',  '✉', '❌']
    for emoji in reactionList:
        await panel.add_reaction(emoji)
        
    def check(reaction, user):
        return str(reaction)== '🔨' or str(reaction) == '✉' or str(reaction) == '❌' and user != panel.author
    
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
            
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
            
        else:
            if str(reaction) == '🔨':
                updatedEmbed = banUpdatedEmbed(guildID)
                await panel.edit(embed = updatedEmbed)
                await panelTempBan(rawEventData, bot)
                
            elif str(reaction) == '✉':
                updatedEmbed = banUpdatedEmbed(guildID)
                await panel.edit(embed = updatedEmbed)
                await panelUnTempBan(rawEventData, bot)
                
            elif str(reaction) == '❌':
                await GUIS.purgeChannel(rawEventData, bot)
                await disciplinePanel(rawEventData, bot)
                break
            
        await panel.clear_reactions()
        await panel.edit(embed = banEmbed(guildID))
        for emoji in reactionList:
            await panel.add_reaction(emoji)

async def muteRoutine(rawEventData, bot, panel):
    await panel.clear_reactions()
    guildID = rawEventData.guild_id
    channelID = rawEventData.channel_id
    disciplineEmbed = muteEmbed(guildID)
    await panel.edit(embed = disciplineEmbed)
    
    reactionList  = ['🔇',  '🔊', '❌']
    for emoji in reactionList:
        await panel.add_reaction(emoji)
        
    def check(reaction, user):
        return str(reaction)== '🔇' or str(reaction) == '🔊' or str(reaction) == '❌' and user != panel.author
    
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
            
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
            
        else:
            if str(reaction) == '🔇':
                updatedMutePanel = muteUpdatedEmbed(guildID)
                await panel.edit(embed = updatedMutePanel)
                await panelMute(rawEventData, bot)

            elif str(reaction) == '🔊':
                updatedMutePanel = muteUpdatedEmbed(guildID)
                await panel.edit(embed = updatedMutePanel)
                await panelUnMute(rawEventData, bot)

            elif str(reaction) == '❌':
                await GUIS.purgeChannel(rawEventData, bot)
                await disciplinePanel(rawEventData, bot)
                break
        
        await panel.clear_reactions()
        await panel.edit(embed = muteEmbed(guildID))
        for emoji in reactionList:
            await panel.add_reaction(emoji)

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
        try:
            wordsRaw = message.content
            parts = wordsRaw.split(" ")
            user = parts[0]
            userTuple = tuple(user.split("#"))
            numberOfStrikes = int(parts[1])
        except:
            return
        
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
        try:
            wordsRaw = message.content
            parts = wordsRaw.split(" ")
            user = parts[0]
            userTuple = tuple(user.split("#"))
            numberOfStrikes = int(parts[1])
        except:
            return
        
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
    
    
async def panelTempBan(rawEventData, bot):
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    
    try:
        message = await bot.wait_for('message', timeout = 180)
        
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    
    else:
        messageContent = message.content
        parts = re.split("#| ",messageContent)
        userName = parts[0]
        discriminator = parts[1]
        user = ''
        
        #Fetches all members from server
        async for member in guild.fetch_members():
            #Checks if the current iteration of the list "member" matches the given user
            if str(member.name) == userName and str(member.discriminator) == discriminator:
                server_object = fm.getServerData(guildID)
                strikeDict = server_object["strikes"]
                user = member
                #Sets the user's strikes to -1 after theyve been banned
                strikeDict[str(user)] = -1
                fm.storeServerData(server_object)
                break
        for channelPoint in guild.channels:
            if isinstance(channelPoint, discord.TextChannel):
                await channelPoint.set_permissions(user, view_channel=False)
            elif isinstance(channelPoint, discord.VoiceChannel):
                await channelPoint.set_permissions(user, view_channel=False)
        await channel.send(f"{user.mention} has been temporarily banned.")    
    
    
async def panelUnTempBan(rawEventData, bot):
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    
    try:
        message = await bot.wait_for('message', timeout = 180)
        
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    
    else:
        messageContent = message.content
        parts = re.split("#| ",messageContent)
        userName = parts[0]
        discriminator = parts[1]
        user = ''
        
        #Fetches all Members from Server
        async for member in guild.fetch_members():
            #Checks if the current iteration of the list "member" matches the given user
            if str(member.name) == userName and str(member.discriminator) == discriminator:
                server_object = fm.getServerData(guildID)
                strikeDict = server_object["strikes"]
                user = member
                #Sets the user's strikes to 2 after being un-banned
                strikeDict[str(user)] = 2
                #Stores the updated file
                fm.storeServerData(server_object)
                break
            
        for channelPoint in guild.channels:
            if isinstance(channelPoint, discord.TextChannel):
                await channelPoint.set_permissions(user, view_channel=None)
            elif isinstance(channelPoint, discord.VoiceChannel):
                await channelPoint.set_permissions(user, view_channel=None)
        await channel.send(f"{user.mention} has been un-temp-banned.")
        

async def panelMute(rawEventData, bot):
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    
    try:
        message = await bot.wait_for('message', timeout = 180)
        
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    
    else:
        messageContent = message.content
        parts = re.split("#| ",messageContent)
        userName = parts[0]
        discriminator = parts[1]
        user = ''
        
    async for member in guild.fetch_members():
        if str(member.name) == userName and str(member.discriminator) == discriminator:
            server_object = fm.getServerData(guildID)
            strikeDict = server_object["strikes"]
            user = member
            if str(user) in strikeDict:
                strikeDict[str(user)] -= 1000
            else:
                strikeDict[str(user)] = -1000
            fm.storeServerData(server_object)
            break
            
    for channelPoint in guild.channels: #interates over all channels in server
        if isinstance(channelPoint, discord.TextChannel): #if the channel is a text channel
            await channelPoint.set_permissions(user, send_messages=False) #mutes member from writing
        elif isinstance(channelPoint, discord.VoiceChannel): #if the channel is a voice channel
            await channelPoint.set_permissions(user, connect=False) #prevents member from joingin
    # Redundant maybe? If you mute 2 or 3 members it becomes really annoying
    # to scroll back up to the panel to use itg
    await channel.send(f"{user.mention} has been muted") #Bot Message
    
    
async def panelUnMute(rawEventData, bot):
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    
    try:
        message = await bot.wait_for('message', timeout = 180)
        
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    
    else:
        messageContent = message.content
        parts = re.split("#| ",messageContent)
        userName = parts[0]
        discriminator = parts[1]
        user = ''
        
    async for member in guild.fetch_members():
        if str(member.name) == userName and str(member.discriminator) == discriminator:
            server_object = fm.getServerData(guildID)
            strikeDict = server_object["strikes"]
            user = member
            strikeDict[str(user)] += 1000
            fm.storeServerData(server_object)
            break
            
    for channelPoint in guild.channels: #interates over all channels in server
        if isinstance(channelPoint, discord.TextChannel): #if the channel is a text channel
            await channelPoint.set_permissions(user, send_messages=None) #mutes member from writing
        elif isinstance(channelPoint, discord.VoiceChannel): #if the channel is a voice channel
            await channelPoint.set_permissions(user, connect=None) #prevents member from joinging
    # Redundant maybe? If you unmute 2 or 3 members it becomes really annoying
    # to scroll back up to the panel to use it
    # await channel.send(f"{user.mention} has been unmuted") #Bot Message