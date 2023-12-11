#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

#------User input area--------
tdb_file = 'Cri_2015.TDB' # TDBDB
ELA = 'Re' # x-axis
ELB = 'Mo' # lower left side
ELC = 'Ni' # y-axis
Temp = 500 # [K]
#------User input area--------
# It is preferable to specify elements in "ELA, ELB and ELC" in alphabetical order.

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
