from prettytable import PrettyTable

print("Nama    : Rija Aulia Mayatri")
print("NIM     : 2509116011")
print("Kelas   : Sistem Informasi (A)")
print("Program : Sistem Daftar Makanan")
print("-" * 45)

# Data user
users = [
    {"nama": "Aya", "role": "Admin",    "password": "1111"},
    {"nama": "Aryo", "role": "Pengguna", "password": "2222"},
    {"nama": "Lia", "role": "Pengguna", "password": "3333"},
]

# List resep
resep_list = []

# Loop login
while True:
    print("\n===== Login Akun =====")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Role"]
    for i, u in enumerate(users, start=1):
        tabel.add_row([i, u["nama"], u["role"]])
    print(tabel)

    batas_login = 3
    user = None

    while batas_login > 0:
        nama = input("Masukkan Nama: ")
        password = input("Masukkan Password: ")

        user = None
        for u in users:
            if u["nama"] == nama and u["password"] == password:
                user = u
                break

        if user:
            print(f"\nLogin berhasil! Selamat datang, {user['nama']} ({user['role']})\n")
            break
        else:
            batas_login -= 1
            print(f"Login salah. Sisa percobaan: {batas_login}\n")

    if not user:
        print("Kesempatan login habis. Program berhenti.")
        break

    # MENU ADMIN
    if user["role"] == "Admin":
        while True:
            print("========== MENU ADMIN ==========")
            print("1. Lihat Semua Resep")
            print("2. Tambah Resep")
            print("3. Edit Resep")
            print("4. Hapus Resep")
            print("5. Lihat Daftar User")
            print("6. Hapus Akun Pengguna")
            print("7. Logout")
            pilih = input("Pilih (1-7): ")

            if pilih == "1":  # Lihat semua resep
                if not resep_list:
                    print("\nBelum ada resep yang tersimpan.\n")
                else:
                    tabel2 = PrettyTable()
                    tabel2.field_names = ["No", "Nama Resep", "Kategori", "Pemilik"]
                    for i, r in enumerate(resep_list, start=1):
                        tabel2.add_row([i, r["nama"], r["kategori"], r["pemilik"]])
                    print("\n===== DAFTAR RESEP =====")
                    print(tabel2)

                    detail = input("Lihat detail resep tertentu? (Ya/Tidak): ").strip().lower()
                    if detail == "ya":
                        try:
                            nomor = int(input("Masukkan No resep: "))
                            index = nomor - 1
                            if 0 <= index < len(resep_list):
                                r = resep_list[index]
                                print("-" * 45)
                                print(f"Nama Resep     : {r['nama']}")
                                print(f"Kategori       : {r['kategori']}")
                                print(f"Bahan-bahan    : {r['bahan']}")
                                print(f"Peralatan      : {r['peralatan']}")
                                print(f"Langkah        : {r['langkah']}")
                                print(f"Pemilik        : {r['pemilik']}")
                                print("-" * 45)
                            else:
                                print("Nomor tidak valid.\n")
                        except ValueError:
                            print("Input harus angka.\n")

            elif pilih == "2":  # Tambah resep
                print("\n===== Tambah Resep =====")
                nama_resep = input("Nama Resep     : ")
                kategori = input("Kategori       : ")
                bahan = input("Bahan-bahan    : ")
                peralatan = input("Peralatan      : ")
                langkah = input("Langkah-langkah: ")
                resep_list.append({
                    "nama": nama_resep, "kategori": kategori, "bahan": bahan,
                    "peralatan": peralatan, "langkah": langkah,
                    "pemilik": user["nama"]
                })
                print("Resep berhasil ditambahkan!\n")

            elif pilih == "3":  # Edit resep
                if not resep_list:
                    print("\nBelum ada resep.\n")
                else:
                    tabel3 = PrettyTable()
                    tabel3.field_names = ["No", "Nama Resep", "Kategori", "Pemilik"]
                    for i, r in enumerate(resep_list, start=1):
                        tabel3.add_row([i, r["nama"], r["kategori"], r["pemilik"]])
                    print("\n===== PILIH RESEP UNTUK DIEDIT =====")
                    print(tabel3)
                    try:
                        nomor = int(input("Masukkan No resep: "))
                        index = nomor - 1
                        if 0 <= index < len(resep_list):
                            r = resep_list[index]
                            print("\nBagian yang ingin diubah:")
                            print("1. Nama  2. Kategori  3. Bahan  4. Peralatan  5. Langkah")
                            bagian = input("Pilih (1-5): ").strip()
                            if bagian == "1": r["nama"] = input("Nama baru: ")
                            elif bagian == "2": r["kategori"] = input("Kategori baru: ")
                            elif bagian == "3": r["bahan"] = input("Bahan baru: ")
                            elif bagian == "4": r["peralatan"] = input("Peralatan baru: ")
                            elif bagian == "5": r["langkah"] = input("Langkah baru: ")
                            else: print("Pilihan tidak valid.")
                            print("Perubahan disimpan!\n")
                        else:
                            print("Nomor tidak valid.\n")
                    except ValueError:
                        print("Input harus angka.\n")

            elif pilih == "4":  # Hapus resep
                if not resep_list:
                    print("\nBelum ada resep.\n")
                else:
                    tabel4 = PrettyTable()
                    tabel4.field_names = ["No", "Nama Resep", "Kategori", "Pemilik"]
                    for i, r in enumerate(resep_list, start=1):
                        tabel4.add_row([i, r["nama"], r["kategori"], r["pemilik"]])
                    print("\n===== PILIH RESEP UNTUK DIHAPUS =====")
                    print(tabel4)
                    try:
                        nomor = int(input("Masukkan No resep: "))
                        index = nomor - 1
                        if 0 <= index < len(resep_list):
                            r = resep_list[index]
                            yakin = input(f"Yakin menghapus '{r['nama']}'? (Ya/Tidak): ").strip().lower()
                            if yakin == "ya":
                                del resep_list[index]
                                print("Resep dihapus.\n")
                            else:
                                print("Dibatalkan.\n")
                        else:
                            print("Nomor tidak valid.\n")
                    except ValueError:
                        print("Input harus angka.\n")

            elif pilih == "5":  # Lihat daftar user
                tabel_user = PrettyTable()
                tabel_user.field_names = ["No", "Nama", "Role"]
                for i, u in enumerate(users, start=1):
                    tabel_user.add_row([i, u["nama"], u["role"]])
                print("\n===== DAFTAR USER =====")
                print(tabel_user)

            elif pilih == "6":  # Hapus akun pengguna
                target_nama = input("Ketik Nama user yang ingin dihapus: ")
                target = None
                for u in users:
                    if u["nama"] == target_nama and u["nama"] != user["nama"]:
                        target = u
                        break
                if target:
                    konf = input(f"Yakin hapus akun '{target['nama']}'? (Ya/Tidak): ").strip().lower()
                    if konf == "ya":
                        # Hapus resep milik user
                        resep_list = [r for r in resep_list if r["pemilik"] != target["nama"]]
                        # Hapus user
                        users = [u for u in users if u["nama"] != target["nama"]]
                        print("Akun dan seluruh resep miliknya telah dihapus.\n")
                    else:
                        print("Dibatalkan.\n")
                else:
                    print("User tidak ditemukan atau tidak valid.\n")

            elif pilih == "7":  # Logout
                print("\nLogout...\n")
                break

            else:
                print("Pilihan tidak valid!\n")

    # MENU USER
    elif user["role"] == "Pengguna":
        while True:
            print("============ MENU USER ============")
            print("1. Tambah Resep")
            print("2. Lihat Semua Resep")
            print("3. Edit Resep Saya")
            print("4. Hapus Resep Saya")
            print("5. Lihat Daftar User")
            print("6. Logout")
            pilih = input("Pilih (1-6): ")

            if pilih == "1":  # Tambah resep
                print("\n============ Tambah Resep ============")
                nama_resep = input("Nama Resep     : ")
                kategori = input("Kategori       : ")
                bahan = input("Bahan-bahan    : ")
                peralatan = input("Peralatan      : ")
                langkah = input("Langkah-langkah: ")
                resep_list.append({
                    "nama": nama_resep, "kategori": kategori, "bahan": bahan,
                    "peralatan": peralatan, "langkah": langkah,
                    "pemilik": user["nama"]
                })
                print("Resep berhasil ditambahkan!\n")

            elif pilih == "2":  # Lihat semua resep
                if not resep_list:
                    print("\nBelum ada resep.\n")
                else:
                    tabel5 = PrettyTable()
                    tabel5.field_names = ["No", "Nama Resep", "Kategori", "Pemilik"]
                    for i, r in enumerate(resep_list, start=1):
                        tabel5.add_row([i, r["nama"], r["kategori"], r["pemilik"]])
                    print("\n============ DAFTAR RESEP ============")
                    print(tabel5)

            elif pilih == "3":  # Edit resep saya
                resep_saya_idx = [i for i, r in enumerate(resep_list) if r["pemilik"] == user["nama"]]
                if not resep_saya_idx:
                    print("\nKamu belum punya resep.\n")
                else:
                    tabel_saya = PrettyTable()
                    tabel_saya.field_names = ["NoGlobal", "Nama Resep", "Kategori"]
                    for i in resep_saya_idx:
                        r = resep_list[i]
                        tabel_saya.add_row([i + 1, r["nama"], r["kategori"]])
                    print("\n===== RESEP SAYA (untuk diedit) =====")
                    print(tabel_saya)
                    try:
                        no = int(input("Masukkan NoGlobal resep saya: ")) - 1
                        if no in resep_saya_idx:
                            r = resep_list[no]
                            print("\nBagian yang ingin diubah:")
                            print("1. Nama  2. Kategori  3. Bahan  4. Peralatan  5. Langkah")
                            bagian = input("Pilih (1-5): ")
                            if bagian == "1": r["nama"] = input("Nama baru: ")
                            elif bagian == "2": r["kategori"] = input("Kategori baru: ")
                            elif bagian == "3": r["bahan"] = input("Bahan baru: ")
                            elif bagian == "4": r["peralatan"] = input("Peralatan baru: ")
                            elif bagian == "5": r["langkah"] = input("Langkah baru: ")
                            else: print("Pilihan tidak valid.")
                            print("Perubahan disimpan!\n")
                        else:
                            print("Itu bukan resep milikmu / nomor tidak valid.\n")
                    except ValueError:
                        print("Input harus angka.\n")

            elif pilih == "4":  # Hapus resep saya
                resep_saya_idx = [i for i, r in enumerate(resep_list) if r["pemilik"] == user["nama"]]
                if not resep_saya_idx:
                    print("\nKamu belum punya resep.\n")
                else:
                    tabel_saya = PrettyTable()
                    tabel_saya.field_names = ["NoGlobal", "Nama Resep", "Kategori"]
                    for i in resep_saya_idx:
                        r = resep_list[i]
                        tabel_saya.add_row([i + 1, r["nama"], r["kategori"]])
                    print("\n===== HAPUS RESEP SAYA =====")
                    print(tabel_saya)
                    try:
                        no = int(input("Masukkan NoGlobal resep saya: ")) - 1
                        if no in resep_saya_idx:
                            r = resep_list[no]
                            yakin = input(f"Yakin menghapus '{r['nama']}'? (Ya/Tidak): ").strip().lower()
                            if yakin == "ya":
                                del resep_list[no]
                                print("Resep dihapus.\n")
                            else:
                                print("Dibatalkan.\n")
                        else:
                            print("Itu bukan resep milikmu / nomor tidak valid.\n")
                    except ValueError:
                        print("Input harus angka.\n")

            elif pilih == "5":  # Lihat daftar user
                tabel_user = PrettyTable()
                tabel_user.field_names = ["No", "Nama", "Role"]
                for i, u in enumerate(users, start=1):
                    tabel_user.add_row([i, u["nama"], u["role"]])
                print("\n===== DAFTAR USER =====")
                print(tabel_user)

            elif pilih == "6":  # Logout
                print("\nLogout...\n")
                break

            else:
                print("Pilihan tidak valid!\n")
