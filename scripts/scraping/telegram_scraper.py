import os
import json
import logging
from dotenv import load_dotenv
from telethon.sync import TelegramClient

# Load environment variables
load_dotenv()

# Configure logging


# Ensure logs directory exists at the project root
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_dir, "scraping.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Get credentials from .env file
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

# Define channels to scrape
CHANNELS = {
    "DoctorsET": "https://t.me/DoctorsET",
    "Chemed": "https://t.me/CheMed123",
    "Lobelia4Cosmetics": "https://t.me/lobelia4cosmetics",
    "Yetenaweg": "https://t.me/yetenaweg",
    "EAHCI": "https://t.me/EAHCI"
}

# Initialize Telegram Client
client = TelegramClient("session_name", API_ID, API_HASH)
client.connect()

if not client.is_user_authorized():
    print("Please authorize the client by logging in.")

def scrape_telegram_channel(channel_name, channel_url, max_messages=100):
    """
    Scrapes messages from a given Telegram channel.
    Saves messages to a JSON file inside 'data/raw/telegram/'.
    """
    try:
        print(f"Scraping {channel_name}...")
        messages = []

        # Fetch messages
        for message in client.iter_messages(channel_url, limit=max_messages):
            messages.append({
                "message_id": message.id,
                "text": message.text,
                "date": str(message.date),
                "media": message.media is not None
            })

        # Store in JSON
        save_path = f"data/raw/telegram/{channel_name}.json"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=4)

        logging.info(f"Successfully scraped {len(messages)} messages from {channel_name}")
        print(f"✅ Done scraping {channel_name}")

    except Exception as e:
        logging.error(f"Error scraping {channel_name}: {str(e)}")
        print(f"❌ Failed to scrape {channel_name}")

def run_scraping():
    """ Runs scraping for all channels. """
    for name, url in CHANNELS.items():
        scrape_telegram_channel(name, url)
    client.disconnect()
    print("✅ Scraping complete. Check 'data/raw/telegram/' for output.")

if __name__ == "__main__":
    run_scraping()
