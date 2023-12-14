from pycalphad import Database, calculate, equilibrium, eqplot
import matplotlib.pyplot as plt
import pycalphad.variables as v

#------User input area--------
tdb_file = 'Li-Na-K-Cs_Cl.dat' # from gitter.im/pycalphad/pycalphad
ELA = 'Cs'  # lower left side (origin)
ELB = 'Li'  # x-axis
ELC = 'Cl'  # fix element
fixc = 0.5  # mole fraction of fix element (ELC)
Temp_Low  = 273 + 327 # [K], y-axis
Temp_High = 273 + 387 # [K], y-axis
#------User input area--------

img_comps = ELA+ELB+"-fix-"+ELC+str(fixc)

ELA = ELA.upper ()
ELB = ELB.upper ()
ELC = ELC.upper ()

# Load database 
tdb = Database(tdb_file)
# Define the components
comps = [ELA, ELB, ELC, 'VA']
# Get all possible phases programmatically
phases = list(tdb.phases.keys())
# Set conditions
conds = {v.P: 101325, v.T: (Temp_Low, Temp_High, 0.1), v.X(ELB): ([0.2, (1.0-1e-4-fixc)]), v.X(ELC): (fixc)}

# calculate equilibrium
calc = equilibrium(tdb, comps, phases, conds)
#calc = equilibrium(tdb, comps, phases, conds, calc_opts={'pdens': 2000})
#print(calc.Phase.values)

fig = plt.figure(figsize=(10,9))
ax = fig.add_subplot()
eqplot(calc, x=v.X(ELB), y=v.T, ax=ax)
#-------------------------------------------------------
plt.rcParams['savefig.bbox'] = 'tight'
output_file = 'plot-'+img_comps+"-"+str(Temp_High)+'K.png'
plt.savefig(output_file, dpi=400)
#-------------------------------------------------------
plt.show()