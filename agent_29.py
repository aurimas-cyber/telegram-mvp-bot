class Agent29:
    def __init__(self):
        self.name = "Agent29"
        self.strategy = "hedge"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"