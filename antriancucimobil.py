#Kelompok 13 - HDC
#Anggota: Chelsea Claudia Hutapea
#         Dyas Arum Paramitha
#         Haura Nur Hafizhah

#file

namaFile = "carwash.txt" 

def bacaData(namaFile):
    dataList = []

    try:
        with open(namaFile, "r") as file:
            for baris in file:
                baris = baris.strip()

                if baris == "":
                    continue

                plat, status = baris.split(",")

                dataList.append({
                    "plat": plat,
                    "status": status,
                    "pembayaran": pembayaran
                })

    except FileNotFoundError:
        pass
        
    return dataList

#save antrian baru
def simpanData(namaFile, dataList):
    with open(namaFile, "w") as file:
        for data in dataList:
            file.write(f"{data['plat']},{data['status']},{data['pembayaran']}\n")

#add antrian
def tambahAntrian(dataList):
    plat = input("Masukkan nomor polisi kendaraan: ").strip()

    if plat == "":
        print("Nomor polisi tidak boleh kosong.")
        return
        
    print("\nStatus Pembayaran")
    print("1. Sudah lunas")
    print("2. Belum bayar")
    print("3. Belum lunas")

    pilih = input("pilih: ").strip()

    if pilih == "1":
        pembayaran = "Lunas"
    elif pilih == "2":
        pembayaran = "Belum bayar"
    elif pilih == "3":
        pembayaran = "Belum lunas"
    else:
        print("pilihan tidak valid.")

    dataList.append({
        "plat": plat,
        "status": "Menunggu",
        "pembayaran": pembayaran
    })

    print("Antrian berhasil ditambahkan.")

#baca/read antrian
def tampilkanAntrian(dataList):
    if len(dataList) == 0:
        print("Antrian kosong.")
        return

    print("DAFTAR ANTRIAN")
    for i, data in enumerate(dataList, start=1):
        print(
            f"{i}. {data['plat']} | "
            f"{data['status']} |"
            f"{data['pembayaran']}"
        )


#update status antrian
def prosesAntrian(dataList, history):
    if len(dataList) == 0:
        print("Tidak ada antrian.")
        return

    # ambil antrian paling depan (QUEUE)
    data = dataList[0]

    print(f"\nMemproses: {data['plat']}")
    print("1. Sedang Dicuci")
    print("2. Selesai")

    pilihan = input("Pilih status: ").strip()

    if pilihan == "1":
        data["status"] = "Sedang Dicuci"

    elif pilihan == "2":
        data["status"] = "Selesai"

        history.append(data)   # STACK (riwayat)
        dataList.pop(0)        # QUEUE (keluar dari depan)

        print("Mobil selesai & masuk riwayat.")

    else:
        print("Pilihan tidak valid.")

#delete antrian
def hapusAntrian(dataList):
    nama = input("Masukkan nama: ").strip()

    for data in dataList:
        if data["plat"] == plat:
            dataList.remove(data)
            print("Data berhasil dihapus.")
            return

    print("Data tidak ditemukan.")

#show history dgn stack
def tampilkanHistory(history):
    if len(history) == 0:
        print("Belum ada riwayat.")
        return

    print("\n=== RIWAYAT CUCI MOBIL ===")

    # LIFO 
    for data in reversed(history):
         print(
            f"{data['plat']} | "
            f"{data['status']} |"
            f"{data['pembayaran']}"
        )

#pembayaran
def pembayaranMobil(history):
    if len(history) == 0:
        print("Belum ada mobil yang selesai dicuci.")
        return
    plat = input("Masukkan plat mobil: ").strip().upper()
    
    for data in history:
        if data["plat"] == plat:
            print(f"\nPlat Mobil : {data['plat']}")
            print(f"Status Pembayaran : {data['pembayaran']}")

            if data["pembayaran"] == "Lunas":
                print("Mobil ini sudah lunas.")
                return

            print("\n1. Tandai Lunas")
            print("2. Batal")

            pilih = input("Pilih: ").strip()

            if pilih == "1":
                data["pembayaran"] = "Lunas"
                print("Pembayaran berhasil dikonfirmasi.")
            else:
                print("Pembayaran dibatalkan.")

            return

    print("Plat mobil tidak ditemukan.")

#main program 
def main():
    dataList = bacaData(namaFile)
    history = []
    
    while True:
        print("MENU CAR WASH HDC")
        print("1. Tambah Antrian")
        print("2. Tampilkan Antrian")
        print("3. Proses Antrian")
        print("4. Hapus Antrian")
        print("5. Lihat Riwayat")
        print("6. Pembayaran")
        print("7. Simpan ke File")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tambahAntrian(dataList)
        elif pilihan == "2":
            tampilkanAntrian(dataList)
        elif pilihan == "3":
            prosesAntrian(dataList, history)
        elif pilihan == "4":
            hapusAntrian(dataList)
        elif pilihan == "5":
            tampilkanHistory(history)
        elif pilihan == "6":
            pembayaranMobil(history)
        elif pilihan == "7":
            simpanData(namaFile, dataList)
            print("Data disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
