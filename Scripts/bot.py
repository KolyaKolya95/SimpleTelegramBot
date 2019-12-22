from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

TG_TOKEN = "812570802:AAFBDPRhA1zlZdQpcc-SJ6AjDqifRCBFoXk"

def message_handler(update, context):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = "incognito"

    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def main():
    print("Run Bot")

    updater = Updater(TG_TOKEN, use_context=True)

    handler = MessageHandler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

