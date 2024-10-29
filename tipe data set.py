#Cara Pembuatan Tipe Data Set Python
#menggunakan tanda kurung kurawal, kemudian setiap anggota set dipisah dengan tanda koma
x = {"Selamat", "menunaikan", "ibadah", "Puasa"}
y = {10, 20, 30, 40}
z = {"Puasa", 31, 23.59, True}
 
print(x)
print(y)
print(z)

#Menggunakan function type(), kita bisa melihat perbedaan cara penulisan tipe data list, tuple dan set dalam bahasa Python
y = ["Selamat", "menunaikan", "ibadah", "Puasa"]
print(type(y))
 
j = ("Selamat", "menunaikan", "ibadah", "Puasa")
print(type(j))
 
k = {"Selamat", "menunaikan", "ibadah", "Puasa"}
print(type(k))

#Sifat Tipe Data Set Python
j = {"Bintang", "Sigma", "Skibidi", "Rizz", "Aura"}
k = {100, 200, 300, 400, 200, 300}
 
print(j)
print(k)

#Operasi Himpunan tipe data Set Python
#tipe data khusus yang dipakai untuk operasi himpunan, seperti operasi gabungan (union), operasi irisan (intersection), dst
#berikut contoh penggunaan tipe data set untuk operasi himpunan:
y = {1, 2, 3, 4, 6}
x = {3, 4, 5, 6, 8}
 
print (y | x) # union
print (y & x) # intersection