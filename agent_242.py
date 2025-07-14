class Agent242:
    def __init__(self):
        self.name = "Agent242"
        self.strategy = "copy"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"