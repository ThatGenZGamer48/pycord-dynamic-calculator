import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import json

load_dotenv()

with open("config.json", "r") as f:
    config_data = json.load(f)
    
GUILD_IDS = config_data["guild_ids"]
TOKEN = config_data["token"]

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("c!"),
    intents=discord.Intents(members=True, messages=True, guilds=True),
    help_command=commands.MinimalHelpCommand(),
    description="A small button-based calculator",
    allowed_mentions=discord.AllowedMentions(
        users=False, roles=False, everyone=False, replied_user=False
    ),
)


class CalcView(discord.ui.View):
    def __init__(self):
        self.values = ""
        super().__init__(timeout=None)

    @discord.ui.button(label="Clear", style=discord.ButtonStyle.green)
    async def clear_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values = ""
            await interaction.response.edit_message(content=f"You cleared the calculator! Start typing numbers or operations!")
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="9", style=discord.ButtonStyle.green)
    async def nine_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "9"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="8", style=discord.ButtonStyle.green)
    async def eight_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "8"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="7", style=discord.ButtonStyle.green)
    async def seven_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "7"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="=", style=discord.ButtonStyle.green)
    async def equals_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            await interaction.response.edit_message(content=eval(self.values))
        except:
            await interaction.channel.send("Please enter proper operations and values!")

    @discord.ui.button(label="+", style=discord.ButtonStyle.green)
    async def plus_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "+"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")
        
    @discord.ui.button(label="6", style=discord.ButtonStyle.green)
    async def six_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "6"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="5", style=discord.ButtonStyle.green)
    async def five_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "5"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="4", style=discord.ButtonStyle.green)
    async def four_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "4"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="-", style=discord.ButtonStyle.green)
    async def minus_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "-"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="*", style=discord.ButtonStyle.green)
    async def multiply_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "*"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="3", style=discord.ButtonStyle.green)
    async def three_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "3"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="2", style=discord.ButtonStyle.green)
    async def two_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "2"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="1", style=discord.ButtonStyle.green)
    async def one_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "1"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(label="/", style=discord.ButtonStyle.green)
    async def divide_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "/"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.slash_command(
    name="startcalc",
    description="Starts the dynamic calculator.",
    guild_ids=GUILD_IDS,
)
async def _startcalc(ctx):
    view = CalcView()
    await ctx.respond("Started calculator", view=view)

@bot.command(
    name="startcalc",
    description="Starts the dynamic calculator.",
)
async def _command_startcalc(ctx):
    view = CalcView()
    await ctx.send("Started calculator", view=view)

bot.run(TOKEN)
