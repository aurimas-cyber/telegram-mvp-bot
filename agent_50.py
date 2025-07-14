class Agent50:
    def __init__(self):
        self.name = "Agent50"
        self.strategy = "trend"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"