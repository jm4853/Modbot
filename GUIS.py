import discord
import modFileManager as fm
import asyncio
import panelDiscipline
import panelRoles
import channelGUI

Colors = discord.Colour

# Raw event data contains 7 attributes:
#  - channel_id     #  - member
#  - emoji          #  - message_id
#  - event_type     #  - user_id
#  - guild_id

# Helpful tips:
# - by passing around the bot object, you have
#   access to all the channels that the bot can see
#   which will have to replace ctx in most commands
# - Channel Object: bot.get_channel(rawEventData.channel_id)
# - Guild Object: bot.get_guild(rawEventData.guild_id)
# - rawEventData.member is a member object
# - rawEventData.emoji is a PartialEmoji object



async def purgeChannel(rawEventData, bot, *args):
    channel = bot.get_channel(rawEventData.channel_id)
    await channel.purge()
    homePanelID = await sendHomePanel(channel)

def storeHomePanel(guildID, panelID):
    guildData = fm.getServerData(guildID)
    guildData["homePanel"] = panelID
    fm.storeServerData(guildData)


async def samplePanel(rawEventData, bot):
    # Getting disord objects from rawEventData
    print(rawEventData.channel_id)
    channel = bot.get_channel(rawEventData.channel_id)
    guildID = rawEventData.guild_id
    channelID = rawEventData.channel_id
    
    
    title = "Sample Panel"
    desc = "Here are some actions:\nš» - print one thing\nš¦ - print another\nš· - another "
    color = Colors.purple()
    
    sampleEmbed = discord.Embed(title = title, description = desc, color = color)
    samplePanel = await channel.send(embed = sampleEmbed)
    reactionList = ['š»', 'š¦', 'š·', 'ā']
    
    for reaction in reactionList:
        await samplePanel.add_reaction(reaction)
        
    def check(reaction, user):
        #print(str(reaction))
        return str(reaction)== 'š»' or str(reaction) == 'š¦' or str(reaction) == 'š·' or str(reaction) == 'ā' and user != samplePanel.author
    
    
    while True:
        #WAITS FOR USER TO REACT WITH VALID REACTION
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 120.0, check=check)
            
        except asyncio.TimeoutError:
            await purgeChannel(guildID, channelID, bot)
            break
        
        else:
            #IF THE USER HAS SELECTED "VIEW" GETBLACKLIST IS RUN
            if str(reaction) == 'š»':
               await channel.send("message1")
            
            #IF THE USER HAS SELECTED "ADD" PANELADDWORD IS RUN
            elif str(reaction) == 'š¦':
                await channel.send("message2")
              
            #IF THE USER HAS SELECTED "REMOVE" PANELREMOVEWORD IS RUN
            elif str(reaction) == 'š·':
                await channel.send("message3")
             
            #IF THE USER HAS SELECTED "CLOSE" PURGECHANNEL IS RUN
            elif str(reaction) == 'ā':
                #await ctx.send("I see you")
                await purgeChannel(rawEventData, bot)
                break
    
    
    







# This dictionary is used for correlating panels with emojis.
# To add a pannel simply add a new entry to the dictionary
# with the unicode value of the emoji as the key. You will
# have to edit the message sent in the home panel

callGUI = {
    "šļø": samplePanel,
    "ā¼": panelDiscipline.disciplinePanel,
    "š": panelRoles.rolePanel,
    "š²": channelGUI.channelPanel
    }
# Use this function to get the list of panel emojis
def panelListEmojis():
        return list(callGUI.keys())

async def handleGUIreactions(rawEventData, bot):
    print(f"reacted: {rawEventData.emoji}")
    guildID = rawEventData.guild_id
    messageID = rawEventData.message_id
    emoji = rawEventData.emoji
    guildData = fm.getServerData(guildID)
    homePanelID = guildData["homePanel"]
    if messageID == homePanelID:
        await callGUI[emoji.name](rawEventData, bot)
    

async def sendHomePanel(channel):    
    title = "Home Panel"
    desc = "Here you can access the other moderation panels:\nā¼ - for blacklist and strike management\nš - for role management\nš² - for channel management"
    color = Colors.dark_gold()
    
    homeEmbed = discord.Embed(title = title, description = desc, color = color)
    homePanel = await channel.send(embed = homeEmbed)
    
    storeHomePanel(homePanel.guild.id, homePanel.id)
    
    for emoji in panelListEmojis():
        await homePanel.add_reaction(emoji)
    
    return homePanel.id