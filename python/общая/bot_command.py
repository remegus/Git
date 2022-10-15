from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import *
from spy import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.now()}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/sum\n')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    new = update.message.text
    new = new.split()
    x = int(new[1])
    y = int(new[2])
    await update.message.reply_text(f'Sum {x} + {y} = {x + y}')


async def xo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)

    await update.message.reply_text(f'/hello\n/time\n/sum\n')
