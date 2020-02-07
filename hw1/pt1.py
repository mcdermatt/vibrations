import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Consider the last problem done in class (a collar sliding down a vertical rod) and find the point H* where the collar stops.

# Assume:
# k=2kn/M
# L=0.3m
# L0 = 0.2m
# m = 1.5kg

# 1)- no friction
# 2)- u = 0.2

fig = plt.figure()
ax = fig.gca(projection='3d')

# Hbar- represents dimensionless height
# Hbar = H/L0
Hbar = np.arange(0, 20, 0.2) #evenly spaced values from 0 to 5

#Lbar- represents dimensionless length
#lbar = ((L/L0)-1)^2
lbar = np.arange(0, 500, 5)
Hbar, lbar = np.meshgrid(Hbar, lbar)

#equation
lam = ((lbar-1)**2-(np.sqrt(abs(lbar**2-Hbar**2))**2) / (-1*Hbar))

# Plot the surface.
cmap = mpl.cm.coolwarm
norm = mpl.colors.Normalize(vmin=0,vmax=500000)
surf = ax.plot_surface(Hbar, lbar, lam, cmap=cmap, norm=norm, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.set_xlabel("Hbar")
ax.set_ylabel("Lbar")
ax.set_zlabel("lambda")

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=10, aspect=5,norm=norm,cmap=cmap)


plt.title('Case of No Friction')
plt.show()