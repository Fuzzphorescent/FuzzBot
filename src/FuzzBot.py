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

async def switch_roles_by_reaction(payload, channel_id, message_id, emoji_id, guild_id, \
                             role_to_add, role_to_remove):
    if payload.channel_id == int(channel_id) and \
    payload.message_id == int(message_id) and \
    payload.emoji.id == int(emoji_id):
        guild = client.get_guild(int(guild_id))
        member = guild.get_member(payload.user_id)
        await member.add_roles(get_role_by_name(guild, role_to_add))
        await member.remove_roles(get_role_by_name(guild, role_to_remove))

@client.event
async def on_raw_reaction_add(payload):
    await switch_roles_by_reaction(payload, config.CHANNEL_ID, config.MESSAGE_ID, config.EMOJI_ID, \
                             config.GUILD_ID, config.ROLE_1, config.ROLE_2)

@client.event
async def on_raw_reaction_remove(payload):
    await switch_roles_by_reaction(payload, config.CHANNEL_ID, config.MESSAGE_ID, config.EMOJI_ID, \
                             config.GUILD_ID, config.ROLE_2, config.ROLE_1)

client.run(config.BOT_TOKEN)