import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('alcrni_dup.tdb') # You can get 'alcrni_dup.tdb' file from CPDDB.
comps = ['AL', 'CR', 'NI', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 1573, v.P:101325, v.X('CR'): (0,1,0.015), v.X('AL'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('CR'), y=v.X('AL'))

plt.show()
