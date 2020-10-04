import os
import random
import logging
import telegram

from flask import Flask, jsonify, Response, request
app = Flask(__name__)


def generate_cats():    
    cs_all = [
        "👊",
        "💪",
        "⭐️",
        "⚡️",
        "😍",
        "😱",
        "🤙",
        "♻️",
    ]
    
    cs = random.sample(cs_all, 3)
    
    t = f"""
{cs[0]}: {random.randint(4,5)}/5
{cs[1]}: {random.randint(3,5)}/5
{cs[2]}: {random.randint(1,5)}/5
    """
        
    return t
        
    
@app.route('/', methods=['GET'])
def getme():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    bot = telegram.Bot(TELEGRAM_TOKEN)
    return str(bot.get_me())
    

@app.route('/api', methods=['GET', 'POST'])
def api():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    if TELEGRAM_TOKEN is None:
        return jsonify({"status": "error", "reason": "no tg token"})
        
    bot = telegram.Bot(TELEGRAM_TOKEN)
    
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id

        text = generate_cats()  # update.message.text 
        bot.sendMessage(chat_id=chat_id, text=text)
    else:
        return str(bot.get_me())
        
    return jsonify({"status": "ok"})
