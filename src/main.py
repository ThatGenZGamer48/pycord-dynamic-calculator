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


class CalcView(discord.ui.View):
    def __init__(self):
        self.values = ""
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Clear", style=discord.ButtonStyle.red, custom_id="calc_view:clear"
    )
    async def clear_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values = ""
            await interaction.response.edit_message(
                content=f"You cleared the calculator! Start typing numbers or operations!"
            )
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="9", style=discord.ButtonStyle.green, custom_id="calc_view:nine"
    )
    async def nine_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "9"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="8", style=discord.ButtonStyle.green, custom_id="calc_view:eight"
    )
    async def eight_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "8"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="7", style=discord.ButtonStyle.green, custom_id="calc_view:seven"
    )
    async def seven_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "7"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="=", style=discord.ButtonStyle.grey, custom_id="calc_view:equals"
    )
    async def equals_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            await interaction.response.edit_message(content=eval(self.values))
        except:
            await interaction.channel.send("Please enter proper operations and values!")

    @discord.ui.button(
        label="+", style=discord.ButtonStyle.grey, custom_id="calc_view:plus"
    )
    async def plus_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "+"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="6", style=discord.ButtonStyle.green, custom_id="calc_view:six"
    )
    async def six_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "6"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="5", style=discord.ButtonStyle.green, custom_id="calc_view:five"
    )
    async def five_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "5"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="4", style=discord.ButtonStyle.green, custom_id="calc_view:four"
    )
    async def four_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "4"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="-", style=discord.ButtonStyle.grey, custom_id="calc_view:minus"
    )
    async def minus_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "-"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="*", style=discord.ButtonStyle.grey, custom_id="calc_view:multiply"
    )
    async def multiply_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "*"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="3", style=discord.ButtonStyle.green, custom_id="calc_view:three"
    )
    async def three_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "3"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="2", style=discord.ButtonStyle.green, custom_id="calc_view:two"
    )
    async def two_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "2"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="1", style=discord.ButtonStyle.green, custom_id="calc_view:one"
    )
    async def one_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "1"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")

    @discord.ui.button(
        label="/", style=discord.ButtonStyle.grey, custom_id="calc_view:divide"
    )
    async def divide_callback(
        self, button: discord.ui.Button, interaction: discord.Interaction
    ):
        try:
            self.values += "/"
            await interaction.response.edit_message(content=str(self.values))
        except:
            await interaction.channel.send("There was an error!")


class CalculatorBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("c!"),
            intents=discord.Intents(members=True, messages=True, guilds=True),
            help_command=commands.MinimalHelpCommand(),
            description="A small button-based calculator",
            allowed_mentions=discord.AllowedMentions(
                users=False, roles=False, everyone=False, replied_user=False
            ),
        )
        self.calc_view_added = False

    async def on_ready(self):
        if not self.calc_view_added:
            self.add_view(CalcView())
            self.calc_view_added = True

        print(f"{self.user} is ready! (ID: {self.user.id})")


bot = CalculatorBot()


@bot.slash_command(
    name="startcalc",
    description="Starts the dynamic calculator.",
    guild_ids=GUILD_IDS,
)
async def _startcalc(ctx):
    await ctx.respond("Started calculator", view=CalcView())


@bot.command(
    name="startcalc",
    description="Starts the dynamic calculator.",
)
async def _command_startcalc(ctx):
    await ctx.send("Started calculator", view=CalcView())


bot.run(TOKEN)
