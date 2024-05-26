import matplotlib.pyplot as plt
import numpy as np
import magpylib as magpy
from magpylib.magnet import Cuboid, Cylinder

# Crear una figura de Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))

# Crear una cuadrícula de observación en el plano de simetría xz
X, Y = np.mgrid[-50:50:100j, -50:50:100j].transpose((0, 2, 1))
grid = np.stack([X, Y, np.zeros((100, 100))], axis=2)

# Crear un cuboide y un cilindro con polarizaciones y posiciones diferentes
cuboid = Cuboid(position=(0, 0, 0), dimension=(20, 20, 20), magnetization=(0, 0, 500))
cylinder = Cylinder(magnetization=(500, 0, 0), dimension=(40, 20), position=(30, 0, 0))

# Calcular el campo B de ambos imanes en la cuadrícula
B_cuboid = cuboid.getB(grid)
B_cylinder = cylinder.getB(grid)

# Sumar los campos magnéticos de ambos imanes
B_total = B_cuboid + B_cylinder

# Visualización con streamplot utilizando una función de color y ancho de línea
ax.streamplot(
    grid[:, :, 0],
    grid[:, :, 1],
    B_total[:, :, 0],
    B_total[:, :, 1],
    density=1.5,
    color=np.log(np.linalg.norm(B_total, axis=2)),
    linewidth=1,
    cmap="spring_r",
)

# Estilizado de la figura
ax.set(
    xlabel="x-position",
    ylabel="y-position",
    aspect=1,
    xlim=(-50, 50),
    ylim=(-50, 50),
)

# Dibujar el contorno de los límites del cuboide
ax.plot(
    [-10, 10, 10, -10, -10],
    [-10, -10, 10, 10, -10],
    "k--",
    label='Cuboide'
)

# Dibujar el contorno de los límites del cilindro
ts = np.linspace(0, 2 * np.pi, 50)
ax.plot(30 + 10 * np.sin(ts), 10 * np.cos(ts), "b--", label='Cilindro')


ax.legend()
plt.tight_layout()
plt.show()
