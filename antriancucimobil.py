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

                plat, status, pembayaran = baris.split(",")

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
    plat = input("Masukkan nomor plat kendaraan: ").strip()

    if plat == "":
        print("Nomor plat tidak boleh kosong.")
        return
        
    print("\nStatus Pembayaran")
    print("1. Lunas")
    print("2. Belum Lunas")

    pilih = input("Pilih: ").strip()

    if pilih == "1":
        pembayaran = "Lunas"
    elif pilih == "2":
        pembayaran = "Belum Lunas"
    else:
        print("Pilihan tidak valid.")
        return

    dataList.append({
        "plat": plat,
        "status": "Menunggu",
        "pembayaran": pembayaran
    })

    print("\n✓ Antrian berhasil ditambahkan.")

#baca/read antrian
def tampilkanAntrian(dataList):
    if len(dataList) == 0:
        print("Antrian kosong.")
        return

    print("\n" + "="*60)
    print("                 DAFTAR ANTRIAN")
    print("="*60)
    print(f"{'No':<5}{'Plat':<15}{'Status':<20}{'Pembayaran'}")
    print("-"*60)

    for i, data in enumerate(dataList, start=1):
        print(
            f"{i:<5}"
            f"{data['plat']:<15}"
            f"{data['status']:<20}"
            f"{data['pembayaran']}"
        )

    print("="*60)


#update status antrian
def prosesAntrian(dataList, history):
    if len(dataList) == 0:
        print("Tidak ada antrian.")
        return

    # ambil antrian paling depan (QUEUE)
    data = dataList[0]

    print("\n" + "="*40)
    print(f"Sedang Memproses : {data['plat']}")
    print("="*40)
    print("1. Sedang Dicuci")
    print("2. Selesai")

    pilihan = input("Pilih status: ").strip()

    if pilihan == "1":
        data["status"] = "Sedang Dicuci"

    elif pilihan == "2":
        data["status"] = "Selesai"

        history.append(data)   # stack (riwayat)
        dataList.pop(0)        # queue (fifo)

        print("\n✓ Mobil selesai dicuci dan masuk ke riwayat.")

    else:
        print("Pilihan tidak valid.")

#delete antrian
def hapusAntrian(dataList):
    plat = input("Masukkan plat: ").strip().upper()

    for data in dataList:
        if data["plat"].upper() == plat:
            dataList.remove(data)
            print("\n✓ Data kendaraan berhasil dihapus.")
            return

    print("\n✗ Plat tidak ditemukan.")

#show history dgn stack
def tampilkanHistory(history):
    if len(history) == 0:
        print("Belum ada riwayat.")
        return

    print("\n" + "="*35)
    print("      RIWAYAT CAR WASH")
    print("="*35)

    # LIFO
    for i, data in enumerate(reversed(history), start=1):
        print(f"{i}. {data['plat']}")

#search
def cariPlat(dataList):
    platCari = input("Masukkan plat yang dicari: ").strip().upper()

    for data in dataList:
        if data["plat"].upper() == platCari:
            print("\n" + "="*35)
            print("      DATA KENDARAAN")
            print("="*35)
            print(f"Plat        : {data['plat']}")
            print(f"Status      : {data['status']}")
            print(f"Pembayaran  : {data['pembayaran']}")
            print("="*35)
            return

    print("Plat tidak ditemukan.")
    
#main program
def main():
    dataList = bacaData(namaFile)
    history = []
    
    while True:
        print("\n" + "="*40)
        print("           CAR WASH HDC")
        print("="*40)
        print("1. Tambah Antrian")
        print("2. Tampilkan Antrian")
        print("3. Proses Antrian")
        print("4. Hapus Antrian")
        print("5. Cari Plat")
        print("6. Lihat Riwayat")
        print("7. Simpan ke File")
        print("0. Keluar")
        print("="*40)

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
            cariPlat(dataList)
        elif pilihan == "6":
            tampilkanHistory(history)
        elif pilihan == "7":
            simpanData(namaFile, dataList)
            print("Data disimpan.")
        elif pilihan == "0":
            simpanData(namaFile, dataList)
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
