class Agent299:
    def __init__(self):
        self.name = "Agent299"
        self.strategy = "scalping"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"