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

                nama, status = baris.split(",")

                dataList.append({
                    "nama": nama,
                    "status": status
                })

    except FileNotFoundError:
        pass
        
    return dataList

#save antrian baru
def simpanData(namaFile, dataList):
    with open(namaFile, "w") as file:
        for data in dataList:
            file.write(f"{data['nama']},{data['status']}\n")

#baca antrian
def tampilkanAntrian(dataList):
    if len(dataList) == 0:
        print("Antrian kosong.")
        return

    print("DAFTAR ANTRIAN")
    for i, data in enumerate(dataList, start=1):
        print(f"{i}. {data['nama']} - {data['status']}")

#add antrian
def tambahAntrian(dataList):
    nama = input("Masukkan nama: ").strip()

    if nama == "":
        print("Nama tidak boleh kosong.")
        return

    dataList.append({
        "nama": nama,
        "status": "Menunggu"
    })

    print("Berhasil ditambahkan.")

    data = dataList[0]

    print(f"\nMemproses: {data['nama']}")
    print("1. Sedang Dicuci")
    print("2. Selesai")

    pilihan = input("Pilih status: ").strip()

    if pilihan == "1":
        data["status"] = "Sedang Dicuci"

    elif pilihan == "2":
        data["status"] = "Selesai"

        history.append(data)

        dataList.pop(0)

        print("Mobil selesai & masuk riwayat.")

    else:
        print("Pilihan tidak valid.")

def updateStatus(dataList, history):
    if len(dataList) == 0:
        print("Antrian kosong.")
        return

#update status antrian
def updateStatus(dataList, history):
    nama = input("Masukkan nama: ").strip()

    for data in dataList:
        if data["nama"] == nama:

            print("1. Sedang Dicuci")
            print("2. Selesai")

            pilihan = input("Pilih status: ").strip()


#delete antrian
def hapusAntrian(dataList):
    nama = input("Masukkan nama: ").strip()

    for data in dataList:
        if data["nama"] == nama:
            dataList.remove(data)
            print("Data berhasil dihapus.")
            return

    print("Data tidak ditemukan.")

#main program 
def main():
    dataList = bacaData(namaFile)
    history = []
      while True:
        print("\n=== MENU CAR WASH ===")
        print("1. Tambah Antrian")
        print("2. Tampilkan Antrian")
        print("3. Proses Antrian (Queue)")
        print("4. Hapus Antrian")
        print("5. Lihat Riwayat (Stack)")
        print("6. Simpan ke File")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tambahAntrian(dataList)
        elif pilihan == "2":
            tampilkanAntrian(dataList)
        elif pilihan == "3":
            updateStatus(dataList, history)
        elif pilihan == "4":
            hapusAntrian(dataList)
        elif pilihan == "5":
            tampilkanHistory(history)
        elif pilihan == "6":
            simpanData(namaFile, dataList)
            print("Data disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
