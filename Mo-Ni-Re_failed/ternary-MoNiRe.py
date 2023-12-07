#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('BEF.TDB')
comps = ['MO', 'NI', 'RE', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 1500, v.P:101325, v.X('RE'): (0,1,0.015), v.X('NI'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('RE'), y=v.X('NI'))

plt.show()
