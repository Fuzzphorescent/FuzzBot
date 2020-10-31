import discord
import config

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message):
    if message.guild:
        if message.content == 'pingi':
            await message.channel.send('pongi')

def get_role_by_name(guild, role_name):
    for role in guild.roles:
        if role_name == role.name:
            return role

@client.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == int(config.CHANNEL_ID) and \
    payload.message_id == int(config.MESSAGE_ID) and \
    payload.emoji.id == int(config.EMOJI_ID):
        guild = client.get_guild(int(config.GUILD_ID))
        member = guild.get_member(payload.user_id)
        await member.add_roles(get_role_by_name(guild, config.ROLE_1))
        await member.remove_roles(get_role_by_name(guild, config.ROLE_2))

@client.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id == int(config.CHANNEL_ID) and \
    payload.message_id == int(config.MESSAGE_ID) and \
    payload.emoji.id == int(config.EMOJI_ID):
        guild = client.get_guild(int(config.GUILD_ID))
        member = guild.get_member(payload.user_id)
        await member.add_roles(get_role_by_name(guild, config.ROLE_2))
        await member.remove_roles(get_role_by_name(guild, config.ROLE_1))

client.run(config.BOT_TOKEN)