
# Text-to-Speech Telegram Bot

This is a simple yet powerful Telegram bot that converts text messages into speech audio files. It's built with Python using the `python-telegram-bot` library for interacting with the Telegram API and `gTTS` for text-to-speech conversion.

## Features

- **Text-to-Speech Conversion**: Converts any text message into a high-quality audio file.
- **Easy to Use**: Simply send a message to the bot, and it will reply with the audio.
- **/start Command**: A welcoming message to guide new users.
- **Command Suggestions**: Suggests the `/start` command when the user types `/`.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**
- **pip** (Python package installer)

## Setup and Installation

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/debojyoti-tantra/Telegram-bot-TextToSpeechGenerator.git
    cd your-repository-name
    ```

2.  **Create a Telegram Bot**:

    - Talk to the [BotFather](https://t.me/BotFather) on Telegram to create a new bot.
    - You will receive a token for your bot. Keep it safe.

3.  **Set up your bot token**:

    - Create a file named `token.txt` in the root of the project directory.
    - Paste your bot token into this file and save it.

4.  **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## How to Run the Bot

Once you have completed the setup, you can start the bot with the following command:

```bash
python bot.py
```

The bot will start polling for new messages. To stop the bot, press `Ctrl-C` in your terminal.

## How to Use the Bot

1.  **Find your bot** on Telegram using the username you chose.
2.  **Send the `/start` command** to see the welcome message.
3.  **Send any text message** to the bot.
4.  The bot will reply with an **audio file** of the text you sent.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
