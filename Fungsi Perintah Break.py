#Berikut format dasar penggunaan perintah break dalam perulangan while:
#start;
#while condition1:
  # kode program yang akan diulang
  # kode program yang akan diulang
  #if condition2:
    #break
  #increment
  
#Contoh Kode Program Perintah break Python
i = 1
while i <= 10:
  print(i,' x ',i ,' = ',i*i)
  i += 1
  
#jika variabel counter i sudah mencapai angka 5, maka hentikan perulangan (break). Berikut kode programnya:
i = 1
while i <= 10:
  print(i,' x ',i ,' = ',i*i)
  if i == 5:
    break
  i += 1
  
#Sebagai tambahan, posisi pemeriksaan kondisi ini bisa berpengaruh kepada tampilan akhir. Perhatikan kode program berikut:
i = 1
while i <= 10:
  if i == 5:
    break
  print(i,' x ',i ,' = ',i*i)
  i += 1
  
#Sebagai penutup, berikut contoh penggunaan perintah break pada perulangan for Python:
for i in range(1,11):
  print(i,' x ',i ,' = ',i*i)
  if i == 5:
    break 