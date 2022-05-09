import discord
import modFileManager as fm
import asyncio


# Behavior

async def enforceBlackList(message):
    # Gets string from message
    words = message.content
    # Gets server blacklist
    serverData = fm.getServerData(message.guild.id)
    blacklist = serverData["blacklist"]
    # Tries to split the string up by space
    if " " in words:
        words = words.split(" ")
        # Loops through each list of words to detect any on the black list
        print("out loop")
        print(words)
        if not message.content.startswith('$removeWord'):
            print('in loop')
            for word in words:
                for badword in blacklist:
                    print("In loop")
                    # If word is on blacklist
                    if word == badword:
                        await message.channel.send("That was a bad word")
                        await addStrike(message, message.author)
                        # Function returns true to signify that it was successful
                        return True
    else:
        # This case is if its only a single word
        for badword in blacklist:
            if words == badword:
                await message.channel.send("That was a bad word")
                await addStrike(message, message.author)
                return True
    # Returns false if word isnt on blacklist
    return False


async def enforceStrikes(ctx, user, strikeDict):
    # Checks that the user has strikes
    if str(user) in strikeDict.keys():
        # Gets a member object so we can use the kick/ban methods
        # Kick after 3 strikes
        if strikeDict[str(user)] >= 3:
            await user.kick()
            await ctx.channel.send(f"{user} was kicked")
        # Ban after 6 strikes
        elif strikeDict[str(user)] >= 6:
            await user.ban()
            await ctx.channel.send(f"{user} was banned")

# This is to add strikes without commands
async def giveStrike():
    pass









# Commands

async def getStrikes(ctx, user: discord.Member):
    guildID = str(ctx.guild.id)
    # Gets the stored data from getServerData
    server_object = fm.getServerData(guildID)

    # Sets strikeDict to the dictionary stored at key "strikes"
    strikeDict = server_object["strikes"]

    # Checks if user is in strike dict
    if not str(user) in strikeDict.keys():
        await ctx.send(f"The user {user} has 0 strikes")
    else:
        # If user is in dict prints number of strikes
        await ctx.send(f"The user {user} has {strikeDict[str(user)]} strikes")



async def addStrike(ctx, user: discord.Member):
    guildID = str(ctx.guild.id)
    # Gets the stored data from getServerData
    server_object = fm.getServerData(guildID)

    # Sets strikeDict to the dictionary stored at key "strikes"
    strikeDict = server_object["strikes"]
    
    messageList = ctx.message.content.split()
    
    numberOfStrikes = int(messageList[2])
    
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
    await enforceStrikes(ctx, user, strikeDict)
    
    if numberOfStrikes == 1:
        await ctx.channel.send('Added 1 strike to ' + str(user))
    else:
        await ctx.channel.send('Added ' + str(numberOfStrikes) + ' strikes to ' + str(user))



async def removeStrike(ctx, user: discord.Member):
    guildID = str(ctx.guild.id)
    # Gets the stored data from getServerData
    server_object = fm.getServerData(guildID)

    # Sets strikeDict to the dictionary stored at key "strikes"
    strikeDict = server_object["strikes"]
    
    messageList = ctx.message.content.split()
    
    numberOfStrikes = int(messageList[2])
    
    # Checks that the user has gotten a strike before
    if not str(user) in strikeDict.keys():
        await ctx.channel.send("This user already has 0 strikes")
    else:
        for strike in range(numberOfStrikes):
            # If the user has 0 strikes already it will remove none
            if strikeDict[str(user)] <= 0:
                print('\nin loop if\n')
                await ctx.channel.send("This user has no strikes")
            else:
                print('\nin loop else\n')
                strikeDict[str(user)] -= 1
        if numberOfStrikes == 1:
            await ctx.send('Removed 1 strike from ' + str(user))
        else:
            await ctx.send('Removed ' + str(numberOfStrikes) + ' strikes from ' + str(user))

    # Sets the value of strikes to the strike dictionary
    server_object["strikes"] = strikeDict

    # Sends server dictionary back the be stored
    fm.storeServerData(server_object)



async def addWord(ctx):
    # get variables
    guildID = str(ctx.guild.id)
    # Gets server data
    server_object = fm.getServerData(guildID)

    # Stores list from server object to blacklist, then appends the words to it
    
    #Gets the message data from the ctx object "words"
    words = ctx.message
    
    #Gets the string of the message from the message data
    wordsContent = words.content
    
    #Splits the words via spaces
    wordsSplit = wordsContent.split(' ')
    
    #Removes the command from the list of words so it is not added to the blacklist
    wordsSplit.remove("$addWord")
    
    blackList = server_object["blacklist"]
    
    #Iterates through the list of words and appends each one to the blacklist seperately 
    for x in wordsSplit:
        blackList.append(x)
        
        
    #Changes array into string to be output to user
        output = (', '.join(wordsSplit))

    # Sets the object data for blacklist to new blacklist
    server_object["blacklist"] = blackList

    # Stores data
    fm.storeServerData(server_object)

    await ctx.send("You have added '" + output + "' to the black list.")
    #await ctx.send(wordsSplit)



