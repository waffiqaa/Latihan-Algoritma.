#Operator Logika
#Operator	Penjelasan	Contoh	Hasil
#and	True jika kedua operand bernilai True	True and True	True
#or	True jika salah satu operand bernilai True	True or False	True
#not	True jika operand bernilai False	not False	True

#Contoh Kode Program Operator Logika Python
print('Hasil dari True and True   :', True and True)
print('Hasil dari True and False  :', True and False)
print('Hasil dari False and True  :', False and True)
print('Hasil dari False and False :', False and False)
 
print('\n')
 
print('Hasil dari True or True   :', True or True)
print('Hasil dari True or False  :', True or False)
print('Hasil dari False or True  :', False or True)
print('Hasil dari False or False :', False or False)
 
print('\n')
 
print('Hasil dari not True  :', not True)
print('Hasil dari not False :', not False)

#kita juga bisa menggabungkan lebih dari satu operasi seperti contoh berikut:
x = (5 > 6) and (10 <= 8)
print(x)
 
y = ('hello word' == 'hello word') or (10 <= 8)
print(y)
 
z = not (10 < 10)
print(z)
 
w = ('duniailkom' == 'duniailkom') and (10 <= 8) or (1 != 1)
print(w)