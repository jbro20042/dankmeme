import discord
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    print("logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use!")
