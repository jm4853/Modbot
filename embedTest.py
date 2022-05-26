import discord
import roles
import events
import channelbot as chnls
import discipline as dspln
import modFileManager as fm
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def getBlacklist(ctx):
   await dspln.getBlacklist(ctx)
   
@bot.command()
async def panelAddWord(ctx, message):
    await dspln.panelAddWord(ctx, message)
    
@bot.command()
async def panelRemoveWord(ctx, message):
    await dspln.panelRemoveWord(ctx, message)
    
@bot.command()
async def purgeChannel(ctx):
    await ctx.channel.purge()
    await ctx.send("Home Panel")

@bot.command()
async def panelGetStrikes(ctx, user:discord.Member):
    await dspln.panelGetStrikes(ctx, user)
    
@bot.command()    
async def panelAddStrike(ctx, user: discord.Member, amountOfStrikes):
    await dspln.panelAddStrike(ctx, user, amountOfStrikes)
    
    
@bot.command()
async def panelRemoveStrike(ctx, user: discord.Member, amountOfStrikes):
    await dspln.panelRemoveStrike(ctx, user, amountOfStrikes)

#----------------------|
#UNIVERSAL COLOR OBJECT|
#----------------------|

univColor = discord.Colour

@bot.command()
async def testReaction(ctx):
    color = discord.Colour
    colorRed = color.blue()
    title = "Test"
    url = "https://google.com"
    desc = "test embed"
    color = "xFF0000"
    embed = discord.Embed(title = title, url = url, description = desc, color = colorRed)
    await ctx.send(embed=embed)

#ON EVENT FOR USER REACTION

'''@bot.event
async def on_reaction_add(reaction, user):
     await reaction.message.channel.send(str(reaction))
     print(str(reaction))
'''      
        
@bot.command()
async def blackListPanel(ctx):
    #CREATION OF THE EMBED PANEL AND COLOR OBJECT
    title = "Blacklist Edit Panel"
    desc = "Would you like to: \n View the Blacklist? \n Add a Word to the Blacklist? \n Remove a Word From the Blacklist? \n Get Strikes of a User? \n Add Strikes to a User? \n Remove Strikes from a User? \n \n Press: \n 'V' to View Blacklist \n 'A' to Add to Blacklsit \n 'R' to Remove from Blacklist \n 'W' to Get Strikes \n 'U' to Add Strikes \n 'T' to Remove Strikes"
    color = univColor.blue()
    blackListEmbed = discord.Embed(title = title, description = desc, color = color)
    reactionList = ['🇻', '🇦', '🇷', '🇼', '🇺', '🇹' ,'❌']
    embedMessage = await ctx.send(embed = blackListEmbed)
    messageID = embedMessage.id
    messageList = []
    
    for x in reactionList:
        await embedMessage.add_reaction(x)

    #CHECKS IF USER REACTED WITH VALID REACTIONS
    def check(reaction, user):
        #print(str(reaction))
        return str(reaction)== '🇻' or str(reaction) == '🇦' or str(reaction) == '🇷' or str(reaction) == '🇼' or str(reaction) == '🇺' or str(reaction) == '🇹' or str(reaction) == '❌' and user != embedMessage.author
    
    while True:
        #WAITS FOR USER TO REACT WITH VALID REACTION
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
            
        except asyncio.TimeoutError:
            await purgeChannel(ctx)
            break
        
        else:
            #IF THE USER HAS SELECTED "VIEW" GETBLACKLIST IS RUN
            if str(reaction) == '🇻':
               await getBlacklist(ctx)
            
            #IF THE USER HAS SELECTED "ADD" PANELADDWORD IS RUN
            elif str(reaction) == '🇦':
                await ctx.send("Please Enter the Word(s) You Would Like to Add to the Blacklist.")
                
                message = await bot.wait_for('message')
                
                await panelAddWord(ctx, message)
              
            #IF THE USER HAS SELECTED "REMOVE" PANELREMOVEWORD IS RUN
            elif str(reaction) == '🇷':
                await ctx.send("Please Enter the Word(s) You Would Like to Remove from the Blacklist.")
                
                message = await bot.wait_for('message')
                
                await panelRemoveWord(ctx, message)
                
            #IF THE USER HAS SELECTED "GET STRIKES" PANELGETSTRIKES IS RUN  
            elif str(reaction) == '🇼':
                await ctx.send("Please Enter the Username and Discriminator of the User You Would Like to Get the Strikes of. Ex: test#9123")
                
                message = await bot.wait_for('message')
                messageContent = message.content
                
                await panelGetStrikes(ctx, messageContent)
                
            #IF THE USER HAS SELECTED "ADD STRIKES" PANELADDSTRIKES IS RUN    
            elif str(reaction) == '🇺':
                await ctx.send("Please Enter the Username and Discriminator of the User")
                
                username = await bot.wait_for('message')
                
                await ctx.send("Please Enter the Amount of Strikes You Would Like to Add")
                
                numStrikes = await bot.wait_for('message')
                
                uNameContent = username.content
                nStrikesContent = numStrikes.content
                
                await panelAddStrike(ctx, uNameContent, nStrikesContent)
                
            #IF THE USER HAS SELECTED "REMOVE STRIKES" PANELREMOVESTRIKES IS RUN    
            elif str(reaction) == '🇹':
                await ctx.send("Please Enter the Username and Discriminator of the User")
                
                username = await bot.wait_for('message')
                
                await ctx.send("Please Enter the Amount of Strikes You Would Like to Add")
                
                numStrikes = await bot.wait_for('message')
                
                uNameContent = username.content
                nStrikesContent = numStrikes.content
                
                await panelRemoveStrike(ctx, uNameContent, nStrikesContent)
                
            #IF THE USER HAS SELECTED "CLOSE" PURGECHANNEL IS RUN
            elif str(reaction) == '❌':
                #await ctx.send("I see you")
                await purgeChannel(ctx)
                break
        
botkey = 'Mjk1MzYzODIzOTI4MzQ0NTc2.GSAi2M.w17wpVfQXUTQ1FceDwEchryuUlFh-iKJ7PDFbs'
bot.run(botkey)