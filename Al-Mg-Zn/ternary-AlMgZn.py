#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

db_al_cu_y = Database('cost507R.TDB')
comps = ['AL', 'MG', 'ZN', 'VA']
phases = list(db_al_cu_y.phases.keys())
conds = {v.T: 608, v.P:101325, v.X('MG'): (0,1,0.015), v.X('ZN'): (0,1,0.015)}

ternplot(db_al_cu_y, comps, phases, conds, x=v.X('MG'), y=v.X('ZN'))

plt.show()

