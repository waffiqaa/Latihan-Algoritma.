#Operator Identitas
#Operator	Penjelasan
#is	Bernilai True jika kedua operand merujuk ke object yang sama dan berisi nilai yang sama
#is not	Bernilai True jika kedua operand merujuk ke object yang tidak sama

#Berikut contoh penggunaannya:
y = 5
j = 5
k = 6
print('y is j :', y is j)
print('y is k :', y is k)
print('y is not k :', y is not k)
print('\n')
  
i = 'Duniailkom'
j = 'Duniailkom'
print('i is j :', i is j)
print('i is not j :', i is not j)
print('\n');
  
x = ['a','b','c']
y = ['a','b','c']
print('x is y :', x is y)
print('x is not y :', x is not y)

#Operator Keanggotaan
#Operator	Penjelasan
#in	Bernilai True jika nilai yang dicari ada di dalam himpunan
#not in	Bernilai True jika nilai yang dicari tidak ada dalam himpunan

#Berikut contoh penggunaannya:
x = 'Duniailkom'
print('x :',x)
print('\'i\' in x     :', 'i' in x)
print('\'k\' not in x :', 'k' not in x)
print('\'d\' not in x :', 'd' not in x)
print('\n')
 
 
y = ['a','b','c']
print('y :',y)
print('\'a\' in y     :', 'a' in y)
print('\'a\' not in y :', 'a' not in y)
print('\'d\' not in y :', 'd' not in y)
print('\n')
 
z = (12,43,102,55)
print('z :',z)
print('102 in z     :', 102 in z)
print('102 not in z :', 102 not in z)
print('35 not in z  :', 35 in z)