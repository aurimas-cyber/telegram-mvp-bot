class Agent161:
    def __init__(self):
        self.name = "Agent161"
        self.strategy = "copy"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"