def main():
    # Input
    kode_barang = input("Masukkan Kode Barang: ")
    harga_barang = float(input("Masukkan Harga Barang: "))
    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    
    # Hitung bayar
    bayar = harga_barang * jumlah_barang
    
    # Hitung diskon
    if bayar > 150000:
        diskon = bayar * 0.05
    else:
        diskon = 0
    
    # Hitung total bayar
    total_bayar = bayar - diskon
    
    # Output total bayar
    print(f"Total Bayar: {total_bayar:.2f}")

# Jalankan program
if __name__ == "__main__":
    main()


