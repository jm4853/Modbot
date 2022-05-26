import discord
from discord.ext import commands
from discord.errors import Forbidden
bot = commands.Bot(command_prefix='$', help_command=None)

desc =(
    """
    Discipline and Strikes:

        $mute {@user} {duration in minutes}, once command is passed the discord member targeted cannot send messages in any text channel and cannot join any voice channel, until the mute expires.
        
        $unmute {@user}, once command is passed the discord member targeted will be given permission to send messages in text channels and allowed to join voice channels.
        
        $tempBan {@user} {duration in days}, once command is passed the discord member targeted cannot view any channels in the server, until the temporary ban expires.
        
        $unTempBan {@user}, once command is passed the discord member targeted will be given permission to view all channels.
        
        $addWord {at least 1 word, or more separated by space}, once the command is passed the bot will add all words in the message separated by space into the black list.
        
        $removeWord {at least 1 word, or more separated by space}, once the command is passed the bot will remove all words in the message separated by space into the black list.
        
        $addStrike {@user} {# of Strikes}, once this command is passed the bot will add the specified number of strikes to the user targeted and update the stored server data for strikes. 
        
        $removeStrike {@user} {# of Strikes}, once this command is passed the bot will remove the specified number of strikes to the user targeted and update the stored server data for strikes. 
        
        $getStrikes {@user}, once this command is passed the bot will send a message to the admin containing the number of strikes that the targeted user has.
        
        $getBlacklist {@user}, once this command is passed the bot will send a message to the admin containing the entire blacklist of words for the server. 
    
    """)

desc1 =(
    """
    Roles & Server Wide Permissions:

        $addRole {@user} {@roleName}, once this command is passed the bot will give the targeted user the specified role.
        
        $takeRole {@user} {@roleName}, once this command is passed the bot will take the specified role from the targeted user.
        
        $roleInfo {@roleName}, once this command is passed the bot will send a message of the permissions the specified role has.
        
        $makeRole {name}, once this command is passed the bot will create a role with the specified name.
        
        $GRP(Give Role Permissions) {@roleName}, once this command is passed the bot will parse through all permissions and have the user respond true or false for server wide permissions. 

    """)

desc2 =(
    '''
    Channels & Categories:

        $createMemberCount, once this command is passed the bot will create a private voice channel that cannot be connected to, but the name will be “Members: “ and a count of all members in the server. 
        
        $createChannel {type (t or v)} {name} {category (optional)}, once this command is passed the bot will make either a text or voice channel with the passed name based on the type parameter, it will then place it into the category specified if given. 
        
        $makeCategory {name}, once this command is passed the bot will create an empty category with the given name.
        
        $removeTextC {#channel}, once this command is passed the bot will search for a text channel with this name and then remove it
        
        $removeVoiceC {#channel}, once this command is passed the bot will search for a voice channel with this name and then remove it
        
        $moveTextC {#channel} {#category}, once this command is passed the bot will search for a text channel with this name and then move it to the specified category.
        
        $moveVoiceC {#channel} {#category}, once this command is passed the bot will search for a voice channel with this name and then move it to the specified category.
        
        $limitVoiceChannel {#channel} {limit}, once this command is passed the bot will search for a voice channel with the name and limit the possible joinees to the limit number.

    ''')
    
desc3 =(
    '''
    Role & User Permissions in Channels:

        $TChannelEditUserPerms {@user} {#channel}, once this command is passed the bot will present all possible user permissions within a text channel and you will respond true or false to toggle permissions for the specific channel.
        
        $TChannelEditRolePerms {@role} {#channel}, once this command is passed the bot will present all possible role permissions within a text channel and you will respond true or false to toggle permissions for the specific channel.
        
        $VChannelEditUserPerms {@user} {#channel}, once this command is passed the bot will present all possible user permissions within a voice channel and you will respond true or false to toggle permissions for the specific channel.
        
        $VChannelEditRolePerms {@role} {#channel}, once this command is passed the bot will present all possivel role permissions within a voice channel and you will respond true or false to toggle permissions for the specific channel.

    ''')

desc4 =(
    '''
    Custom Emojis:

        $createEmoji {Discord Attachment URL}, once this command is passed the bot will create a custom emoji of the Discord attachment that has been passed as the emoji.
        
        $deleteEmoji {emoji}, once this command is passed the bot will delete the custom emoji passed.
    
    ''')

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e1 = discord.Embed(color=discord.Color.blurple(), description = desc)
        e2 = discord.Embed(color=discord.Color.blurple(), description = desc2)
        e3 = discord.Embed(color=discord.Color.blurple(), description = desc1)
        e4 = discord.Embed(color=discord.Color.blurple(), description = desc3)
        e5 = discord.Embed(color=discord.Color.blurple(), description = desc4)
        for page in self.paginator.pages:
            e1.description += page
            e2.description += page
            e3.description += page
            e4.description += page
            e5.description += page
        await destination.send(embed=e1)
        await destination.send(embed=e2)
        await destination.send(embed=e3)
        await destination.send(embed=e4)
        await destination.send(embed=e5)

def initHelp(bot):
    bot.help_command = MyHelpCommand()

