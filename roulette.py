import random
from telegram import Update
from telegram.ext import CallbackContext
from database import get_participants

async def start_roulette(update: Update, context: CallbackContext):
    participants = get_participants()

    if not participants:
        await update.message.reply_text("Tidak ada peserta yang terdaftar untuk roulette.")
        return

    winner = random.choice(participants)
    await update.message.reply_text(f"🎉 Pemenang adalah: {winner} 🎉")
