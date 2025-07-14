class Agent44:
    def __init__(self):
        self.name = "Agent44"
        self.strategy = "sniping"
        self.risk = "low"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"