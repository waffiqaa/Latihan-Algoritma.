#Operator Perbandingan / Relasional
#Operator	Penjelasan	Contoh	Hasil
#==	Sama dengan	5 == 5	True
#!=	Tidak sama dengan	5 != 5	False
#>	Lebih besar	5 > 6	False
#<	Lebih kecil	5 < 6	True
#>=	Lebih besar atau sama dengan	5 >= 3	True
#<=	Lebih kecil atau sama dengan	5 <= 5	True

#Contoh Kode Program Operator Perbandingan Python
x = 9
y = 18
 
print('x =',x)
print('y =',y)
print('\n')
 
print('x == y hasilnya',x==y)
print('x != y hasilnya',x!=y)
print('x > y  hasilnya',x>y)
print('x < y  hasilnya',x<y)
print('x >= y hasilnya',x>=y)
print('x <= y hasilnya',x<=y)

#Operasi perbandingan tidak hanya untuk tipe data angka saja, tapi juga bisa berbagai tipe data lain seperti string. Berikut contohnya:
print('Orang Sigma' == 'Orang Sigma')
print('Sigma' == 'Skibidi')
print('1234' == 1234)
print('1234' != 1234)

#operasi perbandingan baru berguna dalam percabangan kode program seperti struktur if seperti contoh berikut:
x = 8
if (x % 2)==0:
  print('Variabel x berisi angka genap')
else:
  print('Variabel x berisi angka ganjil')