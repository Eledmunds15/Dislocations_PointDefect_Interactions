## Using python with Atomsk to create files with dislocations
# Ethan L. Edmunds

# Set up inspired by Dislocation motion in BCC metals by molecular dynamic: Bulatov

# Import Libraries
import os
import subprocess
import glob
import inspect

# Get the current working directory
current_directory = os.path.dirname(os.path.realpath(__file__))

# Set path to current directory
os.chdir(current_directory)

# Manually set the script name (for interactive environments like Jupyter)
script_name = "create_dislocation_input.py"  # Replace with your script's name, e.g., 'clean_folder.py'

# Get all files in the current directory
files = glob.glob(os.path.join(current_directory, "*"))

# Loop over the list of files and remove them, excluding the script
for file in files:
    try:
        if os.path.isfile(file) and os.path.basename(file) != script_name:
            os.remove(file)  # Remove file
            print(f"Removed: {file}")
        elif os.path.isdir(file) and os.path.basename(file) != script_name:
            os.rmdir(file)  # Remove empty directories if needed
            print(f"Removed directory: {file}")
    except Exception as e:
        print(f"Error removing file {file}: {e}")

# Define filenames
unitcell = "Fe_unitcell.xsf"
superstructure_top_bottom = "Fe_supercell_1.xsf"
superstructure_middle = "Fe_supercell_2.xsf"
dipoleDislocationStructure = "Fe_dislocation_dipole_supercell.lmp"

# Define lattice constant for Fe (BCC)
lattice_constant = 2.866  # in Angstroms (BCC Fe)

# Size of superstructure (top and bottom)
x = 10
y = 10
z = 10

# Size of superstructure (middle)
y_mid = 15

# Define dislocation parameters
dislocation_position_1 = "0.25*box"
dislocation_position_2 = "0.75*box"
dislocation_type = "edge_add"
dislocation_direction = ["X", "Y"]
burgers_vector = "2.860954"
dislocation_parameter = "0.33"

# Create a unit cell of Iron 
subprocess.run(["atomsk", "--create", "bcc", str(lattice_constant), "Fe", "orient", "[111]", "[-101]", "[1-21]", unitcell])
print("Unit Cell created...")

# Create a superstructure of the unit cell to be on the top and bottom of the dislocation
deform_param_top_bot = 0.5/x
subprocess.run(["atomsk", unitcell, "-duplicate", str(x), str(y), str(z), "-deform", "X", str(deform_param_top_bot), "0,0", superstructure_top_bottom])
print("Supercell Top and Bottom created...")

# Create a superstructure of the middle cell
deform_param_mid = -0.5/(x+1)
subprocess.run(["atomsk", unitcell, "-duplicate", str(x+1), str(y_mid), str(z), "-deform", "X", str(deform_param_mid), "0,0", superstructure_middle])
print("Supercell middle created...")

# Create dislocation in the cell
subprocess.run(["atomsk", "--merge", "Y", "3", superstructure_top_bottom, superstructure_middle, superstructure_top_bottom, dipoleDislocationStructure])
print("Final simulation cell created")

