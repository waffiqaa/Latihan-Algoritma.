#Berikut format dasar struktur perulangan for dalam bahasa Python:
#x = [a, b, ...] 
#for i in x:
  # kode program yang akan diulang
  # kode program yang akan diulang
  
#Contoh Kode Program Perulangan For Bahasa Python
warna = ['Merah','Biru','Kuning','Biru']
for z in warna:
  print(z)
  
#Perulangan for juga bisa dipakai untuk tipe data lain, misalnya tipe data set:
warna = {'Merah','Biru','Kuning','Biru'}
for z in warna:
  print(z)
  
#tipe data string juga bisa:
web = 'Robloxcom'
for huruf in web:
  print(huruf)
  
#Penggunaan Function range()
for y in range(5):
  print(y)
  
#Namun kita bisa mengatur jangkauan yang diinginkan.
#Caranya, tambah angka kedua ke dalam function range():
for y in range(5,10):
  print(y)
  
#Tidak hanya itu, kita juga bisa mengatur tingkat "kenaikan" atau increment dari range
#dengan cara menambah 1 lagi angka pada saat pemanggilan function range():
for z in range(3,100,3):
  print(z)