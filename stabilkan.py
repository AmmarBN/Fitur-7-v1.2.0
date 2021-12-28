import os,sys,time

def spin():
        try:
                L="/-\\|"
                for q in range(75):
                        time.sleep(0.1)
                        sys.stdout.write("\r \x1b[1;97m\x1b[1;91m#\x1b[1;97m \x1b[1;97mStarting [\x1b[1;92m"+L[q % len(L)]+"\x1b[1;97m]")
                        sys.stdout.flush()
        except:
                exit()

print ("Menstabilkan Jaringan")
spin()
print ("")
print ("\033[1;30m<------------[ \033[1;33m+ RUNNING \033[1;33m+ \033\033[1;30m]------------>")
os.system("ping -s1000 1.1.1.1")
