siswa_list = []

def tampilkan_menu():
    print("\nMenu Manajemen Data Siswa")
    print("1. Tambah Siswa")
    print("2. Lihat Daftar Siswa")
    print("3. Edit Data Siswa")
    print("4. Hapus Siswa")
    print("5. Keluar")

def tambah_siswa():
    nama = input("Masukkan Nama Siswa: ")
    usia = input("Masukkan Usia Siswa: ")
    nilai = input("Masukkan Nilai Rata-rata Siswa: ")
    siswa_list.append({"Nama": nama, "Usia": usia, "Nilai": nilai})
    print("Siswa berhasil ditambahkan!")

def lihat_siswa():
    if not siswa_list:
        print("Tidak ada data siswa.")
    else:
        print("\nDaftar Siswa:")
        for i, siswa in enumerate(siswa_list, start=1):
            print(f"{i}. Nama: {siswa['Nama']}, Usia: {siswa['Usia']}, Nilai: {siswa['Nilai']}")

def edit_siswa():
    lihat_siswa()
    indeks = int(input("Pilih nomor siswa yang ingin diedit: ")) - 1
    if 0 <= indeks < len(siswa_list):
        for key in siswa_list[indeks]:  
            siswa_list[indeks][key] = input(f"Masukkan {key} baru: ") or siswa_list[indeks][key]
        print("Data siswa berhasil diperbarui!")
    else:
        print("Nomor siswa tidak valid.")

def hapus_siswa():
    lihat_siswa()
    indeks = int(input("Pilih nomor siswa yang ingin dihapus: ")) - 1
    if 0 <= indeks < len(siswa_list):
        siswa_list.pop(indeks)
        print("Siswa berhasil dihapus!")
    else:
        print("Nomor siswa tidak valid.")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        lihat_siswa()
    elif pilihan == "3":
        edit_siswa()
    elif pilihan == "4":
        hapus_siswa()
    elif pilihan == "5":
        print("Terima kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")