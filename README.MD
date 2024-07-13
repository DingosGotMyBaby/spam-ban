# Discord Ban Bot

This is a Python Discord bot that automatically bans users when they post in a specific channel.

## Prerequisites

Before running the bot, make sure you have the following:

- Python 3.x installed
- Discord.py library installed (`pip install discord.py`)

## Setup

1. Clone this repository to your local machine.
2. Create a new Discord bot on the Discord Developer Portal.
3. Make a copy of `.env.example` and call it `.env`
3. Copy the bot token and paste it in the `.env` file.
4. Customize the `.env` file to specify the target channel ID, message id of the message to edit
5. Run the `app.py` script to start the bot.

## Usage

Once the bot is running, it will monitor the specified channel for new messages. If a user posts in that channel, they will be automatically banned and receive the specified ban message.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
