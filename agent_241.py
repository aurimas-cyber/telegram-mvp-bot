class Agent241:
    def __init__(self):
        self.name = "Agent241"
        self.strategy = "neutral"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"