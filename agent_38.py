class Agent38:
    def __init__(self):
        self.name = "Agent38"
        self.strategy = "trend"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"