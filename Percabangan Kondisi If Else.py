#if condition: 
  # Kode program yang dijalankan jika condition bernilai True 
  # Kode program yang dijalankan jika condition bernilai True
#else:
  # Kode program yang dijalankan jika condition bernilai False
  # Kode program yang dijalankan jika condition bernilai False
  
#Contoh Kode Program Percabangan If Else Bahasa Python
x = 7
 
if (x % 2) == 0:
  print('Variabel x berisi angka genap')
if (x % 2) != 0:
  print('Variabel x berisi angka ganjil')
  
#Alur ini sebenarnya akan lebih sederhana (dan lebih efisien) jika kita ubah ke dalam struktur If Else.
#Dengan demikian kode programnya bisa saya tulis ulang sebagai berikut:
x = 7
 
if (x % 2) == 0:
  print('Variabel x berisi angka genap')
else:
  print('Variabel x berisi angka ganjil')
  
#Berikut contoh lain dari struktur kondisi If Else:
nilai = 65
 
if nilai >= 75:
  print('Selamat, anda lulus')
else:
  print('Maaf, silahkan coba lagi tahun depan')