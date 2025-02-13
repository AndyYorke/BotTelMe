import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from config import BOT_TOKEN
from handlers import start, help_command
from roulette import start_roulette

# Konfigurasi logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Menambahkan handler untuk command
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("roulette", start_roulette))

    logging.info("Bot telah dimulai.")
    app.run_polling()

if __name__ == "__main__":
    main()
