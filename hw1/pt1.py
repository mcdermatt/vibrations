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

#plot multiple
# fig2 = plt.figure()
# ax2 = fig2.gca(projection='3d')

# Lambda- represents
# X = 2mg/(k*l0) 
X = np.arange(0, 500, 5) #evenly spaced values from 0 to 5

#Lbar- represents dimensionless length
#lbar = ((L/L0)-1)^2
lbar = np.arange(0, 5, 0.05)
X, lbar = np.meshgrid(X, lbar)

H = 1

#equation
V = np.sqrt((lbar-1)**2 + lbar*H - (np.sqrt(lbar*lbar-H*H)-1)**2)
#Z = 1

# Plot the surface.
surf = ax.plot_surface(X, lbar, V, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.set_xlabel("lambda")
ax.set_ylabel("Lbar")
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)


plt.title('Case of No Friction')
plt.show()