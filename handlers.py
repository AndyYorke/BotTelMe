from telegram import Update
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Halo! Saya adalah bot Telegram yang berjalan di Railway.")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Gunakan /start untuk memulai bot.\nGunakan /roulette untuk memutar roda.")
