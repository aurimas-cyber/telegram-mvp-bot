class Agent42:
    def __init__(self):
        self.name = "Agent42"
        self.strategy = "copy"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"