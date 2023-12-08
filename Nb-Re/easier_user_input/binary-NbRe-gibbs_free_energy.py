#%matplotlib inline
import matplotlib.pyplot as plt
from pycalphad import Database, calculate, variables as v
from pycalphad.plot.utils import phase_legend
import numpy as np

#------User input area--------
tdb_file = 'nbre_liu.tdb'
ELA = 'Nb' 
ELB = 'Re' # x-axis
Temp = 2800 # [K], y-axis
#------User input area--------

img_comps = ELA+ELB

ELA = ELA.upper ()
ELB = ELB.upper ()

# Load database and choose the phases that will be plotted
db_nbre = Database(tdb_file)
#------User input area--------
my_phases_nbre = ['CHI_RENB', 'SIGMARENB', 'FCC_RENB', 'LIQUID_RENB', 'BCC_RENB', 'HCP_RENB']
#------User input area--------

# Get the colors that map phase names to colors in the legend
legend_handles, color_dict = phase_legend(my_phases_nbre)

fig = plt.figure(figsize=(9,6))
ax = fig.gca()

# Loop over phases, calculate the Gibbs energy, and scatter plot GM vs. X(ELB)
for phase_name in my_phases_nbre:
    result = calculate(db_nbre, [ELA, ELB], phase_name, P=101325, T=Temp, output='GM')
    ax.scatter(result.X.sel(component=ELB), result.GM, marker='.', s=5, color=color_dict[phase_name])

# Format the plot
ax.set_xlabel('x('+ELB.capitalize()+')')
ax.set_ylabel('Gibbs energy [J/mol]')
ax.set_xlim((0, 1))
ax.legend(handles=legend_handles, loc='center left', bbox_to_anchor=(1, 0.6))

plt.rcParams['savefig.bbox'] = 'tight'
output_file = 'binary-'+img_comps+"-"+str(Temp)+'K-gibbs_free_energy.png'
plt.savefig(output_file)

plt.show()