import os

MEMORY_FILE = "mem.txt"

def load_memory_stats():
    if not os.path.exists(MEMORY_FILE):
        return "📂 Atmintis dar tuščia."
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        data = f.read()
    return f"🧠 Atminties įrašai:\n{data[:1000]}"  # nerodyti per daug

def save_to_memory(text):
    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
