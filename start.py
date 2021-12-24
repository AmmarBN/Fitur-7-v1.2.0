import os,sys,time,requests
os.system("clear")
print ("Kamu Belum Login Login Terlebih Dahulu")
print ("Agar Data Kamu Masuk Ke Database \033[1;93mJumlah Database : \033[1;95m 425 \033[1;90mOrang")
print ("\033[1;92m_    ____ ____ _ _  _ ")
print ("|    |  | | __ | |\ | ")
print ("|___ |__| |__] | | \| ")

x = "LordAmmar"
y = "subscribe"
def login():
          user = raw_input("Masukkan Creator Name : ")
          pasw = raw_input("Masukkan Password : ")
          nama = raw_input("Masukkan Nomor HP Kamu : ")
          if user ==x and pasw ==y:
              print ("Sukses Login Ke Database")
              time.sleep(2)
              os.system("python2 menu.py")
          else:
              print ("Acces danied/Gagal")
              time.sleep(2)
              os.system("python2 start.py")
if __name__ == "__main__":
       login()
