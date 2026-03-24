# Fase 2: Exploración: Funciones básicas
# Este script realiza el análisis algebraico y gráfico de las funciones dadas:
# a. f(x) = sqrt(x)
# b. g(x) = |x|
# c. h(x) = 1/x
# d. t(x) = ln(x)

import numpy as np
import matplotlib.pyplot as plt

# Definición de funciones

def f(x):
    return np.sqrt(x)

def g(x):
    return np.abs(x)

def h(x):
    return 1/x

def t(x):
    return np.log(x)

# Dominio y rango
# f(x) = sqrt(x): dominio [0, inf), rango [0, inf)
# g(x) = |x|: dominio (-inf, inf), rango [0, inf)
# h(x) = 1/x: dominio (-inf, 0) U (0, inf), rango (-inf, 0) U (0, inf)
# t(x) = ln(x): dominio (0, inf), rango (-inf, inf)

# Selección de elementos del dominio para evaluar las funciones
x_f = np.array([0, 1, 4, 9, 16])
x_g = np.array([-3, -1, 0, 1, 3])
x_h = np.array([-2, -1, -0.5, 0.5, 1, 2])
x_t = np.array([0.1, 1, 2, 3, 10])

# Evaluación de las funciones
f_values = f(x_f)
g_values = g(x_g)
h_values = h(x_h)
t_values = t(x_t)

# Impresión de valores
print("f(x) = sqrt(x):")
for xi, yi in zip(x_f, f_values):
    print(f"f({xi}) = {yi}")

print("\ng(x) = |x|:")
for xi, yi in zip(x_g, g_values):
    print(f"g({xi}) = {yi}")

print("\nh(x) = 1/x:")
for xi, yi in zip(x_h, h_values):
    print(f"h({xi}) = {yi}")

print("\nt(x) = ln(x):")
for xi, yi in zip(x_t, t_values):
    print(f"t({xi}) = {yi}")

# Graficar las funciones y puntos evaluados
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# f(x) = sqrt(x)
axs[0, 0].plot(x_f, f_values, 'ro', label='Puntos evaluados')
# Para la curva continua
x_cont = np.linspace(0, 20, 400)
axs[0, 0].plot(x_cont, f(x_cont), 'b-', label='f(x) = sqrt(x)')
axs[0, 0].set_title('f(x) = sqrt(x)')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')
axs[0, 0].legend()
axs[0, 0].grid(True)

# g(x) = |x|
axs[0, 1].plot(x_g, g_values, 'ro', label='Puntos evaluados')
x_cont_g = np.linspace(-10, 10, 400)
axs[0, 1].plot(x_cont_g, g(x_cont_g), 'b-', label='g(x) = |x|')
axs[0, 1].set_title('g(x) = |x|')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('g(x)')
axs[0, 1].legend()
axs[0, 1].grid(True)

# h(x) = 1/x
axs[1, 0].plot(x_h, h_values, 'ro', label='Puntos evaluados')
x_cont_h1 = np.linspace(-10, -0.1, 200)
x_cont_h2 = np.linspace(0.1, 10, 200)
axs[1, 0].plot(x_cont_h1, h(x_cont_h1), 'b-')
axs[1, 0].plot(x_cont_h2, h(x_cont_h2), 'b-', label='h(x) = 1/x')
axs[1, 0].set_title('h(x) = 1/x')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('h(x)')
axs[1, 0].legend()
axs[1, 0].grid(True)

# t(x) = ln(x)
axs[1, 1].plot(x_t, t_values, 'ro', label='Puntos evaluados')
x_cont_t = np.linspace(0.01, 20, 400)
axs[1, 1].plot(x_cont_t, t(x_cont_t), 'b-', label='t(x) = ln(x)')
axs[1, 1].set_title('t(x) = ln(x)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('t(x)')
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()