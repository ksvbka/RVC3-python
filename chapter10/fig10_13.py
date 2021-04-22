import rvcprint
import numpy as np
import matplotlib.pyplot as plt
from machinevisiontoolbox import *

nm = 1e-9


lam = np.arange(350, 750) * nm
cmf = cmfxyz(lam)

plt.plot(lam / nm, cmf)

plt.ylabel('color matching function')
plt.xlabel('Wavelength (nm)')
plt.grid()
plt.xlim(350, 750)
plt.ylim(0, 1.8)
plt.legend(labels=('CIE X', 'CIE Y', 'CIE Z'))

plt.show()

# rvcprint.rvcprint(subfig='a')

plt.clf()



xycolor = showcolorspace('xy')
xycolor = np.flip(xycolor, axis=0)

plt.imshow(xycolor, extent=(0, 0.8, 0, 0.9))

plt.grid()

# lam = np.arange(350, 750) * nm
# xy = lambda2xy(lam)
# print(xy)
# print(xy.shape)
# plt.plot(xy[0:, 0], xy[0:, 1], linewidth=1)  
# following fig10_13.m, colorspace looks a bit different...


plt.show(block=True)
# rvcprint.rvcprint(subfig='b')

