import os
from dotenv import load_dotenv
from core.router import start_bot

def main():
    # Įkeliam aplinkos kintamuosius iš .env failo
    load_dotenv()

    # Paimam BOT_TOKEN iš aplinkos
    token = os.getenv("BOT_TOKEN")

    # Patikrinam, ar BOT_TOKEN rastas
    if not token:
        raise ValueError("BOT_TOKEN nerastas .env faile arba aplinkos kintamuosiuose.")

    # Paleidžiam botą
    start_bot(token)

if __name__ == "__main__":
    main()
