import numpy as np
from constants import *

#hamiltonian builder
class hamiltonian:
    def __init__(self, N, dim = 2, spacing, V, extent): 
        '''
        args:
        N: number of particles
        spacing: number of intervals/gridpoints on meshgrid
        V: potential term
        extent: spacial extent (come back for units)
        dim: dimensions
        '''

        self.N = N
        self.spacing = spacing
        self.V = V
        self.dim = dim
        self.observable_count = 0

        #dx finite difference value
        self.dx = extent/spacing

        #ensure N is an integer
        if type(N) != int:
            raise Exception('Particle number N must be of int type.')
        
        #ensure dimensions is correct
        if dim in range(1,3,1):
            raise Exception('Dimension must be either 1, 2 or 3')


