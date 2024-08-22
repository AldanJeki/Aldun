import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx):
    await ctx.send("guess a number between 1 and 3")

@bot.command()
async def answer(ctx, n):
    angka = random.randint(1, 3)
    if n == angka:
        await ctx.send("Good job!!!")
    else:
        await ctx.send("you're wrong!!!")

bot.run("MTI3MzYyNTE3OTM5NzgyMDQ3Ng.Gj9tb_.dj0v8pz_kxLRtrvqLpUglxRNHJKpntlPx3NNdM")
