## Ethan L. Edmunds, Dec 2024
# Testing out how to call commands from Atomsk using Python

# Import libraries
import subprocess
import os

subfolder = 'tests'

# Make sure the subfolder exists, if not make it
if not os.path.exists(subfolder):
    os.makedirs(subfolder)

print("Current working directory:", os.getcwd())

# Create a FCC lattice unit cell for Iron Fe
command = ['atomsk', '--create', 'bcc', '2.866', 'Fe', os.path.join(subfolder, 'Fe_unitcell.xsf')]

subprocess.run(command)