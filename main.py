# Modbot.py
#
# This project is still in progress, some features are incomplete and
# may cause other components of the bot to raise errors.
#
# The purpose of this script is to handle events all call other function.
# You can see in the imports each module that we use. The functions
# in each module have the same name as the actual event/command that
# they correspond to. At the bottom of this script, you will find a
# bot.run() call. In order to use this code, you will need to create your
# own bot applications through the Discord developer portal:
# https://discord.com/developers/docs/intro
#
# Once you have created a bot application, you will be able to take its
# token, and paste it into the bot.run() call (at the end of this file).
# To turn on the bot simply run this file (main.py).
#
# Guild and server might be used interchangably throughout this code,
# however its important to note that the correct term is guild.
#
# Documentation for the API wrapper:
# https://discordpy.readthedocs.io/en/stable/
#
# Authors:
# Jake Marchese
# Joshua Kropp
# Michael Trent
# Nathan Kong
# Nemanja Sajatovic 


# Importing the discord API wrapper
import discord
import roles
import events
import GUIS
import channelbot as chnls
import discipline as dspln
import modFileManager as fm
from Help_Command import initHelp
# Another component of the API wrapper that allows us to use the
# bot.command() wrapper
from discord.ext import commands

# Back up measure(s) to ensure bot has necessary tools:
intents = discord.Intents.all()

# Bot must have Intents.reactions enabled for GUI to work reliably
# Creates bot using commands (instead of discord.client())
bot = commands.Bot(command_prefix='$', intents=intents)


# -------------------
# | Event Behaviors |
# -------------------

# Called when bot starts
# Boot up message
@bot.event
async def on_ready():
    await events.on_ready()

# Called when a message is sent in any channel viewable by the bot
# Manual command function (for reference). This is how you would have
# to write commands withouth the commands import
# Includes a $ping command
@bot.event
async def on_message(message):
    # on_message requires the bot object, so its passed in as well
    await events.on_message(message, bot)

# Called whe bot joins a guild
# Bot join's server and posts message
@bot.event
async def on_guild_join(guild):
    await events.on_guild_join(guild)

# Called when a member joins the server
# Currently can add role (prespecified in code) and print message
# Todo: Set the role search function and output channel to a user editable string
@bot.event
async def on_member_join(member):
    await events.on_member_join(member, bot)

# Called when member leaves the server
# Currently sends a message in welcome
# Todo: set outp channel to user editable string
@bot.event
async def on_member_remove(member):
    await events.on_member_remove(member)
    
# Called whenever any reaction occurs
# on the server. Only used to detect reactions
# to the home panel. Must use raw reaction to avoid
# message getting removed from bots interal cache.
# Its important to note that rawEventData is a different
# data type than what is used in almost all other
# bot.events, meaning functions that are called from
# this event must be rewritten to use rawEventData.
# More information can be found in GUIS.py
@bot.event
async def on_raw_reaction_add(rawEventData):
    await events.on_raw_reaction_add(rawEventData, bot)

# Help command
# The help command is actually a default behavior
# and does not need a bot.command() decorator, instead
# it just needs to be initialized
initHelp(bot)


# -----------------------
# | Basic/Test Commands |
# -----------------------
# Test Command
# Returns string passed in
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    print("Run")


# -----------------
# | Role Commands |
# -----------------

# This command adds a role to a specified user
# $add {username} {role}
# Work that needs to be done:
#  - The inputs are very fussy, user can be a
#    string or an @, but role must only be the
#    name of the role, if you use a role @ it
#    wont work.
@bot.command(pass_context=True)
async def add(ctx, user: discord.Member, role):
    await roles.addRole(ctx, user, role)


# Command is basically the same as add, needs
# the same issues worked on
@bot.command(pass_context=True)
async def take(ctx, user: discord.Member, roleName):
    await roles.takeRole(ctx, user, roleName)


# Prints the "Role String" of a specified role
# Has the same issues as take and add, where
# the role passed in must perfectly be the
# name of the role.
@bot.command(pass_context=True)
async def roleInfo(ctx, roleName):
    await roles.getInfo(ctx, roleName)


# Creates a new role, must then use GRP to
# Give Role Permissions
@bot.command(pass_context=True)
async def makeRole(ctx, name):
    await roles.makeRole(ctx, name)


# This takes in a role name, and then a 36
# digit long binary string, each position
# represents a specific permission, below
# gives admin and nothing else:
# $GRP Test 010000000000000000000000000000000000
@bot.command(pass_context=True)
async def GRP(ctx, role):
    await roles.GRP(ctx, role, bot)




# --------------------
# | Channel Commands |
# --------------------

@bot.command(pass_context=True)
async def createMemberCount(ctx, channelPrefix):
    await chnls.createMemberCount(ctx, channelPrefix)

@bot.command(pass_context=True)
async def createChannel(ctx, typeChar, channelName, category: discord.CategoryChannel = None): #Category is default to none
    await chnls.createChannel(ctx, typeChar, channelName, category)

# Creates category with name
@bot.command(pass_context=True)
async def makeCategory(ctx, name):
    await chnls.makeCategory(ctx, name)

@bot.command(pass_context=True)
async def removeTextC(ctx, channel: discord.TextChannel):
    await chnls.removeTextC(ctx, channel)
@bot.command(pass_context=True)
async def removeVoiceC(ctx, channel: discord.VoiceChannel):
    await chnls.removeVoiceC(ctx, channel)


@bot.command(pass_context=True)
async def moveTextC(ctx, channel: discord.TextChannel, category: discord.CategoryChannel):
    await chnls.moveTextC(ctx, channel, category)

@bot.command(pass_context=True)
async def moveVoiceC(ctx, channel: discord.VoiceChannel, category: discord.CategoryChannel):
    await chnls.moveVoiceC(ctx, channel, category)
@bot.command(pass_context=True)
async def limitVoiceChannel(ctx: commands.Context, channel: discord.VoiceChannel, limit: int):
    await chnls.limitVoiceChannel(ctx, channel, limit)
    
@bot.command(pass_context=True)
async def sendHomePanel(ctx):
    await GUIS.sendHomePanel(ctx.channel)


# -----------------------
# | Discipline Commands |
# -----------------------

@bot.command(pass_context=True)
async def getStrikes(ctx, user: discord.Member):
    await dspln.getStrikes(ctx, user)


@bot.command()
async def addStrike(ctx, user: discord.Member):
    await dspln.addStrike(ctx, user)


@bot.command()
async def removeStrike(ctx, user: discord.Member):
    await dspln.removeStrike(ctx, user)

@bot.command()
async def getBlacklist(ctx):
    await dspln.getBlacklist(ctx)

@bot.command()
async def addWord(ctx):
    await dspln.addWord(ctx)


@bot.command()
async def removeWord(ctx):
    await dspln.removeWord(ctx)

@bot.command()
async def mute(ctx, user: discord.Member, time: int=15):
    await dspln.mute(ctx, user, time)

@bot.command()
async def unmute(ctx, user: discord.Member):
    await dspln.unmute(ctx, user)
    
@bot.command()
async def tempBan(ctx, user: discord.Member, days: float=1):
    await dspln.tempBan(ctx, user, days)

@bot.command()
async def unTempBan(ctx, user: discord.Member):
    await dspln.unTempBan(ctx, user)
    
    


bot.run('''Put your bot token here''')