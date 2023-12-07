import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('steel1.TDB')
comps = ['CR', 'FE', 'MO', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 1400, v.P:101325, v.X('CR'): (0,1,0.015), v.X('MO'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('CR'), y=v.X('MO'))

plt.show()
