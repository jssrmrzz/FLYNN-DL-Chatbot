import random
import aiohttp
import discord
from discord import Embed 
from discord.ext import commands
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents01.json') 
chatbot.train_model()
chatbot.save_model()

print("FLYNN Protocol Activated...")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("qq"):
        response = chatbot.request(message.content[3:]) #3rd letter after "qq" will be read as msg
        await message.channel.send(response)
    await client.process_commands(message)

# client = commands.Bot(command_prefix="!")

# @client.command()
# async def ping(ctx):
#     await ctx.reply("pong")

# @client.command()
# async def lulz(ctx):
#     async with aiohttp.ClientSession() as cd:
#         async with cd.get("https://www.reddit.com/r/memes.json") as r:
#             lulz = await r.json()
#             embed = discord.Embed(color=discord.Color.random())
#             embed.set_image(url=lulz["data"]["children"][random.randint(0, 30)]["data"]["url"])
#             embed.set_footer(text=f"lulz produced by: {ctx.author}")

#             await ctx.send(embed = embed)
load_dotenv()
TOKEN = os.getenv("TOKEN")

client.run(TOKEN) # client ID