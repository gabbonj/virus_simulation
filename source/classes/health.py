from .. import imports


class Health:

    def __init__(self, strongness=.5, immune=False):
        assert isinstance(strongness, float)
        self.strongness = strongness
        self.immune = immune