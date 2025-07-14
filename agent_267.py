class Agent267:
    def __init__(self):
        self.name = "Agent267"
        self.strategy = "neutral"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"