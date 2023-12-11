#%matplotlib inline # for Jupyter notebooks
import matplotlib.pyplot as plt
from pycalphad import Database
from pycalphad.plot import triangular
from pycalphad import calculate

#------User input area--------
tdb_file = 'modified_almgzn_hay.tdb' # from CPDDB (modifiled)
#tdb_file = 'Qiu_2015_en.TDB' # from CPDDB (modifiled)
ELA = 'Mg' # x-axis
ELB = 'Al' # lower left side
ELC = 'Zn' # y-axis
Temp = 608 # [K]
refcs = 'FCC_A1' # e.g., FCC_A1, etc
#------User input area--------

img_title_comps = ELA+'-'+ELB+'-'+ELC
img_comps = ELA+ELB+ELC

ELA = ELA.upper ()
ELB = ELB.upper ()
ELC = ELC.upper ()

tdb = Database(tdb_file)
comps = [ELA, ELB, ELC, 'VA']

# some sample data, these could be from an equilibrium calculation or a property model.
# here we are calculating the mixing gibbs (free) energy of the FCC_A1 phase at 830K. 
c = calculate(tdb, comps, refcs, output='GM_MIX', T=Temp, P=101325, pdens=5000)

# Here we are getting the values from our plot. 
xs = c.X.values[0, 0, 0, :, 0]  # 1D array of Al compositions
ys = c.X.values[0, 0, 0, :, 1]  # 1D array of Cu compositions
zs = c.GM_MIX.values[0, 0, 0, :]  # 1D array of mixing enthalpies at these compositions

# when we imported the pycalphad.plot.triangular module, it made the 'triangular' projection available for us to use.
fig = plt.figure()
ax = fig.add_subplot(projection='triangular')
ax.scatter(xs, ys, c=zs, 
           cmap='coolwarm', 
           linewidth=0.0)

# label the figure
ax.set_xlabel('X ('+ELA+')')
ax.set_ylabel('X ('+ELB+')')
ax.yaxis.label.set_rotation(60)  # rotate ylabel
ax.yaxis.set_label_coords(x=0.12, y=0.5)  # move the label to a pleasing position
ax.set_title(img_title_comps+' GM_MIX [J/mol] at '+str(Temp)+' [K], Ref='+refcs)

# set up the colorbar
cm = plt.cm.ScalarMappable(cmap='coolwarm')
cm.set_array(zs)
fig.colorbar(cm);

plt.text(-0.05, -0.08, ELC, family='monospace', fontsize=12)
#plt.text(-0.08, 1.08, str(Temp)+' K', family='monospace', fontsize=12)

plt.rcParams['savefig.bbox'] = 'tight'
output_file = 'ternary-'+img_comps+"-"+str(Temp)+'K-gibbs.png'
plt.savefig(output_file)

plt.show()
