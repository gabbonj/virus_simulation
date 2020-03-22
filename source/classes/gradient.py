from .. import imports


class Gradient():

    def __init__(self, start, stop):
        assert (type(start) == list or type(start) == tuple) and (type(stop) == list or type(stop) == tuple), \
            'The parameters must be list or tuple'
        assert len(start) == 3 and len(stop) == 3, 'Wrong color format'
        self.start = start
        self.stop = stop

    def get_color(self, percent):
        out = [0, 0, 0]
        if self.start[0] > self.stop[0]:
            out[0] = (self.start[0]+self.stop[0])*(1-percent)
        else:
            out[0] = (self.start[0] + self.stop[0]) * percent
        if self.start[1] > self.stop[1]:
            out[1] = (self.start[1]+self.stop[1])*(1-percent)
        else:
            out[1] = (self.start[1] + self.stop[1]) * percent
        return out