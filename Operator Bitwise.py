#Operator Bitwise
#Operator	Nama	Contoh	Biner	Hasil (biner)	Hasil (decimal)
#&	And	10 & 12	1010 & 1100	1000	8
#|	Or	10 | 12	1010 | 1100	1110	14
#^	Xor	10 ^ 12	1010 ^ 1100	0110	6
#~	Not	~ 10	~1010	0101	-11 (two complement)
#<<	Left shift	10 << 1	1010 << 1	10100	20
#>>	Right shift	10 >> 1	1010 >> 1	101	5

#Contoh Kode Program Operator Bitwise Python
x = 10
y = 12
 
print('x berisi angka',x ,'desimal atau',bin(x),'biner')
print('y berisi angka',y ,'desimal atau',bin(y),'biner')
 
print('\n')
 
print('x & y  :',x & y)
print('x | y  :',x | y)
print('x ^ y  :',x ^ y)
print('~x     :',~x)
print('x << 1 :',x << 1)
print('x >> 1 :',x >> 1)