class Agent207:
    def __init__(self):
        self.name = "Agent207"
        self.strategy = "sniping"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"