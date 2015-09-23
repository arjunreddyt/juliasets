class Juliaset(object):
    
    def __init__(self, c, n=100):
        self.c = c
        self.n = n
        self._d = 0.001
        self._complexplane = []
        self._set = []
