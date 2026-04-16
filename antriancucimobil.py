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

