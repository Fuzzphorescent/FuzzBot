import discord
import config

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is now online!')

client.run(config.BOT_TOKEN)