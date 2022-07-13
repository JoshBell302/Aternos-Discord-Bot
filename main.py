import discord #pip install discord
import os
client = discord.Client()

# Private information may be censored when posting code 
TOKEN = '' # Private
BOT_CHANNEL_NAME = 'bot-test'

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
        if command.lower() == '!ping':
            await message.channel.send(f'pong!')
            return
client.run(TOKEN)