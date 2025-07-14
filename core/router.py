from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from telegram import Update

from core.handlers import (
    handle_start,
    handle_ask,
    handle_price,
    handle_stats,
    handle_snipe,
)

def start_bot(token: str):
    app = ApplicationBuilder().token(token).build()

    # Bot commands
    app.add_handler(CommandHandler("start", handle_start))
    app.add_handler(CommandHandler("ask", handle_ask))
    app.add_handler(CommandHandler("price", handle_price))
    app.add_handler(CommandHandler("stats", handle_stats))
    app.add_handler(CommandHandler("snipe", handle_snipe))

    print("🚀 Bot is starting...")
    app.run_polling()
