import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Function to translate a rectangle
def translate_rectangle(P, T):

    # Cetak koordinat asli
    print("Kotak Awal: ({}, {}) ke ({}, {})".format(P[0][0], P[0][1], P[1][0], P[1][1]))

    # Menghitung koordinat baru setelah translasi
    P_new = [[P[0][0] + T[0], P[0][1] + T[1]], [P[1][0] + T[0], P[1][1] + T[1]]]

    # Cetak koordinat setelah translasi
    print("Kotak Tertranslasi: ({}, {}) ke ({}, {})".format(P_new[0][0], P_new[0][1], P_new[1][0], P_new[1][1]))

    # Plotting using Matplotlib
    plt.style.use('dark_background')
    fig, ax = plt.subplots()

    # Plot original rectangle
    original_rect = Rectangle((P[0][0], P[0][1]), P[1][0] - P[0][0], P[1][1] - P[0][1], fill=None, edgecolor='lavender', linewidth=2, label='Kotak Asli')
    ax.add_patch(original_rect)

    # Plot translated rectangle
    translated_rect = Rectangle((P_new[0][0], P_new[0][1]), P_new[1][0] - P_new[0][0], P_new[1][1] - P_new[0][1], fill=None, edgecolor='springgreen', linewidth=2, label='Kotak Tertranslasi')
    ax.add_patch(translated_rect)

    # Set axis limits
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)

    # Add grid, labels, and legend
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Sumbu X', color='white')
    ax.set_ylabel('Sumbu Y', color='white')
    ax.legend(facecolor='black', edgecolor='white', fontsize=10)

    # Show the plot
    plt.title('Rectangle Translation', color='white')
    plt.show()

# Driver function
if __name__ == "__main__":
    # Koordinat dari pojok kiri atas dan kanan bawah kotak
    P = [[5, 8], [12, 18]]
    # Faktor translasi
    T = [2, 1]
    translate_rectangle(P, T)
