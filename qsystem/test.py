import numpy as np
from constants import *
from hamiltonian import *
from particles import *

def landau(particle):
    return particle.I

H = hamiltonian(N = 1, spacing = 400, V = landau, extent = 10, dim = 2)

H.print()

print('hi')