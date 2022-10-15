from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *
from spy import *


app = ApplicationBuilder().token(
    "5708649513:AAGJukd6XFP4QOpESBZM6WumoBRw-iqfgCM").build()
print('server start')

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("xo", xo_command))
app.run_polling()
