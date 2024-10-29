#Cara Pembuatan Tipe Data Tuple Python
#Untuk membuat tipe data Tuple, gunakan tanda kurung biasa, kemudian setiap anggota list dipisah dengan tanda koma.
x = ("Yuk", "Coding", "Biar", "Rizz")
y = (7, 8, 9, 10)
z = ("Coding", 9, 9.99, True)
  
print(x)
print(y)
print(z)

#Tipe data Tuple juga bisa dibuat menggunakan tanda kurung bulat, bukan tanda kurung siku sebagaimana List. berikut contohnya:
z = ["Yuk", "Coding", "Biar", "Rizz"]
print(type(z))
z = ("yuk", "coding", "biar", "rizz")
print(type(z))

#Cara Mengakses Tipe Data Tuple Python
#Cara mengakses tipe data Tuple tidak berbeda dengan tipe data List, dimana kita menulis nomor urut index dalam tanda kurung siku:
x = ("Coding", 9, 9.99, True, 'Rizz', 2j)
  
print(x[0])
print(x[1])
print(x[2])
print(x[2:5])
print(x[:3])
print(x[3:])
print(x[:])