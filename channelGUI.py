import GUIS
import discord
import modFileManager as fm
import asyncio
import channelbot as cb
from discord.utils import get

Colors = discord.Colour

removingChannel = False

async def channelPanel(rawEventData, bot):
    # Gets discord objects from raw data:
    channel = bot.get_channel(rawEventData.channel_id)
    print("in the loop")
    title = "Channel Module"
    desc = "Would you like to:\n1️⃣ - Create channel.\n2️⃣ - Remove channel (enter channel name).\n3️⃣ - Limit voice channel (enter channel name and number of users)\n4️⃣ - Make category (enter category name)."
    color = Colors.dark_teal()
    
    channelEmbed = discord.Embed(title = title, description = desc, color = color)
    panel = await channel.send(embed = channelEmbed)
    
    reactionList = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '❌']
    
    for emoji in reactionList:
        await panel.add_reaction(emoji)
        
    def check(reaction, user):
        #print(str(reaction))
        return str(reaction)== '1️⃣' or str(reaction) == '2️⃣' or str(reaction) == '3️⃣' or str(reaction) == '4️⃣' or str(reaction) == '❌' and user != panel.author
    
    routineCaller = {
        "1️⃣": createChannelRoutine,
        "2️⃣": removeChannelRoutine,
        "3️⃣": limitVoiceRoutine,
        "4️⃣": makeCategoryRoutine,
        "❌": GUIS.purgeChannel
        }
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
    except asyncio.TimeoutError:
        await GUIS.purgeChannel(rawEventData, bot)
    else:
        if str(reaction) in routineCaller:
            await routineCaller[str(reaction)](rawEventData, bot, panel)
        else:
            channel.send("Not a valid emoji.")
            asyncio.sleep(2)
            await GUIS.purgeChannel(rawEventData, bot)
            await channelPanel(rawEventData, bot)



    ####################
    #                  #
    #  CREATE CHANNEL  #
    #                  #
    ####################



def updatedCreateChannelEmbed(guildID):
    guildData = fm.getServerData(guildID)
    title = "Channel Module"
    desc ="You can react with ✅ to create a text channel or ⭕ to create a voice channel (❌ to exit)."
    desc += "\nAfter reacting, enter the name and category of the channel."
    color = Colors.dark_teal()
    
    channelEmbed = discord.Embed(title = title, description = desc, color = color)
    return channelEmbed

async def createChannelRoutine(rawEventData, bot, panel):
    print("here")
    await panel.clear_reactions()
    guildID = rawEventData.guild_id
    channel = bot.get_channel(rawEventData.channel_id)
    
    channelEmbed = updatedCreateChannelEmbed(guildID)
    
    await panel.edit(embed = channelEmbed)
    
    reactionList = ['✅', '⭕', '❌']
    for emoji in reactionList:
        await panel.add_reaction(emoji)
    
    def check(reaction, user):
        return str(reaction)== '✅' or str(reaction) == '⭕' or str(reaction) == '❌' and user != panel.author
    
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
            
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
        else:
            if str(reaction) == '✅':
                await panelCreateTextChannel(rawEventData, bot)
                await panel.edit(embed = updatedCreateChannelEmbed(guildID))

            elif str(reaction) == '⭕':
                await panelCreateVoiceChannel(rawEventData, bot)
                await panel.edit(embed = updatedCreateChannelEmbed(guildID))

            elif str(reaction) == '❌':
                print("XXXXX")
                await GUIS.purgeChannel(rawEventData, bot)
                await channelPanel(rawEventData, bot)
        
        await panel.clear_reactions()
        for emoji in reactionList:
            await panel.add_reaction(emoji)
            

async def panelCreateTextChannel(rawEventData, bot):
    
    message = await bot.wait_for('message', timeout = 180)            
    messageList = str(message.content).split()
            
    if len(messageList) == 1:
        messageList.append(None)
        
    channelName = messageList[0]
    categoryName = messageList[1]
    
    
    guildID = rawEventData.guild_id
    guild = bot.get_guild(guildID)
    
    for category in guild.categories:
        if str(category) == str(categoryName):
            myCategory = guild.get_channel(category.id)
    
    if not categoryName == None:
        await myCategory.create_text_channel(channelName)
    else:
        await guild.create_text_channel(channelName)
    
async def panelCreateVoiceChannel(rawEventData, bot):
    
    message = await bot.wait_for('message', timeout = 180)            
    messageList = str(message.content).split()
            
    if len(messageList) == 1:
        messageList.append(None)
        
    channelName = messageList[0]
    categoryName = messageList[1]
    
    guildID = rawEventData.guild_id
    guild = bot.get_guild(guildID)
    
    for category in guild.categories:
        if str(category) == str(categoryName):
            myCategory = guild.get_channel(category.id)
    
    if not categoryName == None:
        await myCategory.create_voice_channel(channelName)
    else:
        await guild.create_voice_channel(channelName)



    ####################
    #                  #
    #  REMOVE CHANNEL  #
    #                  #
    ####################



async def removeChannelRoutine(rawEventData, bot, panel):
    
    guildID = rawEventData.guild_id
    guild = bot.get_guild(guildID)
    
    
    while True:
        try:
            message = await bot.wait_for('message', timeout = 180)
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
            await channelPanel(rawEventData, bot)
        else:
            message = message.content
            for channel in guild.channels:
                if channel.name == message:
                    await channel.delete()
        
        await channelPanel(rawEventData, bot)
            
            
            
    #########################
    #                       #
    #  LIMIT VOICE CHANNEL  #
    #                       #
    #########################



async def limitVoiceRoutine(rawEventData, bot, panel):
    
    guildID = rawEventData.guild_id
    guild = bot.get_guild(guildID)
    
    
    while True:
        try:
            message = await bot.wait_for('message', timeout = 180)
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
            await channelPanel(rawEventData, bot)
        else:
            message = message.content
            messageList = message.split()
            for channel in guild.channels:
                if channel.name == messageList[0]:
                    myChannel = channel
            
            await myChannel.edit(user_limit = int(messageList[1]))
        
        await channelPanel(rawEventData, bot)
    
    
    
    #########################
    #                       #
    #    CREATE CATEGORY    #
    #                       #
    #########################



async def makeCategoryRoutine(rawEventData, bot, panel):
    
    guildID = rawEventData.guild_id
    guild = bot.get_guild(guildID)
    
    
    while True:
        try:
            message = await bot.wait_for('message', timeout = 180)
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
            await channelPanel(rawEventData, bot)
        else:
            message = message.content
            
            await guild.create_category(message)
        
        await channelPanel(rawEventData, bot)