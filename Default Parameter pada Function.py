#Berikut contoh kode programnya:
def tambah(var1, var2):
  return var1 + var2
 
print(tambah(1,2))
print(tambah(5,4))

#Dengan default parameter, kita bisa memanggil fungsi tambah() hanya dengan 1 inputan angka, atau bahkan tidak perlu sama sekali.
#Berikut perubahannya:
def tambah(var1 = 5, var2 = 2):
  return var1 + var2
 
print( tambah() )
print( tambah(1) )
print( tambah(1,2) )
print( tambah(5,4) )

#Penempatan Default Parameter
#Sebuah fungsi bisa memiliki banyak default parameter
#namun tidak boleh ada parameter tanpa nilai default yang ditulis setelah parameter dengan nilai default
#Error terjadi karena parameter pertama sudah memiliki nilai default
#sehingga parameter kedua, ketiga, dst juga harus memiliki nilai default.

#Membuat Fungsi Pemangkatan
#berikut kode program lengkap dari pembuatan function pangkat():
def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(3) )      # 9
print( pangkat(5) )      # 25
print( pangkat(10) )     # 100
print( pangkat(3,3) )    # 27
print( pangkat(5,4) )    # 625
print( pangkat(6,6) )    # 46656