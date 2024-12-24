from os import environ
from dotenv import load_dotenv # So we can import from the env file
import random # So we can randomise the messages it sends instead of iterating through it
import discord # Discord API
from discord.ext import tasks # Discord extention for loops

# Gets bot token from .env file
token = environ["TOKEN"]

# Bot intents & Init the discord client
intents = discord.Intents.default()
discord_client = discord.Client(intents=intents)

# Set channel object with the IF of the channel the messages will be sent in
channel_id = 1321239842692141056
channel = discord_client.get_channel(channel_id)

#List of messages the bot will randomly choose through
messages = [
    "message1",
    "message2",
    "message3",
    "message4",
    "message5",
    "message6",
    "message7",
    "message8",
    "message9",
    "message10"
]

# Creates a 60min loop 
@tasks.loop(minutes = 1440)
async def send_message():
    # Call channel so we can modify it's value
    global channel
    
    # Making sure channel isn't null
    if channel == None:
        channel = discord_client.get_channel(channel_id)
        
    # Wait for the discord pot to load before it starts posting
    await discord_client.wait_until_ready()
    
    # Logs every time it posts a message
    print("Posted random message.")
    # Sends a random message in from the messages array in the channel
    await channel.send(f"{random.choice(messages)}")

# On bot ready
@discord_client.event
async def on_ready():
    print("* Sending random messages to the channel...")

    # Starts the message sending loop
    send_message.start()
    print("Bot ready.")

# Launches Discord bot
print("+ Loading Discord bot...")
discord_client.run(token)
