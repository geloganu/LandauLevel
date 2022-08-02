import numpy as np
from constants import *

#hamiltonian builder
class hamiltonian:
    def __init__(self, N, grid_points, V, extent, dim): 
        '''
        args:
        N: number of particles
        grid_points: number of intervals on meshgrid
        V: potential term
        extent: spacial extent (come back for units)
        dim: dimensions
        '''

        self.N = N
        self.grid_points = grid_points
        self.V = V
        self.dim = dim

        #dx finite difference value
        self.dx = extent/grid_points


        #ensure N is an integer
        if type(N) != int:
            raise Exception('Particle number N must be of int type.')
        
        #ensure dimensions is correct
        if dim in range(1,3,1):
            raise Exception('Dimension must be either 1, 2 or 3')

    
