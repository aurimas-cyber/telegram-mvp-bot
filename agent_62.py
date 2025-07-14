class Agent62:
    def __init__(self):
        self.name = "Agent62"
        self.strategy = "copy"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"