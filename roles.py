import discord
from discord.ext import commands

list_perms = [
    "add_reactions",
    "administrator",
    "attach_files",
    "ban_members",
    "change_nickname",
    "connect",
    "create_instant_invite",
    "deafen_members",
    "embed_links",
    "external_emojis",
    "kick_members",
    "manage_channels",
    "manage_emojis",
    "manage_guild",
    "manage_messages",
    "manage_nicknames",
    "manage_permissions",
    "manage_roles",
    "manage_webhooks",
    "mention_everyone",
    "move_members",
    "mute_members",
    "priority_speaker",
    "read_message_history",
    "read_messages",
    "request_to_speak",
    "send_messages",
    "send_tts_messages",
    "speak",
    "stream",
    "use_external_emojis",
    "use_slash_commands",
    "use_voice_activation",
    "view_audit_log",
    "view_channel",
    "view_guild_insights",
    ]



async def addRole(ctx, user: discord.Member, roleName):
    try:
        # Finds the role based on the string (arg2) passed in
        # then adds the role
        role = discord.utils.get(ctx.guild.roles, name=roleName)
        await user.add_roles(role)
    # Error occurs when its unable to find the role and tries
    # to call add_roles() on nothing
    except:
        await ctx.send("Invalid role")
        return
    await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")


# Command is basically the same as add, needs
# the same issues worked on
async def takeRole(ctx, user: discord.Member, roleName):
    try:
        role = discord.utils.get(ctx.guild.roles, name=roleName)
        await user.remove_roles(role)
    except:
        await ctx.send("Invalid role")
        return
    await ctx.send(f"hey {ctx.author.name}, {role.name} has been removed from {user.name}")


# Prints the "Role String" of a specified role
# Has the same issues as take and add, where
# the role passed in must perfectly be the
# name of the role.
async def roleInfo(ctx, arg1):
    try:
        role = str(discord.utils.get(ctx.guild.roles, name=arg1).permissions)
        await ctx.send(role)
    except:
        await ctx.send("Invalid role")
        return


# Creates a new role, must then use GRP to
# Give Role Permissions
async def makeRole(ctx, name):
    guild = ctx.guild
    try:
        # Passes in the role name
        await guild.create_role(name=name)
        await ctx.send(f'Role `{name}` has been created')
    except Exception as e:
        print(e)
        await ctx.send("Invalid role")
        return

# This takes in a role name and iterates through all possible permissions and gets user input to
# set a permission value to either true or false.
#Params: @role takes in a @ for a role and stores as an instance of the role class.
async def GRP(ctx, role: discord.Role, bot):
    #creates new permission object that is updated in the function
    perms = discord.Permissions()
    
    #method to verify user input from Discor
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ['t', 'f']

    # Starts a for loop that iterates through each perm
    for permission in list_perms:
        await ctx.send(f'Type T or F to set {permission} to True or False') #Prompts user for input
        msg = await bot.wait_for("message", check=check) #checks the message input from user for validity
        
        if msg.content.lower() == "t": #case for true
            #exec method executes a string as code
            exec(f'perms.update({permission} = True)') #builds a formatted string to update a permission value to true
            await ctx.send(f"Successfully set {permission} to True for {role}") #confirmation to user.
                
        else: #case for false
            #exec method executes a string as code
            exec(f'perms.update({permission} = False)') #builds a formatted string to update a permission value to false
            await ctx.send(f"Successfully set {permission} to False for {role}") #confirmation to user.
            
    # Sets the roles permissions to the permission object
    await role.edit(permissions = perms)
    await ctx.send(f'Permissions have been updated for {role}') #user confirmation that function call is over
