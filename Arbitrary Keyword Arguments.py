#Arbitrary keyword arguments (**kwargs), argumen fungsi tersebut ditulis dalam bentuk pasangan nama dan value.
#Sesampainya di dalam fungsi, parameter kwargs akan berbentuk tipe data dictionary.
#contoh kode program berikut:
def sambung_kata(**kwargs):
  print(kwargs)
  print(type(kwargs))
 
sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom")

#Menampilkan Nilai **kwargs Fungsi Python
def sambung_kata(**kata):
  for i in kata:
     print(i)
 
sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom")

#jika ingin menampilkan value dictionary dalam sebuah perulangan for, bisa menggunakan kode berikut:
def sambung_kata(**kata):
  for i in kata.values():
     print(i)
 
sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom")

#berikut modifikasi kode programnya:
def sambung_kata(**kata):
  hasil = ""
  for i in kata.values():
     hasil += i
  return hasil;
 
print( sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom") )

#tambah satu karakter spasi di dalam perulangan for:
def sambung_kata(**kata):
  hasil = ""
  for i in kata.values():
     hasil += i + " "
  return hasil;
 
print( sambung_kata(a="Belajar", b="Python", c="di", d="Duniailkom") )

#Dengan perintah hasil += i + " " di baris 4, maka setiap proses penyambungan kata akan ditambah satu spasi pemisah.

#Menggabung Argument Biasa + *args + kwargs
#Jika sebuah fungsi punya ketiga jenis argument ini, maka urutannya harus sebagai berikut:
#1.Argument / parameter biasa
#2.Arbitrary arguments (*args)
#3.Arbitrary keyword arguments (**kwargs)
#Berikut contoh kode program yang menggabung ketiganya:
def test(var1, var2, *args,**kwargs):
  print(var1)
  print(var2)
  print(args)
  print(kwargs)
 
test(10, 20, 30, 40, 50, a = 60, b = 70, c = 80)

#Disini saya membuat fungsi test() yang menampung 4 buah parameter, yakni var1, var2, *args, dan **kwargs.
#Urutan penulisan harus seperti ini
#Jika ada yang tidak sesuai, Python akan menampilkan pesan error
