def f(x):
    return x**2 + 3*x + 1  # Puedes cambiar la función

x = 1.0
h = 0.0001
fp = (f(x + h) - f(x)) / h
print(f"f'({x}) ≈ {fp:.6f}")
