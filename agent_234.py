class Agent234:
    def __init__(self):
        self.name = "Agent234"
        self.strategy = "scalping"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"