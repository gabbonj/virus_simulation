from .. import imports


class Disease:
    
    def __init__(self, sickness=False, spread_rate=.7, percentage=.5):
        assert isinstance(sickness, bool)
        assert isinstance(spread_rate, float)
        assert isinstance(percentage, float)
        self.sickness = sickness
        self.spread_rate = spread_rate
        self.percentage = percentage
        