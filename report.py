import os,sys,time,requests
# mengetik otomatis
def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)

mengetik ("Masukkan Laporan Anda!!")
report = raw_input("Apa Masalahnya? : ")
mengetik ("Mengirim Link Untuk Memberikan Report")
mengetik ("Ke Author Harap Sabar Bossq")
time.sleep(5)
os.system("xdg-open https://wa.me/6287708773367?text=*[❗]Report* Laporan:<laporan> ")
mengetik ("Done Report!")
time.sleep(5)
