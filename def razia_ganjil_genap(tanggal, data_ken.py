def razia_ganjil_genap(tanggal, data_kendaraan):
    lokasi = ["Gajah Mada", "Hayam Wuruk", "Sisingamangaraja", "Panglima Polim", "Fatmawati", "Tomang Raya"]

    if not 1 <= tanggal <= 31:
        return "Tanggal harus antara 1 sampai 31"
    
    jenis_hari = " ganjil" if tanggal % 2 != 0 else "genap"

    hasil = []

    for nomor_plat in data_kendaraan :
        angka_terakhir = int(nomor_plat.split()[1][-1])
        jenis_nomor = "ganjil" if angka_terakhir % 2 != 0 else "genap"

        if jenis_hari == jenis_nomor :
            hasil.append( f"Kendaraan dengan nomor plat {nomor_plat} BOLEH melintas di {', '.join(lokasi)} pada tanggal {tanggal}.")
        else:
            hasil.append( f"Kendaraan dengan nomor plat {nomor_plat} TIDAK BOLEH melintas di {', '.join(lokasi)} pada tanggal {tanggal}.")

    return hasil

data_kendaraan =["B 444 XXX", "B 123 ABC", "B 789 ZYZ"]
tanggal = 5
print(razia_ganjil_genap(tanggal, data_kendaraan))