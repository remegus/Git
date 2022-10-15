from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('log.csv', 'a+')
    file = file.write()
    await update.message.reply_text(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
