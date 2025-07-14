class Agent254:
    def __init__(self):
        self.name = "Agent254"
        self.strategy = "trend"
        self.risk = "high"

    def decide(self, signal):
        if signal == "volatility_high":
            return "buy"
        elif signal == "volatility_low":
            return "sell"
        else:
            return "wait"