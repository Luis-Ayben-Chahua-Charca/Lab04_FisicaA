import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy
from magpylib.magnet import Cuboid, Cylinder
from magpylib import Collection

#creacion de una entidad plot
fig, ax = plt.subplots()

#creacion de entidades
x1 = Cuboid(position=(-4, 0, 3,), dimension=(3, 3, 3), magnetization=(0, 0, 600))
x2 = Cylinder(magnetization=(0, 0, 500), dimension=(3, 5), )

#creacion de colecciones
c = Collection(x1, x2)

#manipulacion individual de los magnets

x2.move((5, 0, -4))

#manipulacion de colecciones
c.move((-2, 0, 0))

#calcular el campo-B en la cuadricula
xs = np.linspace(-10, 10, 33)
zs = np.linspace(-10, 10, 44)
POS = np.array([(x, 0, z) for z in zs for x in xs])
Bs = c.getB(POS).reshape(44, 33, 3)  #vectorizado


#crear la figura
fig = plt.figure(figsize=(9, 5))
ax1 = fig.add_subplot(121, projection='3d')  # eje 3D
ax2 = fig.add_subplot(122)

#despliega el sistema de geometria en ax1
magpy.show(c, subplotAx=ax1, supress=True)

#despliega el campo zx usando matplotlib
X, Z = np.meshgrid(xs, zs)
U, V = Bs[:, :, 0], Bs[:, :, 2]
ax2.streamplot(X, Z, U, V, color=np.log(U ** 2 + V ** 2))

plt.tight_layout()
plt.show()
