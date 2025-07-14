class Agent215:
    def __init__(self):
        self.name = "Agent215"
        self.strategy = "neutral"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"