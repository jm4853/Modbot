import discord
from discord.ext import commands

import asyncio

bot = commands.Bot(command_prefix='$')

#Bot boot message
@bot.event
async def on_ready():
    print('Bot is Ready!')
    
guild = discord.Guild 

textPerms = ['view_channel',
             'manage_channels',
             'manage_permissions',
             'manage_webhooks',
             'create_instant_invites',
             'send_messages',
             'embed_links',
             'attach_files',
             'add_reactions',
             'attach_file',
             'external_emojis',
             'mention_everyone',
             'manage_messages',
             'read_message_history',
             'send_tts_messages',
             'use_slash_commands']

voicePerms = ['view_channel',
              'manage_channels',
              'manage_permissions',
              'manage_webhooks',
              'create_instant_invites',
              'connect',
              'speak',
              'stream',
              'use_voice_activation',
              'priority_speaker',
              'mute_members',
              'deafen_members',
              'move_members',]
              
@bot.command(pass_context=True)
async def TChannelEditUserPerms(ctx, user: discord.Member, channel: discord.TextChannel):    
    if isinstance(channel, discord.TextChannel):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ['t', 'f', 'view_channel',
             'manage_channels',
             'manage_permissions',
             'manage_webhooks',
             'create_instant_invites',
             'send_messages',
             'embed_links',
             'attach_files',
             'add_reactions',
             'external_emojis',
             'mention_everyone',
             'manage_messages',
             'read_message_history',
             'send_tts_messages',
             'use_slash_commands']
        
        await ctx.send(f'Type in a permission to edit {textPerms}')
        msg = await bot.wait_for("message", check=check)
        
        #editing if perm is view_channel
        if msg.content.lower() == 'view_channel':
            await ctx.send(f'Set view_channel to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(view_channel = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set view_channel to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(view_channel = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set view_channel to False in {channel} for {user.name}")
                
        #editing if perm is manage_channel
        elif msg.content.lower() == 'manage_channels':
            await ctx.send(f'Set manage_channel to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_channels = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_channels to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_channels = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_channels to False in {channel} for {user.name}")

        #editing if perm is manage_webhooks
        elif msg.content.lower() == 'manage_webhooks':
            await ctx.send(f'Set manage_webhooks to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_webhooks = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_webhooks to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_webhooks = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_webhooks to False in {channel} for {user.name}")

        #editing if perm is create_instant_invites
        elif msg.content.lower() == 'create_instant_invites':
            await ctx.send(f'Set create_instant_invites to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(create_instant_invites = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set create_instant_invites to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(create_instant_invites = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set create_instant_invites to False in {channel} for {user.name}")
                
        #editing if perm is send_messages
        elif msg.content.lower() == 'send_messages':
            await ctx.send(f'Set send_messages to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(send_messages = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set send_messages to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(send_messages = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set send_messages to False in {channel} for {user.name}")
                
        #editing if perm is embed_links
        elif msg.content.lower() == 'embed_links':
            await ctx.send(f'Set embed_links to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(embed_links = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set embed_links to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(embed_links = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set embed_links to False in {channel} for {user.name}")
                
        #editing if perm is attach_files
        elif msg.content.lower() == 'attach_files':
            await ctx.send(f'Set attach_files to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(attach_files = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set attach_files to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(attach_files = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set attach_files to False in {channel} for {user.name}")
                
        #editing if perm is add_reactions
        elif msg.content.lower() == 'add_reactions':
            await ctx.send(f'Set add_reactions to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(add_reactions = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set add_reactions to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(add_reactions = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set add_reactions to False in {channel} for {user.name}")
                
        #editing if perm is external_emojis
        elif msg.content.lower() == 'external_emojis':
            await ctx.send(f'Set external_emojis to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(external_emojis = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set external_emojis to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(external_emojis = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set external_emojis to False in {channel} for {user.name}")
                
        #editing if perm is mention_everyone
        elif msg.content.lower() == 'mention_everyone':
            await ctx.send(f'Set mention_everyone to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(mention_everyone = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set mention_everyone to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(mention_everyone = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set mention_everyone to False in {channel} for {user.name}")
                
        #editing if perm is manage_messages
        elif msg.content.lower() == 'manage_messages':
            await ctx.send(f'Set manage_messages to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_messages = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_messages to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_messages = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_messages to False in {channel} for {user.name}")
                
        #editing if perm is read_message_history
        elif msg.content.lower() == 'read_message_history':
            await ctx.send(f'Set read_message_history to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(read_message_history = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set read_message_history to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(read_message_history = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set read_message_history to False in {channel} for {user.name}")  

        #editing if perm is send_tts_messages
        elif msg.content.lower() == 'send_tts_messages':
            await ctx.send(f'Set send_tts_messages to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(send_tts_messages = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set send_tts_messages to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(send_tts_messages = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set send_tts_messages to False in {channel} for {user.name}")   
 
         #editing if perm is use_slash_commands
        elif msg.content.lower() == 'use_slash_commands':
            await ctx.send(f'Set use_slash_commands to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(use_slash_commands = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set use_slash_commands to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(use_slash_commands = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set use_slash_commands to False in {channel} for {user.name}")   
 
        else:
            await ctx.send('Not a valid permission, type the command and try again')
        
    else:
        await ctx.send('Not a valid text channel, type the command and try again')
                
@bot.command(pass_context=True)
async def VChannelEditUserPerms(ctx, user: discord.Member, channel: discord.VoiceChannel):    
    if isinstance(channel, discord.VoiceChannel):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ['t', 'f', 'view_channel',
              'manage_channels',
              'manage_permissions',
              'manage_webhooks',
              'create_instant_invites',
              'connect',
              'speak',
              'stream',
              'use_voice_activation',
              'priority_speaker',
              'mute_members',
              'deafen_members',
              'move_members',]
        
        await ctx.send(f'Type in a permission to edit {voicePerms}')
        msg = await bot.wait_for("message", check=check)
        
        #editing if perm is view_channel
        if msg.content.lower() == 'view_channel':
            await ctx.send(f'Set view_channel to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(view_channel = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set view_channel to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(view_channel = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set view_channel to False in {channel} for {user.name}")
                
        #editing if perm is manage_channel
        elif msg.content.lower() == 'manage_channels':
            await ctx.send(f'Set manage_channel to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_channels = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_channels to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_channels = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_channels to False in {channel} for {user.name}")

        #editing if perm is manage_webhooks
        elif msg.content.lower() == 'manage_webhooks':
            await ctx.send(f'Set manage_webhooks to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_webhooks = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_webhooks to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_webhooks = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_webhooks to False in {channel} for {user.name}")

        #editing if perm is create_instant_invites
        elif msg.content.lower() == 'create_instant_invites':
            await ctx.send(f'Set create_instant_invites to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(create_instant_invites = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set create_instant_invites to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(create_instant_invites = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set create_instant_invites to False in {channel} for {user.name}")
                
        #editing if perm is connect
        elif msg.content.lower() == 'connect':
            await ctx.send(f'Set connect to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(connect = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set connect to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(connect = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set connect to False in {channel} for {user.name}")
                
        #editing if perm is speak
        elif msg.content.lower() == 'speak':
            await ctx.send(f'Set speak to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(speak = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set speak to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(speak = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set speak to False in {channel} for {user.name}")
                
        #editing if perm is use_voice_activation
        elif msg.content.lower() == 'use_voice_activation':
            await ctx.send(f'Set use_voice_activation to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(use_voice_activation = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set use_voice_activation to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(use_voice_activation = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set use_voice_activation to False in {channel} for {user.name}")
                
        #editing if perm is priority_speaker
        elif msg.content.lower() == 'priority_speaker':
            await ctx.send(f'Set priority_speaker to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(priority_speaker = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set priority_speaker to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(priority_speaker = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set priority_speaker to False in {channel} for {user.name}")
                
        #editing if perm is mute_members
        elif msg.content.lower() == 'mute_members':
            await ctx.send(f'Set mute_members to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(mute_members = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set mute_members to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(mute_members = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set mute_members to False in {channel} for {user.name}")
                
        #editing if perm is deafen_members
        elif msg.content.lower() == 'deafen_members':
            await ctx.send(f'Set deafen_members to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(deafen_members = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set deafen_members to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(deafen_members = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set deafen_members to False in {channel} for {user.name}")
                
        #editing if perm is move_members
        elif msg.content.lower() == 'move_members':
            await ctx.send(f'Set move_members to True or False in {channel} for {user}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(move_members = True)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set move_members to True in {channel} for {user.name}")
                
            else:
                overwrite = discord.PermissionOverwrite(move_members = False)
                await channel.set_permissions(user, overwrite=overwrite)
                await ctx.send(f"Successfully set move_members to False in {channel} for {user.name}")
        
    else:
        await ctx.send('Not a valid text channel, type the command and try again')
        
                
@bot.command(pass_context=True)
async def TChannelEditRolePerms(ctx, role: discord.Role, channel: discord.TextChannel):    
    if isinstance(channel, discord.TextChannel):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ['t', 'f', 'view_channel',
             'manage_channels',
             'manage_permissions',
             'manage_webhooks',
             'create_instant_invites',
             'send_messages',
             'embed_links',
             'attach_files',
             'add_reactions',
             'external_emojis',
             'mention_everyone',
             'manage_messages',
             'read_message_history',
             'send_tts_messages',
             'use_slash_commands']
        
        await ctx.send(f'Type in a permission to edit {textPerms}')
        msg = await bot.wait_for("message", check=check)
        
        #editing if perm is view_channel
        if msg.content.lower() == 'view_channel':
            await ctx.send(f'Set view_channel to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(view_channel = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set view_channel to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(view_channel = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set view_channel to False in {channel} for {role}")
                
        #editing if perm is manage_channel
        elif msg.content.lower() == 'manage_channels':
            await ctx.send(f'Set manage_channel to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_channels = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_channels to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_channels = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_channels to False in {channel} for {role}")

        #editing if perm is manage_webhooks
        elif msg.content.lower() == 'manage_webhooks':
            await ctx.send(f'Set manage_webhooks to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_webhooks = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_webhooks to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_webhooks = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_webhooks to False in {channel} for {role}")

        #editing if perm is create_instant_invites
        elif msg.content.lower() == 'create_instant_invites':
            await ctx.send(f'Set create_instant_invites to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(create_instant_invites = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set create_instant_invites to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(create_instant_invites = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set create_instant_invites to False in {channel} for {role}")
                
        #editing if perm is send_messages
        elif msg.content.lower() == 'send_messages':
            await ctx.send(f'Set send_messages to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(send_messages = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set send_messages to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(send_messages = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set send_messages to False in {channel} for {role}")
                
        #editing if perm is embed_links
        elif msg.content.lower() == 'embed_links':
            await ctx.send(f'Set embed_links to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(embed_links = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set embed_links to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(embed_links = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set embed_links to False in {channel} for {role}")
                
        #editing if perm is attach_files
        elif msg.content.lower() == 'attach_files':
            await ctx.send(f'Set attach_files to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(attach_files = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set attach_files to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(attach_files = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set attach_files to False in {channel} for {role}")
                
        #editing if perm is add_reactions
        elif msg.content.lower() == 'add_reactions':
            await ctx.send(f'Set add_reactions to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(add_reactions = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set add_reactions to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(add_reactions = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set add_reactions to False in {channel} for {role}")
                
        #editing if perm is external_emojis
        elif msg.content.lower() == 'external_emojis':
            await ctx.send(f'Set external_emojis to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(external_emojis = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set external_emojis to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(external_emojis = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set external_emojis to False in {channel} for {role}")
                
        #editing if perm is mention_everyone
        elif msg.content.lower() == 'mention_everyone':
            await ctx.send(f'Set mention_everyone to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(mention_everyone = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set mention_everyone to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(mention_everyone = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set mention_everyone to False in {channel} for {role}")
                
        #editing if perm is manage_messages
        elif msg.content.lower() == 'manage_messages':
            await ctx.send(f'Set manage_messages to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_messages = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_messages to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_messages = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_messages to False in {channel} for {role}")
                
        #editing if perm is read_message_history
        elif msg.content.lower() == 'read_message_history':
            await ctx.send(f'Set read_message_history to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(read_message_history = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set read_message_history to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(read_message_history = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set read_message_history to False in {channel} for {role}")  

        #editing if perm is send_tts_messages
        elif msg.content.lower() == 'send_tts_messages':
            await ctx.send(f'Set send_tts_messages to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(send_tts_messages = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set send_tts_messages to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(send_tts_messages = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set send_tts_messages to False in {channel} for {role}")   
 
         #editing if perm is use_slash_commands
        elif msg.content.lower() == 'use_slash_commands':
            await ctx.send(f'Set use_slash_commands to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(use_slash_commands = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set use_slash_commands to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(use_slash_commands = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set use_slash_commands to False in {channel} for {role}")   
 
        else:
            await ctx.send('Not a valid permission, type the command and try again')
        
    else:
        await ctx.send('Not a valid text channel, type the command and try again')

@bot.command(pass_context=True)
async def VChannelEditRolePerms(ctx, role: discord.Role, channel: discord.VoiceChannel):    
    if isinstance(channel, discord.VoiceChannel):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ['t', 'f', 'view_channel',
              'manage_channels',
              'manage_permissions',
              'manage_webhooks',
              'create_instant_invites',
              'connect',
              'speak',
              'stream',
              'use_voice_activation',
              'priority_speaker',
              'mute_members',
              'deafen_members',
              'move_members',]
        
        await ctx.send(f'Type in a permission to edit {voicePerms}')
        msg = await bot.wait_for("message", check=check)
        
        #editing if perm is view_channel
        if msg.content.lower() == 'view_channel':
            await ctx.send(f'Set view_channel to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(view_channel = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set view_channel to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(view_channel = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set view_channel to False in {channel} for {role}")
                
        #editing if perm is manage_channel
        elif msg.content.lower() == 'manage_channels':
            await ctx.send(f'Set manage_channel to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_channels = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_channels to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_channels = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_channels to False in {channel} for {role}")

        #editing if perm is manage_webhooks
        elif msg.content.lower() == 'manage_webhooks':
            await ctx.send(f'Set manage_webhooks to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(manage_webhooks = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_webhooks to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(manage_webhooks = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set manage_webhooks to False in {channel} for {role}")

        #editing if perm is create_instant_invites
        elif msg.content.lower() == 'create_instant_invites':
            await ctx.send(f'Set create_instant_invites to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(create_instant_invites = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set create_instant_invites to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(create_instant_invites = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set create_instant_invites to False in {channel} for {role}")
                
        #editing if perm is connect
        elif msg.content.lower() == 'connect':
            await ctx.send(f'Set connect to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(connect = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set connect to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(connect = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set connect to False in {channel} for {role}")
                
        #editing if perm is speak
        elif msg.content.lower() == 'speak':
            await ctx.send(f'Set speak to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(speak = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set speak to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(speak = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set speak to False in {channel} for {role}")
                
        #editing if perm is use_voice_activation
        elif msg.content.lower() == 'use_voice_activation':
            await ctx.send(f'Set use_voice_activation to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(use_voice_activation = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set use_voice_activation to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(use_voice_activation = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set use_voice_activation to False in {channel} for {role}")
                
        #editing if perm is priority_speaker
        elif msg.content.lower() == 'priority_speaker':
            await ctx.send(f'Set priority_speaker to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(priority_speaker = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set priority_speaker to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(priority_speaker = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set priority_speaker to False in {channel} for {role}")
                
        #editing if perm is mute_members
        elif msg.content.lower() == 'mute_members':
            await ctx.send(f'Set mute_members to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(mute_members = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set mute_members to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(mute_members = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set mute_members to False in {channel} for {role}")
                
        #editing if perm is deafen_members
        elif msg.content.lower() == 'deafen_members':
            await ctx.send(f'Set deafen_members to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(deafen_members = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set deafen_members to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(deafen_members = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set deafen_members to False in {channel} for {role}")
                
        #editing if perm is move_members
        elif msg.content.lower() == 'move_members':
            await ctx.send(f'Set move_members to True or False in {channel} for {role}: T or F')
            msg = await bot.wait_for("message", check=check)
            
            if msg.content.lower() == "t":
                overwrite = discord.PermissionOverwrite(move_members = True)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set move_members to True in {channel} for {role}")
                
            else:
                overwrite = discord.PermissionOverwrite(move_members = False)
                await channel.set_permissions(role, overwrite=overwrite)
                await ctx.send(f"Successfully set move_members to False in {channel} for {role}")
        
    else:
        await ctx.send('Not a valid text channel, type the command and try again')

#Run token
print("Yo")
bot.run('Mjk1MzYzODIzOTI4MzQ0NTc2.WNcU_w.OuFwSoQlSZuTCezHieWrP_xuDiY ')  

