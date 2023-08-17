import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def crash(ctx):
    rand = random.random()
    
    if rand < 0.7:
        random_number = round(random.triangular(1.00, 3.00, 2.50), 2) 
    else:
        random_number = round(random.triangular(3.00, 5.00, 4.00), 2)  
    
    embed = discord.Embed(
        title="Crash Value",
        description=f"crash value: {random_number}",
        color=discord.Color.blue()
    )
    
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1008775844740734996/1141583913911853056/FxiYRy2agAAhDaH.png?width=626&height=626")
    
    await ctx.send(embed=embed)

@bot.command()
async def roulette(ctx):
    colors = ['green', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'blue', 'red', 'red', 'blue', 'blue', 'red', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red']  
    chosen_color = random.choice(colors)
    
    thumbnail_url = "https://media.discordapp.net/attachments/1008775844740734996/1141583913911853056/FxiYRy2agAAhDaH.png?width=1000"  
    
    embed = discord.Embed(
        title="Roulette Result",
        description=f"The roulette landed on: {chosen_color.capitalize()}",
        color=discord.Color.gold() if chosen_color == 'green' else discord.Color.red() if chosen_color == 'red' else discord.Color.blue()
    )
    
    embed.set_thumbnail(url=thumbnail_url)
    
    await ctx.send(embed=embed)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
