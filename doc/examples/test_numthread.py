import os
import time
from ScatPy import *
import matplotlib.pyplot as plt

# Establish target geometry (in um)
length = 0.100
radius = 0.020
target = targets.CYLNDRCAP(length, radius, d=0.003, material='AuPalik.txt')

# Create a job to be run in the subdirectory tmp/
job = DDscat(folder = './tmp', target=target)

# Change the range of calculated wavelengths and ambient index
job.settings.wavelengths = ranges.How_Range(0.300, 0.600, 1)
job.settings.NAMBIENT = 1.0

t = []
for i in range(7):
    t0 = time.time()
    nthtread = i + 1
    print('Using ' + str(nthtread) + ' threads')
    os.environ["OMP_NUM_THREADS"] = str(nthtread)
    job.calculate()
    t1 = time.time() - t0
    t.append(t1)

plt.clf()
plt.plot(t)
plt.show()
