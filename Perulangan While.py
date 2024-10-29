#Berikut format dasar struktur perulangan while dalam bahasa Python:
#start;
#while condition:
  # kode program yang akan diulang
  # kode program yang akan diulang
  #increment

#Contoh Kode Program Perulangan While Bahasa Python:
i = 1
while i <= 5:
  print('Orang Sigma')
  i += 1
  
#Perintah merupakan penulisan singkat dari i = i + 1, yang berfungsi untuk menaikkan nilai variabel i sebanyak 1 angka dalam setiap perulangan.
#Perulangan while di atas akan di ulang sebanyak 5 kali, mulai dari i = 1, i = 2, i = 3, i = 4, hingga i = 5.
#Ketika nilai variabel counter i sudah mencapai 6, maka kondisi while i <= 5 tidak terpenuhi lagi (False), sehingga perulangan berhenti.
#Jika tidak, kondisi akhir tidak akan pernah terpenuhi dan perulangan akan berjalan terus menerus. Ini dikenal dengan istilah infinity loop.
#Untuk menghentikan infinity loop, tekan kombinasi CTRL + C. dari dalam jendela hasil.
#Atau bisa juga dengan tutup paksa aplikasi IDLE Python

#Di dalam Python, kita juga harus hati-hati dengan penggunaan spasi, karena itu adalah penanda blok perulangan.
#Di dalam blok perulangan, kita juga bisa mengakses nilai dari variabel counter i:
i = 1
while i <= 5:
  print('Duniailkom', i)
  i += 1
  
#Bagaimana dengan perulangan menurun? tidak masalah.
#Kita tinggal mengatur kondisi awal, kondisi akhir, serta proses decrement:
i = 10
while i > 5:
  print('Duniailkom', i)
  i -= 1
  
#kode program perulangan While untuk membuat deret kelipatan 3 dari 3 sampai dengan 99
#Kuncinya ada di kondisi perulangan serta proses increment:
i = 3
while i < 100:
  print(i)
  i = i + 3