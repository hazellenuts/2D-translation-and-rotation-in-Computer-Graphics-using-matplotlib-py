import matplotlib.pyplot as plt

# Function to translate point
def translate_point(P, T):

    # Cetak koordinat asal
    print("Koordinat Asal: ({}, {})".format(P[0], P[1]))

    # Hitung koordinat baru setelah translasi
    P_new = [P[0] + T[0], P[1] + T[1]]

    # Cetak koordinat hasil translasi
    print("Koordinat Setelah Translasi: ({}, {})".format(P_new[0], P_new[1]))

    # Kembalikan koordinat baru
    return P_new

# Main function
def main():
    """
    Fungsi utama untuk menjalankan contoh translasi titik dan memvisualisasikannya.
    """

    # Koordinat asal dari titik
    P = [5, 8]

    # Faktor translasi (dx, dy)
    T = [2, 1]

    # Translasi titik P menggunakan faktor translasi T
    P_new = translate_point(P, T)

    # Menggunakan tema latar belakang gelap
    plt.style.use('dark_background')

    # Membuat objek gambar dan sumbu
    fig, ax = plt.subplots()

    # Plot titik asal dengan warna kustom (cyan)
    ax.plot(P[0], P[1], 'o', label='Titik Asal ({},{})'.format(P[0], P[1]), markersize=10, color='lavender')
    ax.text(P[0], P[1], f'({P[0]},{P[1]})', fontsize=12, ha='right', color='ghostwhite')

    # Plot titik hasil translasi dengan warna kustom (magenta)
    ax.plot(P_new[0], P_new[1], 'o', label='Titik Tertranslasi ({},{})'.format(P_new[0], P_new[1]), markersize=10, color='springgreen')
    ax.text(P_new[0], P_new[1], f'({P_new[0]},{P_new[1]})', fontsize=12, ha='left', color='ghostwhite')

    # Gambar garis putus-putus dengan panah untuk menunjukkan translasi
    ax.annotate('', xy=(P_new[0], P_new[1]), xytext=(P[0], P[1]),
                arrowprops=dict(arrowstyle='->', linestyle='--', color='lightgrey'))

    # Mengatur batas sumbu
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Menambahkan grid dengan gaya putus-putus dan warna abu-abu
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax.set_xlabel('Sumbu X', color='white')
    ax.set_ylabel('Sumbu Y', color='white')

    # Mengatur latar belakang hitam pada gambar
    fig.patch.set_facecolor('black')

    # Menambahkan legenda dengan teks berwarna terang
    ax.legend(facecolor='black', edgecolor='white', fontsize=10)

    # Menampilkan judul dengan teks berwarna putih
    plt.title('point translation', color='white')

    # Menampilkan plot
    plt.show()

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()
