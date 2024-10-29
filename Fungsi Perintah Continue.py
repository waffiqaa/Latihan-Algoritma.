#Berikut format dasar penggunaan perintah continue dalam perulangan for Python:
#for i in range(1,x): 
  #if condition2: 
    #continue
  # kode program yang akan diulang 
  # kode program yang akan diulang
  
#Contoh Kode Program Perintah Continue Bahasa Python
for i in range(1,11):
  print(i,' x ',i ,' = ',i*i)
  
#sekarang tambah dengan perintah continue:
for i in range(1,11):
  if i == 5:
    continue
  print(i,' x ',i ,' = ',i*i)
  
#Sebagai tambahan, berikut contoh kode program perintah continue dalam perulangan while:
i = 0
while i < 10:
  i += 1
  if i == 5:
    continue
  print(i,' x ',i ,' = ',i*i)
  
#Jadi, kata kuncinya adalah: perhatikan logika program terutama ketika membuat perulangan while yang melibatkan perintah continue.