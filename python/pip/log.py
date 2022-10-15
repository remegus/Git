from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from command import *


async def loger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('loger.csv', 'a')
    file.write(
        f"""{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n""")
    file.close()
