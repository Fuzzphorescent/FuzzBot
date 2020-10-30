import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

@client.event
async def on_message(message):
    if message.guild:
        if message.content == 'pingi':
            await message.channel.send('pongi')

client.run(config.BOT_TOKEN)