async def removeWord(ctx):
    # get variables
    guildID = str(ctx.guild.id)
    # Gets server data
    server_object = fm.getServerData(guildID)

    # Stores list from server object to blacklist, then appends the words to it
    
    #Gets the message data from the ctx object "words"
    words = ctx.message
    
    #Gets the string of the message from the message data
    wordsContent = words.content
    
    #Splits the words via spaces
    wordsSplit = wordsContent.split(' ')
    
    #Removes the command from the list of words so it is not added to the blacklist
    wordsSplit.remove("$removeWord")
    
    blackList = server_object["blacklist"]
    
    #Iterates through the list of words and appends each one to the blacklist seperately 
    for x in wordsSplit:
        #await ctx.send(x)
        blackList.remove(x)
        
        
    #Changes array into string to be output to user
        output = (', '.join(wordsSplit))

    # Sets the object data for blacklist to new blacklist
    server_object["blacklist"] = blackList

    # Stores data
    fm.storeServerData(server_object)

    await ctx.send("You have removed '" + output + "' from the black list.")
    #await ctx.send(wordsSplit)



async def getBlacklist(ctx):
    # get variables
    guildID = ctx.guild.id
    server_object = fm.getServerData(guildID)
    blacklist = server_object["blacklist"]
    outputString = ""
    counter = 0 
    for x in blacklist:
        #await ctx.send(counter)
        #await ctx.send(len(blacklist))
        if (counter + 1) == len(blacklist):
            outputString += (x + ".")
        else:
            outputString += (x + ", ")
        counter+=1
    await ctx.send("The current blacklist is: " + outputString)
    #await ctx.send(str(blacklist))


#mute functionality takes 2 parameters, 1 as an @to the user, and 2nd a time in minutes for duration
#time is defaulted to 15 mins
async def mute(ctx, user: discord.Member, time: int=15):
    secs = time * 60
    for channel in ctx.guild.channels: #interates over all channels in server
        if isinstance(channel, discord.TextChannel): #if the channel is a text channel
            await channel.set_permissions(user, send_messages=False) #mutes member from writing
        elif isinstance(channel, discord.VoiceChannel): #if the channel is a voice channel
            await channel.set_permissions(user, connect=False) #prevents member from joinging
    await ctx.send(f"{user.mention} has been muted for {time} minutes.") #Bot Message
    await asyncio.sleep(secs) #pauses the running script for the time of the mute
            
    #follow loops execute after the sleep stops and unmutes the member        
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await channel.set_permissions(user, send_messages=None)
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(user, connect=None)
    await ctx.send(f'{user.mention} has been unmuted.')




#unmute functionality, returns privs to a user for writing and joining voice
async def unmute(ctx, user: discord.Member):
    for channel in ctx.guild.channels: #interates over all channels in server
        if isinstance(channel, discord.TextChannel): #if the channel is a text channel
            await channel.set_permissions(user, send_messages=None) #returns privs
        elif isinstance(channel, discord.VoiceChannel): #if the channel is a voice channel
            await channel.set_permissions(user, connect=None )#returns privs
    await ctx.send(f'{user.mention} has been unmuted.') #Bot Message




async def tempBan(ctx, user: discord.Member, days: float=1):
    secs = days * 60 * 60 * 24
    for channel in ctx.guild.channels: #interates over all channels in server
        if isinstance(channel, discord.TextChannel): #if the channel is a text channel
            await channel.set_permissions(user, view_channel=False) #prevents member from seeing the channel
        elif isinstance(channel, discord.VoiceChannel): #if the channel is a voice channel
            await channel.set_permissions(user, view_channel=False) #prevents member from seeing the channel
    await ctx.send(f"{user.mention} has been temporarily banned for {days} days.") #Bot Message
    await asyncio.sleep(secs) #pauses the running script for the days of the ban
            
    #follow loops execute after the sleep stops and unbans the member        
    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            await channel.set_permissions(user, view_channel=None)
        elif isinstance(channel, discord.VoiceChannel):
            await channel.set_permissions(user, view_channel=None)
    await ctx.send(f'{user.mention} has been unbanned.')



#unban functionality, returns privs to a user for viewing channels
async def unTempBan(ctx, user: discord.Member):
    for channel in ctx.guild.channels: #interates over all channels in server
        if isinstance(channel, discord.TextChannel): #if the channel is a text channel
            await channel.set_permissions(user, view_channel=None) #returns privs
        elif isinstance(channel, discord.VoiceChannel): #if the channel is a voice channel
            await channel.set_permissions(user, view_channel=None )#returns privs
    await ctx.send(f'{user.mention} has been unbanned.') #Bot Message
