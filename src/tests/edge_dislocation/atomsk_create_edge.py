## Ethan L. Edmunds, December 2024
# Creating edge discloations using Atomks for Lammps simulation

# 

# Import Libraries
import subprocess
import os

# Get the directory where the script it located
pythonScriptDir = os.path.dirname(os.path.abspath(__file__))

# Initialise filename variables to use
unitFilename = 'Fe_unitcell.xsf'
supercellFilename = 'Fe_supercell.xsf'
dislocationFilename = 'edgeDislocations.lmp'

# Initialise directions for unitcell creation
x = '[]' # Burgers vector of dislocation
y = '[]' # Normal to glide plane
z = '[]' # X x Y (Cross product)

# Initialise supercell sizes
topAndBottom = [40, 10, 1]
middle = [41, 10, 1]

# Initialise material specific values
feAngstromValue = 2.866
material = 'Fe'
crystalStructure = 'bcc'

# Create a unitcell for Iron
unitCellCommand = ['atomsk', '--create', crystalStructure, str(feAngstromValue), material, os.path.join(pythonScriptDir, unitFilename)]

# Create the top/bottom
dislocationCommand = ['atomsk', 'supercellFilename', '-dislocation']