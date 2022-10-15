from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import *
import datetime


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/help\n/hello\n/sum')


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loger(update, context)
    await update.message.reply_text(f' Hi {update.effective_user.first_name}!')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loger(update, context)
    await update.message.reply_text(f'{datetime.datetime.now()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    loger(update, context)
    msq = update.message.text
    print(msq)
    items = msq.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')
