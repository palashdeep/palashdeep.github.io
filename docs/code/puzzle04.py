import pandas as pd

def compute_expected_values(R, B):
    E = [[0.0] * (B + 1) for _ in range(R + 1)]
    
    for r in range(R + 1):
        E[r][0] = r
    
    for r in range(1, R + 1):
        for b in range(1, B + 1):
            continuation = (r / (r + b)) * (1 + E[r-1][b]) + \
                          (b / (r + b)) * (-1 + E[r][b-1])
            E[r][b] = max(0, continuation)
    
    return E

R, B = 4, 4
E = compute_expected_values(R, B)

df = pd.DataFrame(
    [[round(E[r][b], 2) for b in range(B + 1)] for r in range(R + 1)],
    index=[f'r={r}' for r in range(R + 1)],
    columns=[f'b={b}' for b in range(B + 1)]
)

print("E(r,b) table for 4 red, 4 black:\n")
print(df.to_markdown())

# Also print full deck value
E_full = compute_expected_values(26, 26)
print(f"\nE(26,26) = {E_full[26][26]:.4f}")