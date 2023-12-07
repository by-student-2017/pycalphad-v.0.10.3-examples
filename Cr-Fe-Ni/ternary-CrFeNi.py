#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('saf2507.TDB')
comps = ['CR', 'FE', 'NI', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 1200, v.P:101325, v.X('CR'): (0,1,0.015), v.X('NI'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('CR'), y=v.X('NI'))

plt.show()
