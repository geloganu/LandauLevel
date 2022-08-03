import numpy as np
from constants import *
from hamiltonian import *
from particles import *

def landau(particle):
    #constants
    #e = electron charge
    #B = field strength
    #m = me
    
    #constants
    B = 150*T
    m = me
    
    #cyclotron frequency omega = eB/m
    omega = e*B/m
    
    #angular momentum term
    Lz = -particle.px @ particle.y + particle.py @ particle.x
    
    #x^2 + y^2
    coordTerm = np.dot(particle.x,particle.x)+np.dot(particle.y,particle.y)
    
    return -omega*Lz/2 + m/2*(omega/2)**2*coordTerm

H = hamiltonian(N = 1, spacing = 100, potential = landau, extent = 5, dim = 2)

eigVal, eigVec = H.solve(max_state=10)
print(eigVal)