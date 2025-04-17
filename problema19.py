t = [0, 3, 5, 8, 10, 13]
s = [0, 225, 383, 623, 742, 993]

print("Tiempo\tVelocidad (m/s)")
for i in range(1, len(t) - 1):
    v = (s[i+1] - s[i-1]) / (t[i+1] - t[i-1])
    print(f"{t[i]:.1f}\t{v:.6f}")
