class Agent300:
    def __init__(self):
        self.name = "Agent300"
        self.strategy = "hedge"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"