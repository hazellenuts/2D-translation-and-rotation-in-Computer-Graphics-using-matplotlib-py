import matplotlib.pyplot as plt

# Function to translate a line
def translate_line(P, T):

    # Cetak koordinat asli
    print("awal: ({}, {}) ke ({}, {})".format(P[0][0], P[0][1], P[1][0], P[1][1]))

    # Menghitung koordinat baru setelah translasi
    P_new = [[P[0][0] + T[0], P[0][1] + T[1]], [P[1][0] + T[0], P[1][1] + T[1]]]

    # Cetak koordinat setelah translasi
    print("tertranslasi: ({}, {}) ke ({}, {})".format(P_new[0][0], P_new[0][1], P_new[1][0], P_new[1][1]))

    # Plotting with Matplotlib
    plt.style.use('dark_background')
    fig, ax = plt.subplots()

    # Plot original line
    ax.plot([P[0][0], P[1][0]], [P[0][1], P[1][1]], color='lavender', label='Garis Asli', linewidth=2)

    # Plot translated line
    ax.plot([P_new[0][0], P_new[1][0]], [P_new[0][1], P_new[1][1]], color='springgreen', label='Garis Tertranslasi', linewidth=2)

    # Annotate original and translated points
    ax.annotate('({},{})'.format(P[0][0], P[0][1]), (P[0][0], P[0][1]), textcoords="offset points", xytext=(0,10), ha='center', color='white')
    ax.annotate('({},{})'.format(P[1][0], P[1][1]), (P[1][0], P[1][1]), textcoords="offset points", xytext=(0,10), ha='center', color='white')
    ax.annotate('({},{})'.format(P_new[0][0], P_new[0][1]), (P_new[0][0], P_new[0][1]), textcoords="offset points", xytext=(0,-15), ha='center', color='white')
    ax.annotate('({},{})'.format(P_new[1][0], P_new[1][1]), (P_new[1][0], P_new[1][1]), textcoords="offset points", xytext=(0,-15), ha='center', color='white')

    # Set axis limits
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 20)

    # Add grid, labels, and legend
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Sumbu X', color='white')
    ax.set_ylabel('Sumbu Y', color='white')
    ax.legend(facecolor='black', edgecolor='white', fontsize=10)

    # Show the plot
    plt.title('line translation', color='white')
    plt.show()

# Driver function
if __name__ == "__main__":
    # Koordinat dari titik awal dan titik akhir garis
    P = [[5, 8], [12, 18]]
    # Faktor translasi
    T = [2, 1]
    translate_line(P, T)
