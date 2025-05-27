import discord
from discord.ext import commands
import random

YOUR_USER_ID = 1179217779103105075
import os

TOKEN = os.environ["DISCORD_TOKEN"]
bot.run(TOKEN)

yeet_gifs = [
    "https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif",
    "https://media.giphy.com/media/l0MYKDrQK1a6f6t3S/giphy.gif",
    "https://media.giphy.com/media/f9k1tV7HyORcngKF8v/giphy.gif",
    "https://media.giphy.com/media/j0kQWLN2b2oeM/giphy.gif"
]

intents = discord.Intents.default()
bot     = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    # Sync the slash commands with Discord
    await bot.tree.sync()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.tree.command(name="yeet", description="Yeet someone!")
async def yeet(interaction: discord.Interaction, user: discord.Member):
    if interaction.user.id != YOUR_USER_ID:
        await interaction.response.send_message("🚫 You can't use this.", ephemeral=True)
        return
    gif = random.choice(yeet_gifs)
    await interaction.response.send_message(f"**{interaction.user.display_name} yeeted {user.display_name}!**\n{gif}")

bot.run(TOKEN)
