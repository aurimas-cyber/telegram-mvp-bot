from telegram import Update
from telegram.ext import ContextTypes
from core.modules.ai_agent import ask_gpt
from core.modules.price_feed import get_price
from core.memory import load_memory_stats

# /start
async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Sveikas! Aš esu tavo SuperAI. Naudok komandą /ask klausimui užduoti!")

# /ask
async def handle_ask(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text("❗ Įvesk klausimą: /ask Kas yra AI?")
        return
    response = ask_gpt(query)
    await update.message.reply_text(response)

# /price
async def handle_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin = ' '.join(context.args) or "BTC"
    price = get_price(coin)
    await update.message.reply_text(f"💰 {coin.upper()} kaina: {price}")

# /stats
async def handle_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stats = load_memory_stats()
    await update.message.reply_text(f"📊 Bot atminties statistika:\n{stats}")

# /snipe
async def handle_snipe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Vykdau sniping strategiją... (dar kuriama)")
