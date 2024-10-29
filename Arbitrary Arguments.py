#contoh, perhatikan fungsi berikut ini:
def sapa_teman(nama1, nama2, nama3):
  print("Halo",nama1)
  print("Halo",nama2)
  print("Halo",nama3)
   
sapa_teman("Mark","Jeno","Jisung")

#Dengan menggunakan teknik arbitrary arguments, kita bisa membuat sebuah fungsi untuk menerima 3, 4 atau 100 argumen sekaligus.
#Caranya, buat satu parameter dengan tanda bintang di awal seperti berikut:
def sapa_teman(*args):
  print(args)
  print(type(args))
   
sapa_teman("Mark","Jeno","Jisung","Jaehyun")

#Dengan penulisan seperti ini, parameter *args akan menampung semua argumen yang ditulis pada saat pemanggilan fungsi tersebut dan disimpan dalam sebuah tuple.
#Karena hasil akhirnya berbentuk tuple, maka kita bisa menggunakan perulangan untuk mengakses setiap element tuple.
#Berikut modifikasi dari kode program sebelumnya:
def sapa_teman(*nama):
  for i in nama:
    print("Halo",i)
   
sapa_teman("Mark","Jeno","Jisung","Haechan","Jaemin","Chenlee","Renjun")

#Contoh Kode Program *args Python
def jumlah(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil
   
print( jumlah(5,7) )
print( jumlah(5,7,3,2) )
print( jumlah(5,7,3,2,8,2,1,3) )
print( jumlah(100, 200, 300, 400, 500) )

#berikut kode program Python untuk mencari nilai rata-rata menggunakan arbitrary arguments:
def rata2(*args):
  hasil = 0
  for i in args:
    hasil += i
  return hasil / len(args)
   
print( rata2(5,7) )
print( rata2(5,7,3,2) )
print( rata2(5,7,3,2,8,2,1,3) )
print( rata2(100,200,300,400,500) )