import numpy as np
import matplotlib.pyplot as plt

# --- Funciones Grupo 1 ---
def g1_f1(x): return np.sqrt(x + 2)
def g1_f2(x): return np.sqrt(x - 3)
def g1_f3(x): return np.abs(x) + 4
def g1_f4(x): return np.abs(x) - 3

# --- Funciones Grupo 2 ---
def g2_f1(x): return np.sqrt(x - 4)   # dominio x >= 4
def g2_f2(x): return np.sqrt(x + 3)   # dominio x >= -3
def g2_f3(x): return np.abs(x + 2)
def g2_f4(x): return np.abs(x - 3)

# --- Funciones Grupo 3 ---
def g3_f1(x): return -np.sqrt(x)      # dominio x >= 0
def g3_f2(x): return np.sqrt(-x)      # dominio x <= 0
def g3_f3(x): return np.abs(-x)
def g3_f4(x): return -np.abs(x)

# Rango general
x_full = np.linspace(-10, 10, 400)

# Dominios específicos (corregidos)
x_g1_f1 = np.linspace(-2, 10, 400)
x_g1_f2 = np.linspace(3, 10, 400)

x_g2_f1 = np.linspace(4, 10, 400)
x_g2_f2 = np.linspace(-3, 10, 400)   # <-- CORRECCIÓN: x >= -3
# x_g2_f2 antes era [-10, -3] lo que no mostraba bien la raíz

# Para grupo 3
x_g3_f1 = np.linspace(0, 10, 400)
x_g3_f2 = np.linspace(-10, 0, 400)

# Desplazamiento para etiquetas (en unidades x)
dx = 0.3

# ---------------- FIGURA 1: Grupo 1 ----------------
plt.figure(1, figsize=(10,6))
l1, = plt.plot(x_g1_f1, g1_f1(x_g1_f1), linewidth=2, label=r'$f_1(x)=\sqrt{x+2}$')
l2, = plt.plot(x_g1_f2, g1_f2(x_g1_f2), linewidth=2, label=r'$f_2(x)=\sqrt{x-3}$')
l3, = plt.plot(x_full,  g1_f3(x_full),  linewidth=2, label=r'$f_3(x)=|x|+4$')
l4, = plt.plot(x_full,  g1_f4(x_full),  linewidth=2, label=r'$f_4(x)=|x|-3$')

plt.text(x_g1_f1[10]+dx, g1_f1(x_g1_f1[10]), 'f1', color=l1.get_color())
plt.text(x_g1_f2[10]+dx, g1_f2(x_g1_f2[10]), 'f2', color=l2.get_color())
plt.text(1+dx, g1_f3(1), 'f3', color=l3.get_color())
plt.text(x_full[10]+dx, g1_f4(x_full[10]), 'f4', color=l4.get_color(), verticalalignment='top')

plt.title('Gráficas Grupo 1 de funciones')
plt.xlabel('x'); plt.ylabel('f(x)')
plt.xticks(np.arange(-10, 12, 2)); plt.yticks(np.arange(-5, 12, 2))
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.5); plt.axvline(0, color='black', linewidth=0.5)
plt.legend(); plt.xlim(-10,10); plt.ylim(-5,10)

# ---------------- FIGURA 2: Grupo 2 ----------------
plt.figure(2, figsize=(10,6))
l1, = plt.plot(x_g2_f1, g2_f1(x_g2_f1), linewidth=2, label=r'$f_1(x)=\sqrt{x-4}$')
l2, = plt.plot(x_g2_f2, g2_f2(x_g2_f2), linewidth=2, label=r'$f_2(x)=\sqrt{x+3}$')  # ahora visible
l3, = plt.plot(x_full,  g2_f3(x_full),  linewidth=2, label=r'$f_3(x)=|x+2|$')
l4, = plt.plot(x_full,  g2_f4(x_full),  linewidth=2, label=r'$f_4(x)=|x-3|$')

# Etiquetas: elijo puntos dentro del dominio visible para que no queden fuera
plt.text(x_g2_f1[5]+dx, g2_f1(x_g2_f1[5]), 'f1', color=l1.get_color())
plt.text(0+dx, g2_f2(0), 'f2', color=l2.get_color())          # colocar f2 cerca de x=0 (visible)
plt.text(-1+dx, g2_f3(-1), 'f3', color=l3.get_color())
plt.text(4+dx, g2_f4(4), 'f4', color=l4.get_color())

plt.title('Gráficas Grupo 2 de funciones')
plt.xlabel('x'); plt.ylabel('f(x)')
plt.xticks(np.arange(-10, 12, 2)); plt.yticks(np.arange(-5, 14, 2))
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.5); plt.axvline(0, color='black', linewidth=0.5)
plt.legend(); plt.xlim(-10,10); plt.ylim(-5,12)

# ---------------- FIGURA 3: Grupo 3 ----------------
plt.figure(3, figsize=(10,6))
l1, = plt.plot(x_g3_f1, g3_f1(x_g3_f1), linewidth=2, label=r'$f_1(x)=-\sqrt{x}$')
l2, = plt.plot(x_g3_f2, g3_f2(x_g3_f2), linewidth=2, label=r'$f_2(x)=\sqrt{-x}$')
l3, = plt.plot(x_full,  g3_f3(x_full),  linewidth=2, label=r'$f_3(x)=|-x|$')
l4, = plt.plot(x_full,  g3_f4(x_full),  linewidth=2, label=r'$f_4(x)=-|x|$')

plt.text(x_g3_f1[10]+dx, g3_f1(x_g3_f1[10]), 'f1', color=l1.get_color())
plt.text(x_g3_f2[-10]+dx, g3_f2(x_g3_f2[-10]), 'f2', color=l2.get_color())  # etiqueta en la parte izquierda
plt.text(1+dx, g3_f3(1), 'f3', color=l3.get_color())
plt.text(1+dx, g3_f4(1), 'f4', color=l4.get_color())

plt.title('Gráficas Grupo 3 de funciones')
plt.xlabel('x'); plt.ylabel('f(x)')
plt.xticks(np.arange(-10, 12, 2)); plt.yticks(np.arange(-12, 8, 2))
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.5); plt.axvline(0, color='black', linewidth=0.5)
plt.legend(); plt.xlim(-10,10); plt.ylim(-12,8)

plt.show()