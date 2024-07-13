# Discord Ban Bot

This is a Python Discord bot that automatically bans users when they post in a specific channel.
It was developed on Python 3.10.14 but should work on any version that is 3.10+

## Prerequisites

Before running the bot, make sure you have the following:

- Python 3.10+ installed
- Discord.py library installed (`pip install discord.py`)

## Setup

1. Clone this repository to your local machine.
2. Create a new Discord bot on the Discord Developer Portal.
3. Make a copy of `.env.example` and call it `.env`
3. Copy the bot token and paste it in the `.env` file.
4. Customize the `.env` file to specify the target channel ID, message id of the message to edit
5. Start the bot and run the bootstrap command to set the bot's message up
6. Shutdown the bot then edit the env file with the values provided by the bootstrap command.
7. Start the bot again

## Usage

Once the bot is running, it will monitor the specified channel for new messages. If a user posts in that channel, they will be automatically banned and the specified ban message will be sent.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [WTFPL](LICENSE).
