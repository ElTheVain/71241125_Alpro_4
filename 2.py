def main():
    try:
        sisi1 = float(input("Masukkan panjang sisi 1: "))
        sisi2 = float(input("Masukkan panjang sisi 2: "))
        sisi3 = float(input("Masukkan panjang sisi 3: "))
        if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
            print("Panjang sisi harus lebih besar dari nol.")
        elif sisi1 == sisi2 == sisi3:
            print("Semua sisi sama panjang.")
        elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
            print("Ada dua sisi yang sama panjang.")
        else:
            print("Tidak ada sisi yang sama panjang.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")
if __name__ == "__main__":
    main()
