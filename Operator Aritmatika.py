#Tabel berikut merangkum 7 operator aritmatika dalam bahasa pemrograman Python:
#Tabel berikut merangkum 7 operator aritmatika dalam bahasa pemrograman Python:
# Operator	Penjelasan	Contoh
#+	Penambahan	20 + 6, hasil: 26
#–	Pengurangan	20 – 6, hasil: 14
#*	Perkalian	20 * 6, hasil: 120
#/	Pembagian (real/pecahan)	20 / 6, hasil: 3.3333
#//	Pembagian (dibulatkan ke bawah)	20 // 6, hasil: 3
#%	Modulus (sisa hasil bagi)	20 % 6, hasil: 2
#**	Pemangkatan	20 ** 6, hasil: 64000000

#Dan berikut 2 jenis operator aritmatika unary (hanya butuh 1 operand):
#Operator	Penjelasan	Contoh
#+	Positif (plus)	+5
#–	Negatif (min)	-3

#Contoh Kode Program Operator Aritmatika Python
x = 20
y = 6
 
print('x + y =',x+y)
print('x - y =',x-y)
print('x * y =',x*y)
print('x / y =',x/y)
print('x // y =',x//y)
print('x % y =',x%y)
print('x ** y =',x**y)

#Prioritas Operator Aritmatika Python
#Berikut contohnya:
x = 12 + 6 * 4 - 8
print(x)

#Untuk mem-prioritaskan sebuah operasi, bisa ditambahkan tanda kurung, seperti contoh berikut:
y = (12 + 6) * (4 - 8);
print(y)