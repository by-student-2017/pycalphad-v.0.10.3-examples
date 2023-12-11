#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database, ternplot
from pycalphad import variables as v

#------User input area--------
tdb_file = 'altiv_Lu.tdb' # from CPDDB
#tdb_file = 'AlTiV.TDB' # from TDBDB (Lindahl et al. (2015))
#tdb_file = 'PrecHiMn-04.tdb' # from TDBDB (Hallstedt et al. (2017)) (not recommend for Al-Ti-V system)
#tdb_file = 'Ti-M.TDB_V2.txt' # from TDBDB (Hu et al. (2018)) (not recommend for Al-Ti-V system)
ELA = 'Al' # x-axis
ELB = 'V'  # lower left side
ELC = 'Ti' # y-axis
Temp = 1073 # [K]
#------User input area--------

img_comps = ELA+ELB+ELC

ELA = ELA.upper ()
ELB = ELB.upper ()
ELC = ELC.upper ()

tdb = Database(tdb_file)
comps = [ELA, ELB, ELC, 'VA']
phases = list(tdb.phases.keys())
conds = {v.T: Temp, v.P:101325, v.X(ELA): (0,1,0.015), v.X(ELC): (0,1,0.015)}

ternplot(tdb, comps, phases, conds, x=v.X(ELA), y=v.X(ELC))

plt.text(-0.15, -0.15, ELB, family='monospace', fontsize=20)
plt.text(-0.08, 1.08, str(Temp)+' K', family='monospace', fontsize=20)

plt.rcParams['savefig.bbox'] = 'tight'
output_file = 'ternary-'+img_comps+"-"+str(Temp)+'K.png'
plt.savefig(output_file)

plt.show()