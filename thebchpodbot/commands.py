from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from helpers.price import get_fiat_value, supported_currencies
from telegram.parsemode import ParseMode
import logging



# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text(
        "Welcome to TheBCHPodBot! Please write\
        /help to see the commands available.")

def help(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /faq - Link to FAQ
    /website - Link to website
    /music - Playlist of original music
    /twitch - Watch the show live!
    /hotdog - Price of BCH
    /ratio - Ratio of BCH/BTC
    /twitter - Link to Twitter
    /cashrain - Link to cashrain community
    /telegram - Link to TheBCHPodcast Discussion telegram
    /announcements - Link to TheBCHPodcast Announcements channel
    /stats - Links to the Podcast stats
    /roadmap - Links to the "Official" BCH roadmap
    /about - What's this bot about?
    /episodes - Link to all episodes
    /code - Link to website code
    /recommended - Link to recommended
    /clips - Link to clips channel
    /patreon - Link to patreon
    /noise - Link to noise
    /cointree - Link to cointree
    /insta - Link to instagram
    """)

"""
shit to add:
/latestclip - Link to latest clip
/motw - Meme Of The Week
/latestepisode - Links to the latest episode
/mostwatched - Links to the most watched episode
/listen - Link to every platform where you can listen to the podcast
/donate - Send a donation to TheBCHPodcast!

"""

def youtube_url(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/@BitcoinCashPodcast")

def faq_url(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("FAQ Link =>\
        https://bitcoincashpodcast.com/faqs")

def website(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("View the Website =>\
        https://bitcoincashpodcast.com")

def music(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Enjoy the Music =>\
        https://www.youtube.com/playlist?list=PLo1CFIKcwE6IflqM8eByDFSUs_POPjmxG")

def twitch(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Watch the Podcast LIVE! =>\
        https://www.twitch.tv/thebitcoincashpodcast")

def twitter(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Follow us on Twitter => \
        https://twitter.com/TheBCHPodcast")

def cashrain(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Sign up for our CashRain Community =>\
        https://cashrain.com/BitcoinCashPodcast")

def telegram(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Join the Discussion! => \
        https://t.me/thebitcoincashpodcast_discussion")

def pod_announce(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Don't miss any announcements! =>\
        https://t.me/thebitcoincashpodcast")

def latest_ep(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass

def most_watched(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass

def stats(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Check out Podcast Stats here =>\
        https://bitcoincashpodcast.com/stats")

def roadmap(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("View the Roadmap here =>\
        https://bitcoincashpodcast.com/roadmap")

def motw(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass

def about(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("See what it's all about =>\
        https://bitcoincashpodcast.com/about")

def episodes(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("View all episodes here =>\
        https://bitcoincashpodcast.com/docs/welcome")

def code(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("View BCH-related code=>\
        https://bitcoincashpodcast.com/code")

def recommended(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Check out these recommended creators and resources=>\
        https://bitcoincashpodcast.com/recommended")
    pass

def clips(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Check out Podcast Clips =>\
        https://www.youtube.com/@bchclips3643")

def latest_clip(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass

def patreon(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Become a Patron today! =>\
        https://www.patreon.com/bitcoincashpodcast")

def noise(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Join in on the Noise =>\
        https://noise.cash/u/TheBitcoinCashPodcast")

def cointree(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("View our Cointree =>\
        https://cointr.ee/bitcoincashpodcast")

def instagram(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    update.message.reply_text("Check our our sick pics =>\
        https://www.instagram.com/thebitcoincashpodcast/")

def listen(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass

def donate(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass

def hotdog(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    if len(context.args) >= 1:
        currencies = []
        for arg in context.args:
            if arg.lower() in supported_currencies:
                currencies.append(arg.lower())
        price = get_fiat_value(currencies)
    else:
        price = get_fiat_value()
    response = "```\n{}\n```".format(price)
    if update.message is not None:
        update.message.reply_markdown(response, quote=True)
    else:
        pass

def ratio(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    response = "```\n{}\n```".format(get_fiat_value("btc"))
    update.message.reply_markdown(response, quote=True)
