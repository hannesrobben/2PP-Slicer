stl_path = r'C:\Users\hanne\Documents\Seafile\Seafile\Hannes\STL\Saeule_2pp.stl'


from stl import mesh
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def load_stl(file_path):
    return mesh.Mesh.from_file(file_path)

def get_mesh_data(stl_path):
    """
    Extracts vertex coordinates and face indices from an stl_mesh object.

    Parameters:
    stl_mesh (mesh.Mesh): STL mesh object loaded using numpy-stl.

    Returns:
    numpy.ndarray, numpy.ndarray: Array of vertex coordinates, Array of triangular faces.
    """
    stl_mesh = load_stl(stl_path)
    vertices = stl_mesh.points  # Array of vertex coordinates
    faces = stl_mesh.vectors    # Array of triangular faces
    return vertices, faces


def visualize_mesh(vertices, faces):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot vertices
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], c='r', marker='.')

    # Plot triangles
    for triangle in faces:
        print(triangle)
        ax.plot_trisurf( triangle[:,0], triangle[:,1], triangle[:,2])
        
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()



if __name__ == "__main__":
    # Example usage
    vertices, faces = get_mesh_data(stl_path)
    visualize_mesh(vertices, faces)
