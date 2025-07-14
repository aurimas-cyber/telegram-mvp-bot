
from telegram.ext import ApplicationBuilder, CommandHandler
from core.handlers import handle_start, handle_ask, handle_price
from core.env import TELEGRAM_TOKEN

def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", handle_start))
    app.add_handler(CommandHandler("ask", handle_ask))
    app.add_handler(CommandHandler("price", handle_price))
    print("Botas paleistas su SuperAI sistema...")
    app.run_polling()
