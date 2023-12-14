#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

#------User input area--------
tdb_file = 'case.TDB' # from TDBDB
ELA = 'Mo' # lower left side (origin)
ELB = 'Ni' # x-axis
ELC = 'Re' # y-axis
Temp = 273 + 1000 # [K]
#------User input area--------

img_comps = ELA+ELB+ELC

ELA = ELA.upper ()
ELB = ELB.upper ()
ELC = ELC.upper ()

tdb = Database(tdb_file)
comps = [ELA, ELB, ELC, 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: Temp, v.P:101325, v.X(ELB): (1e-4,1,0.015), v.X(ELC): (1e-4,1,0.015)}

fig = plt.figure(figsize=(10, 9))
ax = fig.add_subplot(projection='triangular')

ternplot(tdb, comps, phases, conds, x=v.X(ELB), y=v.X(ELC), ax=ax)

plt.text(-0.15, -0.15, ELA, family='monospace', fontsize=20)
plt.text(-0.08, 1.08, str(Temp)+' K', family='monospace', fontsize=20)

plt.rcParams['savefig.bbox'] = 'tight'
output_file = 'ternary-'+img_comps+"-"+str(Temp)+'K.png'
plt.savefig(output_file, dpi=400)

plt.show()

# Ref: Ternary figure size #371 (https://github.com/pycalphad/pycalphad/issues/371)