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

# Koordinat awal untuk dua titik yang membentuk garis
line = np.array([[1, 0], [-1, 0]])  # Garis horizontal sepanjang 2 unit

# Setup plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Membuat plot garis
line_plot, = ax.plot([], [], 'b-', lw=2)  # Garis berwarna biru

# Inisialisasi grafik kosong
def init():
    line_plot.set_data([], [])
    return line_plot,

# Update posisi garis untuk setiap frame
def update(frame):
    theta = frame  # Sudut rotasi yang diubah setiap frame
    rotated_line = np.array([rotate_point(x, y, theta) for x, y in line])
    line_plot.set_data(rotated_line[:, 0], rotated_line[:, 1])
    return line_plot,

# Membuat animasi
ani = FuncAnimation(fig, update, frames=np.arange(0, 30, 2), init_func=init, blit=True, interval=50)

# Menampilkan animasi
plt.grid(True)
plt.show()
