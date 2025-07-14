class Agent14:
    def __init__(self):
        self.name = "Agent14"
        self.strategy = "sniping"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"