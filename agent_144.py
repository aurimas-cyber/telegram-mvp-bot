class Agent144:
    def __init__(self):
        self.name = "Agent144"
        self.strategy = "sniping"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"