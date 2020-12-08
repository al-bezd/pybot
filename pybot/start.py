from telegram.ext import Updater, MessageHandler, Filters, RegexHandler
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from pybot.trans import translate
from telegram import InlineQueryResultArticle, InputTextMessageContent

TOKEN = '1356600163:AAFOxbTrin5ecUqwrbRTiZXyClj_2LxSOyo'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=translate("I'm a bot, please talk to me!"))


def trans(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=translate(' '.join(context.args)))


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=translate("Sorry, I didn't understand that command."))


def reg(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=translate(update.effective_message.text))

if __name__=="__main__":
    dispatcher.add_handler(CommandHandler('trans', trans))
    dispatcher.add_handler(InlineQueryHandler(inline_caps))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'\w+'), reg))
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
