#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

#------User input area--------
tdb_file = 'Al-Mg_Zhong.tdb'
ELA = 'Al' 
ELB = 'Mg' # x-axis
Temp = 1573 # [K], y-axis
#------User input area--------

img_comps = ELA+ELB

ELA = ELA.upper ()
ELB = ELB.upper ()

# Load database 
tdb = Database(tdb_file)
# Define the components
comps = [ELA, ELB, 'VA']
# Get all possible phases programmatically
phases = tdb.phases.keys()

# Plot the phase diagram, if no axes are supplied, a new figure with axes will be created automatically
binplot(tdb, comps, phases, {v.N: 1, v.P:101325, v.T: (300, Temp, 10), v.X(ELB):(0, 1, 0.02)})

plt.rcParams['savefig.bbox'] = 'tight'
output_file = 'binary-'+img_comps+"-"+str(Temp)+'K.png'
plt.savefig(output_file)

plt.show()
