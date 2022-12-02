from telegram.ext.updater import Updater
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from dotenv import dotenv_values
from commands import *
from messages import *
config = dotenv_values(".env")

updater = Updater(config["TG_API_KEY"],
                  use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('faq', faq_url))
updater.dispatcher.add_handler(CommandHandler('website', website))
updater.dispatcher.add_handler(CommandHandler('music', music))
updater.dispatcher.add_handler(CommandHandler('twitch', twitch))
updater.dispatcher.add_handler(CommandHandler('hotdog', hotdog))
updater.dispatcher.add_handler(CommandHandler('ratio', ratio))
updater.dispatcher.add_handler(CommandHandler('twitter', twitter))
updater.dispatcher.add_handler(CommandHandler("cashrain", cashrain))
updater.dispatcher.add_handler(CommandHandler("telegram", telegram))
updater.dispatcher.add_handler(CommandHandler("announcements", pod_announce))
updater.dispatcher.add_handler(CommandHandler("stats", stats))
updater.dispatcher.add_handler(CommandHandler("roadmap", roadmap))
updater.dispatcher.add_handler(CommandHandler("about", about))
updater.dispatcher.add_handler(CommandHandler("episodes", episodes))
updater.dispatcher.add_handler(CommandHandler("code", code))
updater.dispatcher.add_handler(CommandHandler("recommended", recommended))
updater.dispatcher.add_handler(CommandHandler("clips", clips))
updater.dispatcher.add_handler(CommandHandler("patreon", patreon))
updater.dispatcher.add_handler(CommandHandler("noise", noise))
updater.dispatcher.add_handler(CommandHandler("cointree", cointree))
updater.dispatcher.add_handler(CommandHandler("insta", instagram))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
