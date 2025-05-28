import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 1) Load your .env so DISCORD_TOKEN is in os.environ
load_dotenv()
TOKEN = os.environ["DISCORD_TOKEN"]
YOUR_USER_ID = 1179217779103105075

# 2) Define your bot **before** you ever call bot.run()
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 3) (Re-)register your slash commands
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.tree.command(name="yeet", description="Yeet someone!")
async def yeet(interaction: discord.Interaction, user: discord.Member):
    if interaction.user.id != YOUR_USER_ID:
        await interaction.response.send_message("🚫 You can't use this.", ephemeral=True)
        return
    gif = random.choice([
        "https://tenor.com/view/yeet-lion-king-simba-rafiki-throw-gif-16194362",
    "https://tenor.com/view/camsey-snoopy-flying-fly-peanuts-clouds-house-gif-21093444",
    "https://tenor.com/view/fly-human-fly-float-human-airplane-meme-gif-5277954545468410794",
    "https://tenor.com/view/yeet-naruto-sakura-yeetnaruto-gif-21167415"
    ])
    await interaction.response.send_message(f"**{interaction.user.display_name} yeeted {user.display_name}!**\n{gif}")

@bot.tree.command(name="pretend", description="Pretend to be another user!")
async def pretend(interaction: discord.Interaction, user: discord.Member, message: str):
    if interaction.user.id != YOUR_USER_ID:
        await interaction.response.send_message("🚫 You can't use this.", ephemeral=True)
        return
    member = interaction.guild.get_member(interaction.user.id)
    try:
        await member.edit(nick=user.display_name)
    except discord.Forbidden:
        await interaction.response.send_message(
            "⚠️ I don't have permission to change nicknames here.", ephemeral=True
        )
        return
    await interaction.response.send_message(f"**{user.display_name}:** {message}")

# 4) Finally, run the bot
bot.run(TOKEN)
