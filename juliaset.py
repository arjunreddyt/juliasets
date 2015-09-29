class JuliaSet(object):
    
    def __init__(self, c, n=100):
        self.c = c
        self.n = n
        self._d = 0.001
        self._complexplane = []
        self._set = []
        
        
        def xfrange(start, stop, step):
            while start < stop:
                yield start
                start += step
                
        
        for x in xfrange(-2, 2, self._d): 
            for y in xfrange(-2/self._d, 2/self._d, 1):
                self._complexplane.append(self._d*complex(x,y))
        
    def juliamap(self, z):
        return (z**2) + self.c
    
    def iterate(self, z):
        m = 0
        while True:
            z=self.juliamap(z)
            m = m + 1
            if  abs(z) > 2:
                return m
            if m >=n:
                return 0

    def set_spacing(self, d):
        self._d = d
        self.xfrange()

    def generate(self):
        self._set = [iterate(z) for z in self._complexplane]
        return self._set