#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('mmc1.TDB') # from TDBDB
comps = ['AL', 'CO', 'NI', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 1273, v.P:101325, v.X('CO'): (0,1,0.015), v.X('AL'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('CO'), y=v.X('AL'))

plt.show()
