class Agent58:
    def __init__(self):
        self.name = "Agent58"
        self.strategy = "trend"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"