
from telegram import Update
from telegram.ext import ContextTypes
from core.modules.ai_agent import ask_gpt
from core.modules.price_feed import get_price

async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("SuperAI botas aktyvus.")

async def handle_ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    response = ask_gpt(question)
    await update.message.reply_text(response)

async def handle_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin = " ".join(context.args)
    price = get_price(coin)
    await update.message.reply_text(f"{coin.upper()} kaina: ${price}")
