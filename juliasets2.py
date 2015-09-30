class JuliaSet(object):
    
    def __init__(self, c, n=100):
        self.c = c
        self.n = n
        self._d = 0.001
        self._complexplane = np.array([])
        self._set = np.array([])
        


    def makeplane(self):

        i=np.arange(-2,2,self._d)

        self._complexplane=[complex(x,y) for x in i for y in i]

                

    def juliamap(self, z):

        return (z**2) + self.c

    

    def iterate(self, z):

        m = 0

        while True:

            z=self.juliamap(z)

            m = m + 1

            if  abs(z) > 2:

                return m

            if m >=self.n:

                return 0



    def set_spacing(self, d):

        self._d = d

        self.makeplane()



    def generate(self):

        self.set = [self.iterate(z) for z in self._complexplane]

        return self.set

