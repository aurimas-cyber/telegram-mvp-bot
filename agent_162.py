class Agent162:
    def __init__(self):
        self.name = "Agent162"
        self.strategy = "neutral"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"