class Agent170:
    def __init__(self):
        self.name = "Agent170"
        self.strategy = "trend"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"