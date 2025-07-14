class Agent55:
    def __init__(self):
        self.name = "Agent55"
        self.strategy = "scalping"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"