from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

# Do Nothing if not a command

def unknown(update: Update, context: CallbackContext):
    pass


def unknown_text(update: Update, context: CallbackContext):
    pass
