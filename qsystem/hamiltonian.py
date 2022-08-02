import numpy as np
from constants import *
from particles import *


import time


#hamiltonian builder
class hamiltonian:
    def __init__(self, N, spacing, V, extent, dim = 2): 
        #args:
        #N: number of particles
        #spacing: number of intervals/gridpoints on meshgrid
        #V: potential term
        #extent: spacial extent (come back for units)
        #dim: dimensions
        
        self.N = N
        self.spacing = spacing
        self.potential = V
        self.extent = extent
        self.observable_count = 0
        self.dim = dim

        #dx finite difference value
        self.dx = extent/spacing

        #ensure N is an integer
        if type(N) != int:
            raise Exception('Particle number N must be of int type.')
        
        #ensure dimensions is correct
        if dim not in range(1,3,1):
            raise Exception('Dimension must be either 1, 2 or 3')

        if N == 1:
            self.particle = single_particle()
        elif N == 2:
            self.particle = multi_particle()

        self.particle.matrix_operators(self)
        #construct Hamiltonian H = T+V (if py and px are not second order, they appear in the potential term V)
        self.T = self.particle.kinetic_term(self)

        self.V = self.potential_term(self)

    def potential_term(self):
        V = self.potential(self.particle_system)

        return V

    def print(self):
        print(self)

    def solve(self, N_solution: int):

        H = self.T + self.V
        print("Hamiltonian constructed...")
        t0 = time.time()

        #eigVal, eigVec = iterate(H, )



        print("Took", time.time() - t0)
        return self.eigenstates



