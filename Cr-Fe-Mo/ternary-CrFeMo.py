#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

#------User input area--------
tdb_file = 'steel1.TDB'
ELA = 'Cr'
ELB = 'Fe'
ELC = 'Mo'
Temp = 1400 # [K]
#------User input area--------

ELA = ELA.upper ()
ELB = ELB.upper ()
ELC = ELC.upper ()

tdb = Database(tdb_file)
comps = [ELA, ELB, ELC, 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: Temp, v.P:101325, v.X(ELA): (0,1,0.015), v.X(ELC): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X(ELA), y=v.X(ELC))

plt.text(-0.1, -0.1, ELB, family='monospace', fontsize=20)
plt.text(-0.1, 1.1, str(Temp)+' K', family='monospace', fontsize=20)

plt.show()
