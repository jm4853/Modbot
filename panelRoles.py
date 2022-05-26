import GUIS
import discord
import modFileManager as fm
import asyncio
import discipline as dspln
import re
from time import sleep

Colors = discord.Colour
perm_list = [
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


    
async def rolePanel(rawEventData, bot):
    channel = bot.get_channel(rawEventData.channel_id)
    title = "Roles Module"
    desc = "Would you like to \n1️⃣ - Manage a Users Roles?\n2️⃣ - Manage Server Roles?"
    color = Colors.dark_teal()
    roleEmbed = discord.Embed(title = title, description = desc, color = color)
    
    panel = await channel.send(embed = roleEmbed)
    
    reactionList = ['1️⃣', '2️⃣', '❌']
    
    for emoji in reactionList:
        await panel.add_reaction(emoji)
    def check(reaction, user):
        #print(str(reaction))
        return str(reaction)== '1️⃣' or str(reaction) == '2️⃣' or str(reaction) == '❌' and user != panel.author
    
    switch = {
        "1️⃣": userRoleRoutine,
        "2️⃣": rolesRoutine,
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
            
def updatedUserRolePanel(rawEventData):
    title = "User Roles Module"
    desc = "Would you like to: \n ✅ Add Roles to a User? \n ⭕ Remove Roles from a User? \n ❌ Exit Panel."
    color = Colors.dark_teal()
    updatedUserRolePanel = discord.Embed(title = title, description = desc, color = color)
    return updatedUserRolePanel
    

async def updatedUserRolesEmbed(rawEventData, bot):
    title = "Roles Module"
    desc = "Please Enter: \n The Username and Discriminator of the User You Would Like to Edit the Roles of (e.g: john#0001) \n The Roles You Would like to Give Them/Take From, Separated by Spaces (e.g 1 5 7) \n \n The Current Roles in the Server are:"
    color = Colors.dark_teal()
    counter = 1
    roleList = await panelGetRoles(rawEventData, bot)
    
    for role in roleList:
        desc += f"\n {counter}: {role}"
        counter += 1
    
    userRoleEmbed = discord.Embed(title = title, description = desc, color = color)
        
    return userRoleEmbed

async def userRoleRoutine(rawEventData, bot, panel):
    await panel.clear_reactions()
    guildID = rawEventData.guild_id
    channel = bot.get_channel(rawEventData.channel_id)
    
    roleEmbed = updatedUserRolePanel(guildID)
    
    await panel.edit(embed = roleEmbed)
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
                await panel.edit(embed = await updatedUserRolesEmbed(rawEventData, bot))
                
                message = await bot.wait_for('message', timeout = 60.0)
                messageContent = message.content
                
                await panelAssignRoles(rawEventData, bot, messageContent)

            elif str(reaction) == '⭕':
                await panel.edit(embed = await updatedUserRolesEmbed(rawEventData, bot))
                
                message = await bot.wait_for('message', timeout = 60.0)
                messageContent = message.content
                
                await panelRemoveRoles(rawEventData, bot, messageContent)
                
            elif str(reaction) == '❌':
                await GUIS.purgeChannel(rawEventData, bot)
                await rolePanel(rawEventData, bot)
        
        await panel.clear_reactions()
        for emoji in reactionList:
            await panel.add_reaction(emoji)


async def panelGetRoles(rawEventData, bot):
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    roleList = []
    
    for role in guild.roles:
        roleList.append(role.name)
        
    return roleList
    
async def panelGetRoleIds(rawEventData, bot):
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    roleList = []
    
    for role in guild.roles:
        roleList.append(role)
        
    return roleList

async def panelManageUserRole(rawEventData, bot):
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    
    await channel.send(panelGetRoles)
    
async def panelAssignRoles(rawEventData, bot, message):
    #RawEventData --> Channel, Guild, and GuildID
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id

    #Getting Roles from Server, splitting user message to get username, discriminator, and the number roles the user picked
    roleList = await panelGetRoleIds(rawEventData, bot)
    #print(message)
    messageSplit = re.split("#| ",message)
    uName = messageSplit[0]
    discriminator = messageSplit[1]
    
    #Deletes the username and discriminator from the list after they've been assigned to variables to iterate through the list easier
    messageSplit.pop(0)
    messageSplit.pop(0)
    
    #Declaration of arrays to be assigned later
    desiredRoles = []
    rolesToBeGiven = []
    user = ""
    #print(messageSplit)
    #print(roleList)
    
    #Assigns the numbers of the roles that the user picked to a list so that it can be used as an index for the role assignment
    for x in messageSplit:
        desiredRoles.append(x)
            
    #Checks if the given user is in the server, if found the member Object of the given user is assigned to the variable - user    
    async for member in guild.fetch_members():
            if str(member.name) == uName and str(member.discriminator) == discriminator:
                user = member
                print(user.name)
    
    #First part of print statement
    printMessage = f"Successfully added the following roles to {user}: "
    
    #Assigns the desired roles to the user and appends their name to the print statement
    for index in desiredRoles:
        role = roleList[(int(index)-1)]
        await user.add_roles(role)
        printMessage += f"{role.name} "
        
    await channel.send(printMessage)
    
    
async def panelRemoveRoles(rawEventData, bot, message):
    #RawEventData --> Channel, Guild, and GuildID
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    
    #Getting Roles from Server, splitting user message to get username, discriminator, and the number roles the user picked
    roleList = await panelGetRoleIds(rawEventData, bot)
    #print(message)
    messageSplit = re.split("#| ",message)
    uName = messageSplit[0]
    discriminator = messageSplit[1]
    
    #Deletes the username and discriminator from the list after they've been assigned to variables to iterate through the list easier
    messageSplit.pop(0)
    messageSplit.pop(0)
    
    #Declaration of arrays to be assigned later
    desiredRoles = []
    rolesToBeTaken = []
    user = ""
    #print(messageSplit)
    #print(roleList)
    
    #Assigns the numbers of the roles that the user picked to a list so that it can be used as an index for the role removal
    for x in messageSplit:
        desiredRoles.append(x)
        
    print(desiredRoles)
            
    #Checks if the given user is in the server, if found the member Object of the given user is assigned to the variable - user
    async for member in guild.fetch_members():
            if str(member.name) == uName and str(member.discriminator) == discriminator:
                user = member
                print(user.name)
    
    #First part of print statement
    printMessage = f"Successfully removed the following roles from {user}: "
    
    #Removes the desired roles to the user and appends their name to the print statement
    for index in desiredRoles:
        role = roleList[(int(index)-1)]
        await user.remove_roles(role)
        printMessage += f"{role.name} "
        
    await channel.send(printMessage)
    















def updateRolePanel(guild):    
    title = "Roles Module"
    desc = "Here are the current roles:\n"
    for role in guild.roles:
        desc += f"{role.name}\n"
    desc += "\nWould you like to: \n ✅ Create a new role. \n ⭕ Delete a current role. \n 🔨 Edit a roles permissions. \n ❌ Exit Panel."
    color = Colors.dark_teal()
    return discord.Embed(title = title, description = desc, color = color)

def createAddRoleEmbed(guild):
    title = "Create a role"
    desc = "Here are the current roles:\n"
    for role in guild.roles:
        desc += f"{role.name}\n"
    desc += "\nEnter the name of the role you would like to create."
    color = Colors.dark_teal()
    return discord.Embed(title = title, description = desc, color = color)

def createDeleteRoleEmbed(guild):
    title = "Delete a role"
    desc = "Here are the current roles:\n"
    for role in guild.roles:
        desc += f"{role.name}\n"
    desc += "\nEnter the name of the role you would like to remove."
    color = Colors.dark_teal()
    return discord.Embed(title = title, description = desc, color = color)

def createEditRoleEmbed_ROLES(guild):
    title = "Edit a role"
    desc = "Here are the current roles:\n"
    for role in guild.roles:
        desc += f"{role.name}\n"
    desc += "\nEnter the name of the role you would like to edit."
    color = Colors.dark_teal()
    return discord.Embed(title = title, description = desc, color = color)

def createEditRoleEmbed_PERMS(guild, roleName):
    try:
        role = discord.utils.get(guild.roles, name=roleName)
    except Exception as e:
        print(e)
        return (-1, 0)
    title = "Edit a role"
    desc = f"Here are permissions for {role.name}:\n"
    for perm in perm_list:
        if eval(f"role.permissions.{perm}"):
            desc += f"✅ {perm}\n"
        else:
            desc += f"⭕ {perm}\n"
    desc += "\nEnter the name of the permission you would like to toggle. Enter 'close' to exit."
    color = Colors.dark_teal()
    return (1, discord.Embed(title = title, description = desc, color = color))


async def panelAddRole(guild, bot, name):   
    try:
        # Passes in the role name
        await guild.create_role(name=name)
        return 0
    except Exception as e:
        print(e)
        return - 1

async def panelDeleteRole(guild, bot, name):
    try:
        role = discord.utils.get(guild.roles, name=name)
        await role.delete()
        return 1
    except Exception as e:
        print(e)
        return -1

async def panelEditRole(guild, bot, roleName, perm):
    try:
        role = discord.utils.get(guild.roles, name=roleName)
    except Exception as e:
        print(e)
        return -1
    if not perm in perm_list:
        return -1
    
    permObj = role.permissions
    exec(f"permObj.update({perm} = (not role.permissions.{perm}))")
    await role.edit(permissions = permObj)




async def rolesRoutine(rawEventData, bot, panel):
    await panel.clear_reactions()
    guildID = rawEventData.guild_id
    guild = bot.get_guild(guildID)
    channel = bot.get_channel(rawEventData.channel_id)
    
    roleEmbed = updateRolePanel(guild)
    
    await panel.edit(embed = roleEmbed)
    reactionList = ['✅', '⭕', '🔨', '❌']
    for emoji in reactionList:
        await panel.add_reaction(emoji)
    
    def check(reaction, user):
        #print(str(reaction))
        return str(reaction)== '✅' or str(reaction) == '⭕' or str(reaction) == '🔨' or str(reaction) == '❌' and user != panel.author
    
    def checkExit(reaction, user):
        #print(str(reaction))
        return str(reaction) == '❌' and user != panel.author
    
    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 60.0, check=check)
        except asyncio.TimeoutError:
            await GUIS.purgeChannel(rawEventData, bot)
        else:
            if str(reaction) == '✅':
                await panel.edit(embed = createAddRoleEmbed(guild))
                
                message = await bot.wait_for('message', timeout = 60.0)
                messageContent = message.content
                
                if await panelAddRole(guild, bot, messageContent) == -1:
                    await channel.send("Invalid role name")

            elif str(reaction) == '⭕':
                await panel.edit(embed = createDeleteRoleEmbed(guild))
                
                message = await bot.wait_for('message', timeout = 60.0)
                messageContent = message.content
                
                if await panelDeleteRole(guild, bot, messageContent) == -1:
                    await channel.send("Invalid role name")
            
            elif str(reaction) == '🔨':
                await panel.edit(embed = createEditRoleEmbed_ROLES(guild))
                        
                message = await bot.wait_for('message', timeout = 60.0)
                roleName = message.content
                perms_embed = createEditRoleEmbed_PERMS(guild, roleName)
                if perms_embed[0] == -1:
                    await channel.send("Invalid role name")
                else:
                    await panel.edit(embed = perms_embed[1])
                    await panel.clear_reactions()
                    while True:
                        try:
                            # done, pending = await asyncio.wait([bot.loop.create_task(bot.wait_for('message')), bot.loop.create_task(bot.wait_for('reaction_add'))], return_when=asyncio.FIRST_COMPLETED)
                            message = await bot.wait_for('message', timeout = 60.0)

                        except asyncio.TimeoutError:
                            await GUIS.purgeChannel(rawEventData, bot)
                        else:
                            permName = message.content
                            if permName.lower() == "close":
                                await GUIS.purgeChannel(rawEventData, bot)
                                await rolePanel(rawEventData, bot)
                                return
                                
                            if await panelEditRole(guild, bot, roleName, permName) == -1:
                                await channel.send("Invalid permission name")
                            else:
                                perms_embed = createEditRoleEmbed_PERMS(guild, roleName)
                                await panel.edit(embed = perms_embed[1])
                                sleep(1)
                                await message.delete()
                    
                
            elif str(reaction) == '❌':
                await GUIS.purgeChannel(rawEventData, bot)
                await rolePanel(rawEventData, bot)
                return
        
        await panel.clear_reactions()
        await panel.edit(embed = updateRolePanel(guild))
        for emoji in reactionList:
            await panel.add_reaction(emoji)
















#-----------------------------------------------------------------------------------------------------------
#| Currently Scrapped, Will Leave For Potential Future Implementation --> Allows the ability for the user to |
#| have multiple pages of roles so that only 10 are displayed at once, entirely aesthetic and not necessary, |
#| if you would like to take a shot at it, go for it.                                                        | 
#-----------------------------------------------------------------------------------------------------------
'''   
async def pageChange(rawEventData, bot, reaction):
    channel = bot.get_channel(rawEventData.channel_id)
    guild = bot.get_guild(rawEventData.guild_id)
    guildID = rawEventData.guild_id
    
    reactionString = str(reaction)
    roleList = await panelGetRoles(rawEventData, bot)
    
    leftBound = 0
    rightBound = 0
    counter = 0
    
    desc = "Please Enter: \n The Username and Discriminator of the User You Would Like to Edit the Roles of (e.g: john#0001) \n The Roles You Would like to Give Them, Separated by Spaces (e.g 1 5 7) \n\n Use the Arrows at the Bottom to Change Pages to See More Roles\n \n The current roles in the server are: "
    
    for role in roleList:
        if counter <= 10 and counter < (len(roleList)-1):
            if (len(roleList)) < 10:
                rightBound = (len(roleList)-1)
            elif len(roleList) >= 10:
                rightBound = 10
            
        if counter < rightBound:
            desc += f"\n{counter +1}: {role} "
            counter += 1
            
        if counter < 
                
        
            
    return(str(desc))
'''           
    
    
    
    
    
    
    
    

