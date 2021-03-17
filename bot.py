import discord
import json                         
from discord.ext import commands
import os

with open('./config.json') as f:
    config = json.load(f)

prefix = config.get('prefix')
token = config.get('token')
client = commands.Bot(command_prefix=prefix)
client.remove_command("help") # LEAVE THIS HERE NO MATTER WHAT, REMOVING THIS WILL GIVE YOU A VERY SHITTY COMMAND.

@client.event
async def on_ready():
    print(f"{client.user.name} Has signed in.")
    print('------')

#Thanks to lucas for this one, a lovely Cog loader, because my one was ass.

for filename in os.listdir('./cogs'): 
        if filename.endswith(".py"):
            try:
                client.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e:
                print(f"Failed to load {filename}")
                print(f"[ERROR] {e}")

client.run(token)