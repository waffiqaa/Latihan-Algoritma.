#Cara Pembuatan Tipe Data List Python
#Untuk membuat tipe data List, gunakan tanda kurung siku, kemudian setiap anggota list dipisah dengan tanda koma:
x = ["Yuk", "Coding", "Biar", "Rizz"]
y = [209, 237, 289, 416]
z = ["Coding", 209, 9.99, True]
  
print(x)
print(y)
print(z)

#Perintah print bisa dipakai untuk menampilkan semua isi List secara langsung
#Dengan menggunakan function type(), kita bisa memastikan bahwa ini adalah tipe data list Python:
x = ["Yuk", "Coding", "Biar", "Rizz"]
y = [209, 237, 289, 416]
z = ["Coding", 209, 9.99, True]
 
print(type(x))
print(type(y))
print(type(z))

#Cara Mengakses Tipe Data List Python
x = ["Coding", 209, 9.99, True, 'Rizz', 2j]
  
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])

#Cara Mengganti Nilai Tipe Data List Python
x = ["Coding", 209, 9.99, True, 'Rizz', 2j]
print(x)
  
x[0] = 'Belajar'
x[3] = False
print(x)

#Menampilkan Sebagian Anggota List
#Python menyediakan cara untuk menampilkan beberapa anggota List sekaligus. Berikut prakteknya:
x = ["Coding", 209, 9.99, True, 'Rizz', 2j]
print(x[2:5])
print(x[:3])
print(x[3:])
print(x[:])