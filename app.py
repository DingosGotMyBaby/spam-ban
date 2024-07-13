import discord
from discord import app_commands
import logging
import dotenv
import os

logging.basicConfig(level=logging.DEBUG)
dotenv.load_dotenv()

logging.info("All imported packages and versions: ")
logging.info(f"discord: {discord.__version__}")

MY_GUILD = discord.Object(id=os.environ["GUILD"])  # replace with your guild id
TOKEN = os.environ["TOKEN"]
BAN_CHANNEL = int(os.environ["BANCHANNEL"])
MOD_LOGS = int(os.environ["MODLOGS"])
OWNER = int(os.environ["OWNER"])
COUNTING_MESSAGE = int(os.environ["COUNTINGMESSAGE"]) if os.environ["COUNTINGMESSAGE"] != "None" else None
DEBUG = True if os.environ["DEBUG"] else False
bots = [1078508426923085864, 1176688824508756030]


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        await self.tree.sync()


# intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True),
# intents = discord.Intents.default()
# intents.message_content = True
# intents.guilds = True
# intents.members = True
intents = discord.Intents.all()     


client = MyClient(intents=intents)


@client.event
async def on_ready():
    logging.info(f"Logged in as {client.user} (ID: {client.user.id})") 

    logging.info(f"Guilds: {len(client.guilds)}")
    logging.info(
        f"Invite URL: {discord.utils.oauth_url(client.user.id, permissions=discord.Permissions(permissions=139653810176))}"
    )


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if message.guild.id == MY_GUILD.id:
        if message.channel.id == BAN_CHANNEL:
            # get name of channel
            channel = client.get_channel(BAN_CHANNEL)
            if message.content:
                # Here we ban the user cause they posted in the channel :)
                if not DEBUG:
                    # message.author.ban(reason=f"Posted in the {channel.name} channel.")
                    logging.info(f"{message.author} was banned for posting in {channel.name}.")
                else:
                    await message.channel.send(content=f"{message.author} is a bozo.")
                    logging.info(f"{message.author} was banned for posting in {channel.name}.")

                # Send a message to the mod logs channel
                mod_logs = client.get_channel(MOD_LOGS)
                await mod_logs.send(
                    f"{message.author} was banned for posting in {channel.name}."
                )
                # edit logging message to update the counter
                count_message = await message.channel.fetch_message(COUNTING_MESSAGE)
                await count_message.edit(
                    content=f"Total bans from idiots: {int(count_message.content.split()[-1])+1}"
                )
            else:
                return
    else:
        logging.debug(f"Message from {message.author} in {message.guild.name}({message.guild.id}):{message.channel.name}: {message.content}")
        return
    
# Bootstrap command
@client.tree.command()
# @app_commands.checks.cooldown(1, 600, key=lambda i: (i.guild_id, i.user.id))
@app_commands.describe(channel="The channel you want to have the bans be in")
async def bootstrap(interaction: discord.Interaction, channel: discord.channel.TextChannel):
    """
    Bootstraps the bot to the guild

    Args:
        interaction (discord.Interaction): Discord Interaction
        channel (discord.channel.TextChannel): The channel you want the bot to post to
    """
    if interaction.guild_id != MY_GUILD.id:
        await interaction.response.send_message("You are not in the correct guild.", ephemeral=True)
        return
    if interaction.user.id != OWNER:
        await interaction.response.send_message("You are not authorised to use this command, this has been logged so the bot guy can call you an idiot.", ephemeral=True)
        return
    if interaction.guild_id == MY_GUILD.id:
        message = await channel.send("Total bans from idiots: 0")
        await message.pin()
        await interaction.response.send_message(f"Bootstrapped the bot. Message ID to set in env is {message.id}", ephemeral=True)
        logging.info(f"Bootstrapped the bot. Message ID to set in env is {message.id}")
    else:
        await interaction.response.send_message("You are not in the correct guild.", ephemeral=True)

client.run(TOKEN)