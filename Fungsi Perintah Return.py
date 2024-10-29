#Perintah Return di dalam Function
#Berikut contohnya:
def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
    
hitung_luas_segitiga(5, 7)

#modifikasi dari function hitung_luas_segitiga() dengan penambahan perintah return:
def hitung_luas_segitiga(alas, tinggi):
  luas = (alas * tinggi) / 2
  return luas
    
var1 = hitung_luas_segitiga(5, 7)
print("Luas segitiga adalah:",var1)

#Mengembalikan Langsung Hasil Operasi
def hitung_luas_segitiga(alas, tinggi):
  return (alas * tinggi) / 2
    
print("Luas segitiga adalah:", hitung_luas_segitiga(5, 7))

#Perintah Return Akan Menghentikan Function
def hitung_luas_segitiga(alas, tinggi):
  return (alas * tinggi) / 2
  print ("Belajar Python di Duniailkom")
    
print("Luas segitiga adalah:", hitung_luas_segitiga(5, 7))

#Contoh Lain Perintah Return Python
def harga_setelah_pajak(harga_dasar):
  return harga_dasar + (harga_dasar * 10/100)
 
harga_seblak = 5000
harga_final_seblak = harga_setelah_pajak(harga_seblak)
print("Harga seblak 1 porsi Rp.", harga_final_seblak)