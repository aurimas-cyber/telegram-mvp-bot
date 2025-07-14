class Agent146:
    def __init__(self):
        self.name = "Agent146"
        self.strategy = "scalping"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"