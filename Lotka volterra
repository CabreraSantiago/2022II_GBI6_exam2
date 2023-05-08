import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros
a = 1.0
b = 0.1
c = 1.5
d = 0.75

# Definir la función de la ecuación de Lotka-Volterra
def lotka_volterra(x, y, a, b, c, d):
    return np.array([a*x - b*x*y, c*x*y - d*y])

# Crear una cuadrícula para la gráfica
x, y = np.meshgrid(np.linspace(0, 20, 20), np.linspace(0, 20, 20))

# Calcular las tasas de cambio para cada punto de la cuadrícula
dx, dy = lotka_volterra(x, y, a, b, c, d)

# Graficar las líneas de flujo y los puntos de equilibrio
plt.streamplot(x, y, dx, dy, density=1, arrowsize=1, arrowstyle='->')
plt.plot(0, 0, 'ro')
plt.plot(d/c, a/b, 'bo')
plt.xlabel('Población de presas')
plt.ylabel('Población de depredadores')
plt.title('Ecuación de Lotka-Volterra')
plt.show()
