import numpy as np
from hamiltonian import *
from constants import *
from scipy.sparse import diags
from scipy.sparse import kron
from scipy.sparse import eye

#particle builder for hamiltonian builder

#single particle case N=1
class single_particle:
    def __init__(self, m = me, spin = None):
        '''
        m: mass of electron set to %me by default
        spin: set to 'None' if spin polarized
        '''

        self.m = m
        self.spin = spin

    def matrix_operators(self, H):
        H.ndim = 2

        x = diags([np.linspace(-H.extent/2, H.extent/2, H.spacing)], [0])
        y = diags([np.linspace(-H.extent/2, H.extent/2, H.spacing)], [0])
        I = eye(H.spacing)

        self.x = kron(I,x)
        self.y = kron(y,I)

        diff_x = diags([-1., 0., 1.], [-1, 0, 1] , shape=(H.spacing, H.spacing))*1/(2*H.dx)
        diff_y = diags([-1., 0., 1.], [-1, 0, 1] , shape=(H.spacing, H.spacing))*1/(2*H.dx)

        self.px = kron(I, - hbar *1j * diff_y)
        self.py = kron(- hbar *1j * diff_x, I)
        
        self.I = kron(I,I)

    def kinetic_term(self, H):

        I = eye(H.spacing)
        T_ =  diags([-2., 1., 1.], [0,-1, 1] , shape=(H.spacing, H.spacing))* -0.5 /(self.m*H.dx**2)
        if H.dim ==1:
            T = T_

        elif H.dim==2:
            T =  kron(T_,I) + kron(I,T_)
        return T
       

class multi_particle:
    def __init__(self, m = me, spin = None):
        """
        args:
        N: number of particles (for N != 1)
        m: mass of electron set to %me by default
        spin: set to 'None' if spin polarized
        """

        self.m = m
        self.spin = spin

    