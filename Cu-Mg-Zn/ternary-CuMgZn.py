import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('cumgzn_dre.tdb') # You can get 'alcrni_dup.tdb' file from CPDDB.
comps = ['CU', 'MG', 'ZN', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 673, v.P:101325, v.X('MG'): (0,1,0.015), v.X('ZN'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('MG'), y=v.X('ZN'))

plt.show()
