#Berikut format dasar fungsi Python dengan parameter dan argumen:
#def nama_function(param1, param2):
  # Isi function disini...
  # Isi function disini...
  #return
   
#nama_function(arg1, arg2)

#Contoh Kode Program Parameter dan Argumen Fungsi
def sapa_jaehyuk():
  print("Hai jaehyuk");
 
sapa_jaehyuk()

#Akan lebih fleksibel
#modifikasi fungsi sapa_nama() agar bisa menampung sebuah parameter dan argumen:
def sapa_teman(nama):
  print("Hai",nama);
 
sapa_teman("jaehyuk")

#Kita bisa menjalankan fungsi sapa_teman() dengan argumen yang berbeda-beda:
def sapa_teman(nama):
  print("Hai",nama);
 
sapa_teman("jaehyuk")
sapa_teman("jeongwoo")
sapa_teman("jihoon")

#Membuat Fungsi dengan Lebih dari 1 Parameter/Argumen
def sapa_teman(nama1, nama2, nama3):
  print("Hai", nama1, nama2, nama3);
 
sapa_teman("hoshi", "seungkwan", "DK")

#Membuat Function hitung_luas_segitiga()
def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
    
hitung_luas_segitiga(5, 7)
hitung_luas_segitiga(2, 10)
hitung_luas_segitiga(191, 357)