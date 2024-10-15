import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fungsi untuk merotasi titik (x, y)
def rotate_point(x, y, theta):
    # Mengonversi sudut ke dalam radian
    theta_radians = np.radians(theta)
    
    # Matriks rotasi
    x_new = x * np.cos(theta_radians) - y * np.sin(theta_radians)
    y_new = x * np.sin(theta_radians) + y * np.cos(theta_radians)
    
    return x_new, y_new

# Definisi titik-titik segitiga (A, B, C)
triangle = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])  # Segitiga sama sisi

# Setup plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Membuat garis segitiga pada plot
triangle_plot, = ax.plot([], [], 'b-', lw=2)  # Garis segitiga berwarna biru

# Inisialisasi grafik kosong
def init():
    triangle_plot.set_data([], [])
    return triangle_plot,

# Update posisi segitiga untuk setiap frame
def update(frame):
    theta = frame
    rotated_triangle = np.array([rotate_point(x, y, theta) for x, y in triangle])
    triangle_plot.set_data(np.append(rotated_triangle[:, 0], rotated_triangle[0, 0]),
                           np.append(rotated_triangle[:, 1], rotated_triangle[0, 1]))  # Membuat segitiga tertutup
    return triangle_plot,

# Membuat animasi
ani = FuncAnimation(fig, update, frames=np.arange(0, 90, 2), init_func=init, blit=True, interval=50)

# Menampilkan animasi
plt.grid(True)
plt.show()
