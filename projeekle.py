import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot hazır: {bot.user}")

@bot.command()
async def projeekle(ctx, *, arg):
    try:
        title, desc = arg.split("|")
        embed = discord.Embed(title=title.strip(), description=desc.strip(), color=discord.Color.blue())
        embed.set_footer(text=f"Ekleyen: {ctx.author.display_name}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    except:
        await ctx.send("Hatalı format! Doğru kullanım: `!projeekle Başlık | Açıklama`")

bot.run("MTM1OTUyMTY1NzM3ODgzNjcwMQ.GrZECc.O39-0iGbOHzS4hlrENLG3HUU_ZrCxNqyX63Ymk")
