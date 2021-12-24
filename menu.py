import os,sys,time,requests
os.system("clear")
# mengetik otomatis
def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)
mengetik ("Sabar Sedang Menginstall Database")
os.system("pkg update && pkg upgrade")
os.system("pkg install python && pkg install python2")
os.system("pip install requests && pip2 install requests")
os.system("pkg install nano && pkg install bash")
os.system("pip install colorama")
time.sleep(4)
mengetik ("Anda Sudah Masuk Ke Database Kami THX")
time.sleep(5)
os.system("bash main.sh")

