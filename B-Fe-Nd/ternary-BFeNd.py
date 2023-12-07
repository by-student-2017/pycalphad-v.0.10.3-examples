import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('bfend_hal.tdb') # You can get 'alcrni_dup.tdb' file from CPDDB.
comps = ['B', 'FE', 'ND', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 1275, v.P:101325, v.X('ND'): (0,1,0.015), v.X('B'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('ND'), y=v.X('B'))

plt.show()
