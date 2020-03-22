from .. import imports

class Health:

    def __init__(self, percentage=.9, strongness=.6):
        assert isinstance(percentage, float)
        assert isinstance(percentage,float)
        self.percentage = percentage
        self.strongness = strongness