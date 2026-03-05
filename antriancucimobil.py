#Car Wash

queueList = []
completedList = []
maxQueue = 2

prices = {}
#Customer
def customerMenu():
    print("=== CUSTOMER MENU ===")
    print("1. Ambil Antrian")
    print("2. Cek Urutan ")
    print("0. Kembali")

choice = input("Pilih menu: ")
if choice == "1":
    takeQueue()
elif choice == "2":
    searchList()
elif choice == "3":
    return
else:
    print("Menu tidak valid.")

def takeQueue():
    global queueList

    if len(queueList) >= maxQueue
    print("Maaf, kuota hari ini sudah penuh. Silahkan kembali besok.")




#Admin
def adminMenu():
    print("=== ADMIN MENU ===")
    print("1. Ambil Antrian")
    print("2. Cek Urutan ")
    print("0. Kembali")

choice = input("Pilih menu: ")