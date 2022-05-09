import discord
import GUIS
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
        




#creating a member count channel
@bot.command(pass_context=True)
async def createMemberCount(ctx, channelPrefix = 'Members:'):
    name = f'{channelPrefix} {ctx.guild.member_count}' #creating a name using the prefix and member count
    overwrite = discord.PermissionOverwrite(connect = False) #setting permission overwrites
    await ctx.guild.create_voice_channel(name, overwrite = overwrite) #creating the channel with the permission



# One command that takes in 3 inputs, first a character that represents
# the type of channel to be created, then the name of the channel to
# create, and then the category to put the channel in
async def createChannel(ctx, typeChar, channelName, category: discord.CategoryChannel = None): #Category is default to none
    if (typeChar == 't'): #if typeChar arg is t, we create text channel
        #Takes in new channelName and category name as text
        await ctx.guild.create_text_channel(channelName, category=category)
        await ctx.send(f'A new text channel: {channelName} has just been created in the category: {category}!')
    elif typeChar == 'v':
        #Takes in new channelName and category name as text
        await ctx.guild.create_voice_channel(channelName, category=category)
        await ctx.send(f'A new voice channel: {channelName} has just been created in the category: {category}!')
    else:
        await ctx.send("Error")



# Creates category with name
async def makeCategory(ctx, name):
    await ctx.guild.create_category(name)
    await ctx.send(f'A category: {name} has just been created!')
    


# Both need to be able to take in a specific category or a more specific channel identifier
@bot.command(pass_context=True)
async def removeTextC(ctx, channel: discord.TextChannel):
    await channel.delete()
    await ctx.send(f'Text channel: {channel} has just been deleted')
@bot.command(pass_context=True)
async def removeVoiceC(ctx, channel: discord.VoiceChannel):
    await channel.delete()
    await ctx.send(f'Voice channel: {channel} has just been deleted')

    
    

# Takes in channel and category, and moves the channel into it
@bot.command(pass_context=True)
async def moveTextC(ctx, channel: discord.TextChannel, category: discord.CategoryChannel):
    await channel.edit(category = category)
    await ctx.send(f'Text channel: {channel} has been moved to {category}!')
    
# Takes in channel and category, and moves the channel into it
@bot.command(pass_context=True)
async def moveVoiceC(ctx, channel: discord.VoiceChannel, category: discord.CategoryChannel):
    await channel.edit(category = category)
    await ctx.send(f'Voice channel: {channel} has been moved to {category}!')



#Takes a voice channel name and an int from 1-99 and changes the userlimit to that int
@bot.command(pass_context=True)
async def limitVoiceChannel(ctx: commands.Context, channel: discord.VoiceChannel, limit: int):
    try:
        await channel.edit(user_limit = limit)
        await ctx.send(f'Voice channel: {channel}, has now been limited to {limit} users')
    except Exception:
        await ctx.send(
            (
                "`{limit}` is either too high or too low please "
                "provide a number between 0 and 99."
            ).format(limit = limit)
        )
        return
    await ctx.tick() 

# creates gui channel titled "Server Editing" that is only visible to those with admin role. returns GUI message id
@bot.command(pass_context=True)
async def createGUIChannel(guild):
    print("In createGUIChannel")
    #name = f'{channelPrefix}'
    
    # set overwrites for create secret channel ("only guild.me can view)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
        }
    
    # create gui editing channel
    channel = await guild.create_text_channel('GUI Editing', overwrites=overwrites)
    
    # members in guild with admin role can see GUI channel
    for member in guild.members:
        for role in member.roles:
            if role.name == "admin":
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages = True
                overwrite.read_messages = True
                await channel.set_permissions(member, overwrite=overwrite)
    
    # send main panel message and get channelID
    homeID = await GUIS.sendHomePanel(channel)
    
    # return messageID
    return homeID