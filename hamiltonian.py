import numpy as np
from constants import *
from particles import *

#hamiltonian builder
class hamiltonian:
    def __init__(self, N, spacing, V, extent, dim = 2): 
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
        self.extent = extent
        self.observable_count = 0
        self.dim = dim

        #dx finite difference value
        self.dx = extent/spacing

        #ensure N is an integer
        if type(N) != int:
            raise Exception('Particle number N must be of int type.')
        
        #ensure dimensions is correct
        if dim in range(1,3,1):
            raise Exception('Dimension must be either 1, 2 or 3')

        if N == 1:
            self.single_particle.build_operators(self)
        elif N == 2:
            self.multi_particle.build_operators(self)
        



