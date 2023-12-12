#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

#------User input area--------
tdb_file = 'modified_ASZ_Last.TDB' # from TDBDB
ELA = 'Ag' # x-axis
ELB = 'Zn' # lower left side
ELC = 'Sn' # y-axis
Temp = 273 + 200 # [K]
#------User input area--------

img_comps = ELA+ELB+ELC

ELA = ELA.upper ()
ELB = ELB.upper ()
ELC = ELC.upper ()

tdb = Database(tdb_file)
comps = [ELA, ELB, ELC, 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: Temp, v.P:101325, v.X(ELA): (1e-4,1,0.015), v.X(ELC): (1e-4,1,0.015)} # 0 => 1e-4 for ZeroDivisionError: float division

ternplot(tdb, comps, phases, conds, x=v.X(ELA), y=v.X(ELC))

plt.text(-0.15, -0.15, ELB, family='monospace', fontsize=20)
plt.text(-0.08, 1.08, str(Temp)+' K', family='monospace', fontsize=20)

plt.rcParams['savefig.bbox'] = 'tight'
output_file = 'ternary-'+img_comps+"-"+str(Temp)+'K.png'
plt.savefig(output_file)

plt.show()