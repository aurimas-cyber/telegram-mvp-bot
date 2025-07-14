from utils.memory import remember, recall

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.memory_key = f"agent_memory_{name}"

    def respond(self, prompt):
        """Čia pagrindinis metodas – agento atsakymas į klausimą."""
        last_memory = recall(self.memory_key)
        answer = f"[{self.name}] Atsakymas į: {prompt}"
        
        # Galima įterpti logiką pagal atmintį
        if last_memory:
            answer += f" (Prisimenu: {last_memory})"

        # Išsaugok paskutinį prompt'ą atminty
        remember(self.memory_key, prompt)
        return answer

    def reset_memory(self):
        """Ištrina šio agento atmintį."""
        forget(self.memory_key)
