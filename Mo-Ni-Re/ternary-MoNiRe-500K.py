#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

tdb = Database('mmc1.TDB') # from TDBDB (https://avdwgroup.engin.brown.edu/)
comps = ['MO', 'NI', 'RE', 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: 500, v.P:101325, v.X('RE'): (0,1,0.015), v.X('NI'): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X('RE'), y=v.X('NI'))

plt.show()
