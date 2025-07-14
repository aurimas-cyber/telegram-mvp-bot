class Agent128:
    def __init__(self):
        self.name = "Agent128"
        self.strategy = "neutral"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"