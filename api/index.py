from teleflask import Teleflask
from teleflask.messages import TextMessage
import os

API_KEY = os.getenv("TELEGRAM_TOKEN")
bot = Teleflask(API_KEY, app)

@app.route("/")
def index():
    return "This is awesome, isn't it?"
# end def


# Register the /start command
@bot.command("start")
def start(update, text):
    # update is the update object. It is of type pytgbot.api_types.receivable.updates.Update
    # text is the text after the command. Can be empty. Type is str.
    return TextMessage("<b>Hello!</b> Thanks for using @" + bot.username + "!", parse_mode="html")
# end def


# register a function to be called for updates.
@bot.on_update
def foo(update):
    from pytgbot.api_types.receivable.updates import Update
    assert isinstance(update, Update)
    # do stuff with the update
    # you can use bot.bot to access the pytgbot.Bot's messages functions
    if not update.message:
        return
        # you could use @bot.on_message instead of this if.
    # end if
    if update.message.new_chat_member:
        return TextMessage("Welcome!")
    # end if
# end def
