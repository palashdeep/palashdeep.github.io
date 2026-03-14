import numpy as np
import matplotlib.pyplot as plt
from math import comb

total = comb(52, 2)  # 1326

k = np.arange(1, 52)
pmf = (52 - k) / total

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(k, pmf * 100, color="#2563eb", alpha=0.85, width=0.7)

# Mode
ax.bar(1, pmf[0] * 100, color="#dc2626", alpha=0.95, width=0.7, label="Mode (k = 1)")

# Reference line at Mean (E[X])
ex = np.sum(k * pmf)
ax.axvline(x=ex, color="#16a34a", linestyle="--", linewidth=1.5, label=f"E[X] ≈ {ex:.2f}")

ax.set_xlabel("Position of First Black Ace (k)", fontsize=12)
ax.set_ylabel("Probability (%)", fontsize=12)
ax.set_title("PMF of the Position of the First Black Ace", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)

ax.set_xlim(0, 52)
ax.tick_params(axis="both", labelsize=10)

plt.tight_layout()
plt.savefig("pics/puzzle02.png", dpi=150)
plt.show()
