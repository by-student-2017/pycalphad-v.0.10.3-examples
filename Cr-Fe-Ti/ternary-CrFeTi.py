#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('crfeti_wan.tdb') # You can get 'alcrni_dup.tdb' file from CPDDB.
comps = ['CR', 'FE', 'TI', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 1073, v.P:101325, v.X('CR'): (0,1,0.015), v.X('FE'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('CR'), y=v.X('FE'))

plt.show()
