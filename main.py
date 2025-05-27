import discord
from discord.ext import commands
import random

YOUR_USER_ID = 1179217779103105075
import os

TOKEN = os.environ["DISCORD_TOKEN"]
bot.run(TOKEN)

yeet_gifs = [
    "https://tenor.com/view/yeet-lion-king-simba-rafiki-throw-gif-16194362",
    "https://tenor.com/view/camsey-snoopy-flying-fly-peanuts-clouds-house-gif-21093444",
    "https://tenor.com/view/fly-human-fly-float-human-airplane-meme-gif-5277954545468410794",
    "https://tenor.com/view/yeet-naruto-sakura-yeetnaruto-gif-21167415"
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
@bot.tree.command(
    name="pretend",
    description="Pretend to be another user!"
)
async def pretend(
    interaction: discord.Interaction,
    user: discord.Member,         # the user to impersonate
    message: str                  # the message you want to say
):
    # Restrict to only you
    if interaction.user.id != YOUR_USER_ID:
        await interaction.response.send_message(
            "🚫 You can't use this.", ephemeral=True
        )
        return

    # Change your nickname in this guild
    try:
        await interaction.guild.get_member(interaction.user.id).edit(
            nick=user.display_name
        )
    except discord.Forbidden:
        await interaction.response.send_message(
            "⚠️ I don't have permission to change nicknames here.",
            ephemeral=True
        )
        return

    # Send the pretend message, prefixed by the impersonated name
    content = f"**{user.display_name}:** {message}"
    await interaction.response.send_message(content)
bot.run(TOKEN)
