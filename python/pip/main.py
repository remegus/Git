from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from command import *


app = ApplicationBuilder().token(
    "5708649513:AAGJukd6XFP4QOpESBZM6WumoBRw-iqfgCM").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("time", time_command))


print('Start server')
app.run_polling()
