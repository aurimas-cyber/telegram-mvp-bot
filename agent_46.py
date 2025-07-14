class Agent46:
    def __init__(self):
        self.name = "Agent46"
        self.strategy = "scalping"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"