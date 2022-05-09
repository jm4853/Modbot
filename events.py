import discord
import discipline as dspln
from asyncio import sleep
import modFileManager as fm
import channelbot as cb
import GUIS

# Boot up message
async def on_ready():
    print('Bot is ready!')

# Manual command function (for reference)
# Includes $ping command
async def on_message(message, bot):
    # Makes sure messages arent sent by bot
    if message.author != bot.user:
        # If the word is not on the black list it processes commands
        if not await dspln.enforceBlackList(message):
            await bot.process_commands(message)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$ping'):
        await message.channel.send(f'Pong! {round(bot.latency * 1000)}ms')



# Bot join's server and posts message
async def on_guild_join(guild):
    messageID = await cb.createGUIChannel(guild)
    print("IN onguildjoin")
    fm.addServer(guild.id, messageID)
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("I hath arrived.")
        break



# Called when a member joins the server
# Currently can add role (prespecified in code) and print message
# Todo: Set the role search function and output channel to a user editable string
async def on_member_join(member, bot):
    # Sets role to the string passed in ("onJoin")
    ctx = bot.get_context(member)
    # Adds role

    channel = discord.utils.get(member.guild.text_channels, name="welcome")  # define channel name
    await channel.send(f"{member} has joined!")  # sends message in channel

    for channel in member.guild.channels: #parsing channel lists for the member count channel
        await sleep(60*10)
        true_member_count = len([m for m in ctx.guild.members if not m.bot])
        if channel.name.startswith('Member'): #finding member channel
            await channel.edit(name=f'Members: {true_member_count}') #updating the name and count
            break
    


# Called when member leaves the server
# Currently sends a message in welcome
# Todo: set outp channel to user editable string
async def on_member_remove(member):

    for channel in member.guild.channels: #parsing channel lists for the member count channel
        await sleep(60*10)
        true_member_count = len([m for m in ctx.guild.members if not m.bot])
        if channel.name.startswith('Member'): #finding member channel
            await channel.edit(name=f'Members: {true_member_count}') #updating the name and count
            break

    channel = discord.utils.get(member.guild.text_channels, name="welcome")  # define channel name
    await channel.send(f"{member} has left!")  # sends message in channel


# Called whenever any reaction occurs
# on the server. Only used to detect reactions
# to the home panel. Must use raw reaction to avoid
# message getting removed from bots interal cache
async def on_raw_reaction_add(rawEventData, bot):
    if not rawEventData.member.bot:
        await GUIS.handleGUIreactions(rawEventData, bot)
    
    