#if condition:
  # Kode program yang dijalankan jika condition bernilai True
  # Kode program yang dijalankan jika condition bernilai True
  
#Contoh Kode Program Percabangan If Bahasa Python
x = 20
y = 10
 
if x > y:
  print('Variabel x lebih besar dari variabel y')
  
#Dalam bahasa Python, karakter spasi di awal baris 5 wajib ditulis, karena inilah penanda blok if.
#Jika baris ini tidak 'dijorokkan' satu atau beberapa spasi, maka akan terjadi error
  
#Jika kita ingin menambah perintah lain di blok if yang sama, tulis baris baru dengan awalan spasi yang sama:
x = 20
z = 10
 
if x > z:
  print('Variabel x lebih besar dari variabel z')
  print('Sedang belajar bahasa gen Alpha')
  
#Jika kondisi if ini tidak terpenuhi, maka blok kode program tidak akan di eksekusi. Berikut contohnya:
x = 8
z = 10
 
if x > z:
  print('Variabel x lebih besar dari variabel z')
  print('Sedang belajar bahasa gen Alpha')
  
#Kode program ini tidak akan menampilkan hasil apa-apa, karena variabel a saya isi dengan angka 8
#Sehingga kondisi if a > b menghasilkan nilai False.

#Namun akan berbeda jika ditulis seperti ini:
x = 8
z = 10
 
if x > z:
  print('Variabel x lebih besar dari variabel z')
print('Sedang belajar bahasa gen Alpha')

#Kali ini perintah di baris 6 sudah tidak berada di dalam blok if (perhatikan perbedaan spasi di awal).
#Artinya, apapun hasil kondisi if, perintah di baris 6 akan selalu di jalankan.

#Bagaimana dengan membuat beberapa kondisi if? tidak ada masalah. Berikut contoh kode programnya:
x = 12
y = 12
 
if x > y:
  print('Variabel x lebih besar dari variabel y')
if x < y:
  print('Variabel x lebih kecil dari variabel y')
if x == y:
  print('Variabel x sama dengan variabel y')
  
#Contoh terakhir, mari buat kode program yang bisa menebak apakah angka yang diinput merupakan bilangan genap atau bilangan ganjil:
z = 7
 
if (z % 2) == 0:
  print('Variabel z berisi angka genap')
if (z % 2) != 0:
  print('Variabel z berisi angka ganjil')