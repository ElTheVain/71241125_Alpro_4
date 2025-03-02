def jumlah_hari(bulan):
    hari_per_bulan = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bulan < 1 or bulan > 12:
        return "Bulan tidak valid"
    return hari_per_bulan[bulan - 1]
try:
    bulan = int(input("Masukkan bulan (1-12): "))
    print(f"Jumlah hari: {jumlah_hari(bulan)}")
except ValueError:
    print("Harap masukkan angka yang valid (1-12).")

