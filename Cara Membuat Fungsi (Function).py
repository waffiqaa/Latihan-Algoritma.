#Cara Membuat Fungsi dalam Bahasa Python
#Berikut format dasar cara pendefinisian fungsi dalam bahasa Python:
#def nama_function():
  # Isi function disini...
  # Isi function disini...
  #return nilai
  
#Contoh Kode Program Fungsi Bahasa Python
def sapa_duniailkom():
  print("Halo Duniailkom")
 
sapa_duniailkom()
sapa_duniailkom()
sapa_duniailkom()

#Sebuah kode program bisa saja memiliki banyak fungsi. Berikut contohnya:
def sapa_lisa():
  print("Hai Lisa");
 
def sapa_rosie():
  print("Morning, Rosie");
 
def sapa_jisoo():
  print("Halo girls,..");
 
sapa_lisa()
sapa_rosie()
sapa_jisoo()

#Variabel di Dalam Function
def hitung_luas_segitiga():
  alas = 5
  tinggi = 7
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
   
hitung_luas_segitiga()