import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # Fonction pour la 3D
import numpy as np
from stl import mesh
import matplotlib.tri as mtri


def first():
    global x, y, z, u
    u = np.linspace(-40, 40, 80)
    X = np.meshgrid(u)
    x = 8 * u + 5
    y =  x * x
    z = np.sin(X)
    fig = plt.figure()
    ax = fig.gca(projection='3d')  # Affichage en 3D
    ax.plot_wireframe(x, y, z)  # Tracé filaire
    plt.title("Tracé filaire")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.tight_layout()
    plt.show()

def importstl():
    tri = mtri.Triangulation(u)
    data = np.zeros(len(tri.triangles), dtype=mesh.Mesh.dtype)
    mobius_mesh = mesh.Mesh(data, remove_empty_areas=False)
    mobius_mesh.x[:] = x[tri.triangles]
    mobius_mesh.y[:] = y[tri.triangles]
    mobius_mesh.z[:] = z[tri.triangles]
    mobius_mesh.save('mobius.stl')


if __name__ == '__main__':
    first()
    importstl()
