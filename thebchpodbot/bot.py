from telegram.ext import CommandHandler, Application, MessageHandler, filters
from dotenv import dotenv_values
from bot_commands import *
from messages import *
config = dotenv_values(".env")


app = Application.builder().token(config["TG_API_KEY"]).build()

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('help', bot_help))
app.add_handler(CommandHandler('youtube', youtube_url))
app.add_handler(CommandHandler('faq', faq_url))
app.add_handler(CommandHandler('website', website))
app.add_handler(CommandHandler('music', music))
app.add_handler(CommandHandler('twitch', twitch))
app.add_handler(CommandHandler('hotdog', hotdog))
app.add_handler(CommandHandler('ratio', ratio))
app.add_handler(CommandHandler('twitter', twitter))
app.add_handler(CommandHandler("cashrain", cashrain))
app.add_handler(CommandHandler("telegram", telegram))
app.add_handler(CommandHandler("announcements", pod_announce))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("roadmap", roadmap))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("episodes", episodes))
app.add_handler(CommandHandler("code", code))
app.add_handler(CommandHandler("recommended", recommended))
app.add_handler(CommandHandler("clips", clips))
app.add_handler(CommandHandler("patreon", patreon))
app.add_handler(CommandHandler("noise", noise))
app.add_handler(CommandHandler("cointree", cointree))
app.add_handler(CommandHandler("insta", instagram))
app.add_handler(CommandHandler("broadcast", broadcast_transaction))
app.add_handler(MessageHandler(filters.TEXT, unknown))
app.add_handler(MessageHandler(filters.COMMAND, unknown))  # Filters out unknown commands

# Filters out unknown messages.
app.add_handler(MessageHandler(filters.TEXT, unknown_text))

app.run_polling()
