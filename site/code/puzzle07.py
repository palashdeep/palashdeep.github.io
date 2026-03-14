import numpy as np
import matplotlib.pyplot as plt

s = np.linspace(0, 1, 1000)
pnl = 125 * (1 - s) * (3*s - 1)

s_max = 2/3
pnl_max = 125 * (1 - s_max) * (3*s_max - 1)

plt.figure(figsize=(10, 6))
plt.plot(s, pnl, label=r'$pnl = 125 * (1 - s) * (3s - 1)$', color='blue', linewidth=2)

plt.scatter([s_max], [pnl_max], color='red', zorder=5)
plt.annotate(f'Max: (2/3, {pnl_max:.3f})', xy=(s_max, pnl_max), xytext=(s_max+0.02, pnl_max+1), fontsize=10)

plt.title(r'Plot of $pnl = 125 * (1 - s) * (3s - 1)$')
plt.xlabel('spread')
plt.ylabel('expected pnl')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.savefig("pics/puzzle07.png", bbox_inches='tight')

plt.show()