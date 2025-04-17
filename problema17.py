import math

def f(x):
    return math.exp(x)  # Puedes cambiar esta función si es necesario

def segunda_derivada(x0, h):
    return (-f(x0 - 2*h) + 16*f(x0 - h) - 30*f(x0) + 16*f(x0 + h) - f(x0 + 2*h)) / (12 * h**2)

h = 0.1
print(f"f''(0.4) ≈ {segunda_derivada(0.4, h):.6f}")
print(f"f''(0.8) ≈ {segunda_derivada(0.8, h):.6f}")
