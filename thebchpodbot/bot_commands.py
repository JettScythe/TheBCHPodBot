from telegram.ext import CallbackContext, ContextTypes
from telegram import Update
from helpers.price import get_fiat_value, supported_currencies
import logging
from bitcash.network import NetworkAPI

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text(
        "Welcome to TheBCHPodBot! Please write /help to see the commands available.")


async def bot_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("""Available Commands =>
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


async def youtube_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/@BitcoinCashPodcast")


async def faq_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("FAQ Link =>\
        https://bitcoincashpodcast.com/faqs")


async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("View the Website =>\
        https://bitcoincashpodcast.com")


async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Enjoy the Music =>\
        https://www.youtube.com/playlist?list=PLo1CFIKcwE6IflqM8eByDFSUs_POPjmxG")


async def twitch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Watch the Podcast LIVE! =>\
        https://www.twitch.tv/thebitcoincashpodcast")


async def twitter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Follow us on Twitter => \
        https://twitter.com/TheBCHPodcast")


async def cashrain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Sign up for our CashRain Community =>\
        https://cashrain.com/BitcoinCashPodcast")


async def telegram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Join the Discussion! => \
        https://t.me/thebitcoincashpodcast_discussion")


async def pod_announce(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Don't miss any announcements! =>\
        https://t.me/thebitcoincashpodcast")


async def latest_ep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass


async def most_watched(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Check out Podcast Stats here =>\
        https://bitcoincashpodcast.com/stats")


async def roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("View the Roadmap here =>\
        https://bitcoincashpodcast.com/roadmap")


async def motw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("See what it's all about =>\
        https://bitcoincashpodcast.com/about")


async def episodes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("View all episodes here =>\
        https://bitcoincashpodcast.com/docs/welcome")


async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("View BCH-related code=>\
        https://bitcoincashpodcast.com/code")


async def recommended(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Check out these recommended creators and resources=>\
        https://bitcoincashpodcast.com/recommended")


async def clips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Check out Podcast Clips =>\
        https://www.youtube.com/@bchclips3643")


async def latest_clip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass


async def patreon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Become a Patron today! =>\
        https://www.patreon.com/bitcoincashpodcast")


async def noise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Join in on the Noise =>\
        https://noise.cash/u/TheBitcoinCashPodcast")


async def cointree(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("View our Cointree =>\
        https://cointr.ee/bitcoincashpodcast")


async def instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    await update.message.reply_text("Check our our sick pics =>\
        https://www.instagram.com/thebitcoincashpodcast/")


async def listen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass


async def donate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    pass


async def hotdog(update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    if len(context.args) >= 1:
        if context.args[0] == "all":
            price = get_fiat_value()
        else:
            currencies = []
            for arg in context.args:
                if arg.lower() in supported_currencies:
                    currencies.append(arg.lower())
            price = get_fiat_value(currencies)
    else:
        price = get_fiat_value(["usd"])
    if update.message is not None:
        if len(price) >= 4096:
            if update.message.chat.type != "private":  # check if in DM
                return await update.message.reply_html(
                    text="Private message me to see price in all supported currencies",
                )
            else:
                messages = [price[:len(price) // 2], price[len(price) // 2:]]
                for message in messages:
                    await update.message.reply_markdown("```\n{}\n```".format(message), quote=True)
        else:
            await update.message.reply_markdown("```\n{}\n```".format(price), quote=True)
    else:
        pass


async def ratio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    response = "```\n{}\n```".format(get_fiat_value(["btc"]))
    await update.message.reply_markdown(response, quote=True)


async def broadcast_transaction(update, context: CallbackContext):
    user = update.message.from_user
    logger.info("message from %s: %s", user.username, update.message.text)
    txid = NetworkAPI.broadcast_tx(context.args[0])
    if txid.status_code == 200:
        await update.message.reply_text("Broadcast Success! Txid[s]: {}".format(txid.text), quote=True)
    else:
        await update.message.reply_text(
            "Doesn't look like I could broadcast for you right now, confirm balances and try again", quote=True)
