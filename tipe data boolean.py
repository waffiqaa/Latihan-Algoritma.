#Cara Penggunaan Tipe Data Boolean Python
x = True
y = False
  
print(x)
print(y)

#Boolean sering muncul dari operasi perbandingan, misalnya membandingkan apakah satu nilai lebih besar, lebih kecil, atau sama dengan nilai lain.
#Hasil perbandingan ini akan menjadi True atau False. Contoh:
x = 28 < 20
print(x)
y = 28 > 20
print(y)
z = "J" == "j"
print(z)

#Hasil boolean dari operasi perbandingan ini juga bisa didapat tanpa harus menyimpannya ke dalam variabel, seperti contoh berikut:
print(28 < 20)
print(28 > 20)
print("J" == "j")

#Operasi perbandingan dapat langsung diinput ke dalam perintah print.
#Hasil dari perbandingan ini sering digunakan dalam struktur logika IF. Contohnya:
x = 28
y = 20
if (x < y):
  print("Isi variabel x lebih kecil daripada variabel y")
elif (x > y):
  print("Isi variabel x lebih besar daripada variabel y")
else:
  print("Isi variabel x sama dengan variabel y")