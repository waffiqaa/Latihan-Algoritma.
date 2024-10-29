#Cara Pembuatan Tipe Data Dictionary Python
#Dalam pembuatan dictionary, kita menggunakan tanda kurung kurawal { dan }
#Selain itu setiap element merupakan pasangan dari key dan value
#Antar satu element dengan element lain dipisah dengan tanda koma 
x = { 1: "Berinovasi", 2: "Kreativitas", 3: "di Kehidupan sehari-hari" }
y = { "mengapa": "Berinovasi", "apa": "kreativitas", "dimana": "di kehidupan sehari-hari" }
z = { 1: "Berinovasi", "apa": "kreativitas", "dimana": "di kehidupan sehari-hari" }
 
print(type(x))
print(type(y))
print(type(z))
 
print(x)
print(y)
print(z)

#Nilai atau value dari setiap element dictionary bisa terdiri dari berbagai tipe data
z = { 1: "Mahasiswa", 
        2: ["Pascal", "C", "Python"],
        "website": "Duniailkom",
        "menyerah" : False,
        "target": 2028,
        "riwayat_sekolah": {
          "SD": "SDN 1 Sigma",
          "SMP": "SMP 1 Rizz",
          "SMA": "SMA 1 Delulu"}
      }
       
print(z)

#Cara Mengakses Element Dictionary Python
y = { "kegiatan": "Bermain game",
        "website": "Robloxcom",
        "hasil": "Plus Seribu Aura!" }
 
print(y["website"])

#Cara Mengubah Element Dictionary Python
x = { "kegiatan": "Bermain game",
        "website": "Robloxcom",
        "hasil": "Plus Seribu Aura!" }
 
x["kegiatan"] = "Nonton Live Windah Basudara"
print(x)

#Cara Menambah Element Dictionary Python
z = { "kegiatan": "Bermain game",
        "website": "Robloxcom",
        "hasil": "Plus Seribu Aura!" }
 
z["target"] = 2024
print(z)

#Cara Menghapus Element Dictionary Python
y = { "kegiatan": "Belajar Mewing",
        "website": "Robloxcom",
        "hasil": "Plus Seribu Aura!" }
 
del y["kegiatan"]
print(y)

#Pembuatan Dictionary dengan constructor dict()
x = dict ( kegiatan = "Belajar Mewing",
             website = "Robloxcom",
             hasil = "Plus Seribu Aura!" )
              
print(x)