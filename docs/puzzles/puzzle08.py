import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(0.1, 25, 5000)
x = y**(1/y)

y_max = np.e
x_max = np.e**(1/np.e)

plt.figure(figsize=(10, 6))
plt.plot(y, x, label=r'$x = y^{1/y}$', color='blue', linewidth=2)

plt.scatter([y_max], [x_max], color='red', zorder=5)
plt.annotate(f'Max: (e, {x_max:.3f})', xy=(y_max, x_max), xytext=(y_max+1, x_max),)

plt.title(r'Plot of $x = y^{1/y}$')
plt.xlabel('y')
plt.ylabel('x')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig("puzzle08.png", bbox_inches='tight')

plt.show()