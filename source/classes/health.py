from .. import imports


class Health:

    def __init__(self, strongness=.5):
        assert isinstance(strongness, float)
        self.strongness = strongness