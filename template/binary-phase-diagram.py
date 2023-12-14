#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

#------User input area--------
tdb_file = 'case.TDB' # from TDBDB
ELA = 'Mo' # lower left side (origin)
ELB = 'Ni' # x-axis
Temp = 273 + 1000 # [K], y-axis
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
binplot(tdb, comps, phases, {v.N: 1, v.P:101325, v.T: (300, Temp, 10), v.X(ELB):(1e-4, 1.0, 0.02)})

plt.rcParams['figure.figsize'] = (10,9)
plt.rcParams['savefig.bbox'] = 'tight'
output_file = 'binary-'+img_comps+"-"+str(Temp)+'K.png'
plt.savefig(output_file, dpi=400)

plt.show()
