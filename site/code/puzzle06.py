import random
import matplotlib.pyplot as plt

A = "HHT"
B = "THH"

def penney_trial():
    seq = ""
    while True:
        seq += random.choice(["H", "T"])
        if seq.endswith(A):
            return 0
        if seq.endswith(B):
            return 1

def simulate(n_trials=1000):
    results = []
    wins = 0

    for i in range(1, n_trials + 1):
        wins += penney_trial()
        results.append(wins / i)

    return results

# Run simulation
n_trials = 10000
estimates = simulate(n_trials)

# Plot convergence
plt.figure()
plt.plot(estimates, label="Estimated P(B wins)")
plt.axhline(0.75, linestyle="--", label="Theoretical value (0.75)")
plt.xlabel("Number of simulations")
plt.ylabel("Estimated probability")
plt.title("Monte Carlo convergence for Penney's Game (HHT vs THH)")
plt.legend()
plt.savefig("pics/puzzle06.png", bbox_inches='tight')
plt.show()