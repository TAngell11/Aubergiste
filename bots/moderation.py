import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'{member.name} a été exclu(e).')

bot.run(token=token) 
