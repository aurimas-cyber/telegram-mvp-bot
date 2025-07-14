class Agent90:
    def __init__(self):
        self.name = "Agent90"
        self.strategy = "trend"
        self.risk = "medium"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"