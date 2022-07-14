import discord #pip install discord
import os
from python_aternos import Client # pip install python-aternos
client = discord.Client()

# Private information may be censored when posting code 
TOKEN = '' # Private
BOT_CHANNEL_NAME = '🍦vanilla-pixelmon-server🍦'
USERNAME = '' #Private
PASSWORD = '' # Private

@client.event
async def on_ready():
    print('Bot [{0.user}] is online!'.format(client))

@client.event
async def on_message(message):
    # Gather information about the message for the bot to decipher
    username = str(message.author).split('#')[0]
    command = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {command} ({channel})')

    # Check for bot not to respond to self
    if message.author == client.user:
        return
    
    # Commands that only work in a certain channel
    if message.channel.name == BOT_CHANNEL_NAME:
        # Ping Command
        if command.lower() == '!ping':
            await message.channel.send(f'pong!')
            return

        # Server On Command
        elif command.lower() == '!serveron':
            await message.channel.send(f'Turning Server On! It may take a few minutes to be online')
            aternos = Client.from_credentials(USERNAME, PASSWORD)
            servs = aternos.list_servers()
            myserv = servs[0]
            myserv.start()
            return

        # Server Off Command
        elif command.lower() == '!serveroff':
            await message.channel.send(f'Turning Server Off!')
            aternos = Client.from_credentials(USERNAME, PASSWORD)
            servs = aternos.list_servers()
            myserv = servs[0]
            myserv.stop()
            return
            
client.run(TOKEN)