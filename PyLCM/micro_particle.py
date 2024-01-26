#import numpy as np
import jax.numpy as np
from matplotlib import pyplot as plt
import random

from PyLCM.parameters import *
from PyLCM.parameters import *
from PyLCM.parcel import *
from PyLCM.condensation import *

class particles:
    def __init__(self,n):
        self.id     = 0
        self.M      = 1.0 # mass
        self.A      = 1.0 # weighting factor
        self.Ns     = 1.0 # Aerosol mass
        self.kappa  = 0.5 # kappa parameter
        self.z      = 0.0 # particle vertical location
    def shuffle(particles_list):
        random.shuffle(particles_list)