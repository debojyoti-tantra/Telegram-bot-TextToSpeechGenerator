import logging
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from gtts import gTTS
import os

# Enable logging to see errors and bot activity
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Function to read the bot token from a file
def get_token(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        logger.error(f"Token file not found at: {file_path}")
        return None

# Define the handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message when the /start command is issued."""
    await update.message.reply_text('Hello! I am a Text-to-Speech bot. Send me any text, and I will convert it to an audio file for you.')

# Define the handler for text messages
async def text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Converts the user's text message to speech and sends it back as an audio file."""
    user_text = update.message.text
    if not user_text:
        return

    # Use user ID to create a unique filename to avoid conflicts
    user_id = update.message.from_user.id
    audio_file_path = f'{user_id}.mp3'

    await update.message.reply_text("Generating your audio, please wait...")

    try:
        # Generate the audio file using Google Text-to-Speech
        tts = gTTS(text=user_text, lang='en', slow=False)
        tts.save(audio_file_path)

        # Send the audio file back to the user
        with open(audio_file_path, 'rb') as audio:
            await context.bot.send_audio(chat_id=update.effective_chat.id, audio=audio, title='Your Speech')
    except Exception as e:
        logger.error(f"Error generating or sending audio: {e}")
        await update.message.reply_text("Sorry, I encountered an error and couldn't process your request.")
    finally:
        # Clean up by deleting the temporary audio file
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)

async def post_init(application: Application) -> None:
    """Sets the bot's commands after initialization."""
    await application.bot.set_my_commands([
        BotCommand("start", "Starts the bot and shows a welcome message"),
    ])

def main() -> None:
    """Starts the bot and sets up handlers."""
    # Get the token from the file
    token = get_token('token.txt')
    if not token:
        print("Could not read token from token.txt. Please ensure the file exists and contains your bot token.")
        return

    # Create the Application instance and set the post_init callback
    application = Application.builder().token(token).post_init(post_init).build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_to_speech))

    print("Bot is starting... Press Ctrl-C to stop.")
    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()