from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

# List of supported emojis for reactions
SUPPORTED_EMOJIS = ["👍", "❤️", "😂", "🔥", "😢", "😡", "🤩", "👏", "😎", "🙌",
                    "🎉", "💪", "🤔", "😅", "✅", "😊", "👀", "🎶", "🌟", "💯"]

# Create the bot client (Add your API ID, API Hash, and Bot Token in a .env file)
app = nexichat.Client("reaction_bot")

# Function to react to incoming messages with multiple emojis
@app.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        for emoji in SUPPORTED_EMOJIS:
            await message.react(emoji)
    except Exception as e:
        print(f"Failed to react to message: {e}")

# Run the bot
if __name__ == "__main__":
    app.run()
