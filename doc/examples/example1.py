from ScatPy import *
from aotomat.tools.plottools import *

# Establish target geometry (in um)
length = 0.100
radius = 0.020
target = targets.CYLNDRCAP(length, radius, d=0.005, material='AuPalik.txt')

# Create a job to be run in the subdirectory tmp/
job = DDscat(folder = './tmp', target=target)

# Change the range of calculated wavelengths and ambient index
job.settings.wavelengths = ranges.How_Range(0.300, 0.600, 15)
job.settings.NAMBIENT = 1.0

# Run the job locally
job.calculate()

# Open the results qtable, plot Q_sca, and Q_abs, and add a legend
ans = results.QTable(folder = './tmp')
# ax = ans.plot(['Q_sca', 'Q_abs'])
# ax.legend(loc=0)

wl = ans['wave']
Q_sca = ans['Q_sca']
Q_abs = ans['Q_abs']

plt.plot(wl, Q_sca)
plt.plot(wl, Q_abs)
