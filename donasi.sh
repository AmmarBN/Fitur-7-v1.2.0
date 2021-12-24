#!bin/bash/sh
echo '
      [Menu]
[1], Pulsa
[2], Saweria
[3], Nomor Bot
[4], exit
[5], Kembali/Back
'
echo
read -p "Mau Donasi Lewat Apa Ngap? " donate
if [[ $donate == 1 ]]; then
echo '╭─「 Donasi • Pulsa Buat Author 」
│ • AmmarBN [087708773367]
│ • Agung [082136981440]
│ • Syahrul [0882184728291]
│ • Gilang [081376746950]
╰────
Itu Adalah Author Bot Whatsapp Lord_Botz...
Untuk Creator SC Ini Adalah AmmarBN Silakan
Bisa Pilih Donasi Dari Salah Satu Nomor'
fi

if [[ $donate == 2 ]]; then
echo '╭─「 Donasi • Non Pulsa 」
│ • https://trakteer.id/NFXL
│ • https://saweria.co/NFXL
╰────
Dukung Author Nurutomo Yang Telah
Membuat Script Lord_Botz/Original Script
Dukung Nurutomo Lewat Saweria'
fi

if [[ $donate == 3 ]]; then
     python bot.py
fi

if [[ $donate == "" ]]; then
echo "Input Salah!!"
sleep 1
echo "Input Yang Benar Kaka"
     bash donasi.sh
fi

if [[ $donate == 4 ]]; then
exit
fi

if [[ $donate == 5 ]]; then
     bash main.sh
fi
