t = [1.00, 1.01, 1.02, 1.03, 1.04]
i = [3.10, 3.12, 3.14, 3.18, 3.24]
L = 0.98
R = 0.142

print("t\t e(t) [voltios]")
for k in range(1, len(t) - 1):
    di_dt = (i[k+1] - i[k-1]) / (t[k+1] - t[k-1])
    e = L * di_dt + R * i[k]
    print(f"{t[k]:.2f}\t {e:.6f}")
