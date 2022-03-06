import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="h")

@bot.event
async def on_ready():
 print("봇이 온라인이 되었습니다!")

@bot.command()
async def 안녕(ctx):
 await ctx.send("안녕 만나서 반가워")

bot.run("token")
