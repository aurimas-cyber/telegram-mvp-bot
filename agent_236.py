class Agent236:
    def __init__(self):
        self.name = "Agent236"
        self.strategy = "scalping"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"