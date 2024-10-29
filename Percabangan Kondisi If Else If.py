#if condition_1: 
  # Kode program yang dijalankan jika condition_1 bernilai True 
  # Kode program yang dijalankan jika condition_1 bernilai True
#elif condition_2: 
  # Kode program yang dijalankan jika condition_2 bernilai True 
  # Kode program yang dijalankan jika condition_2 bernilai True
#elif condition_3: 
  # Kode program yang dijalankan jika condition_3 bernilai True 
  # Kode program yang dijalankan jika condition_3 bernilai True
#else:
  # Kode program yang dijalankan jika semua kondisi tidak terpenuhi
  # Kode program yang dijalankan jika semua kondisi tidak terpenuhi
  
#Contoh Kode Program Percabangan If Else If Bahasa Python
nilai = 'D'
 
if nilai == 'A':
  print('Pertahankan')
elif nilai == 'B':
  print('Harus lebih baik lagi')
elif nilai == 'C':
  print('Perbanyak belajar')
elif nilai == 'D':
  print('Jangan keseringan main')
elif nilai == 'E':
  print('Kebanyakan bolos...')
else:
  print('Maaf, format nilai tidak sesuai')
  
#Setiap kondisi dari block elif ini bisa diisi dengan perbandingan yang lebih kompleks, seperti contoh berikut:
nilai = 65
print('Nilai:',nilai)
 
if nilai >= 90:
  print('Pertahankan')
elif (nilai >= 80) and (nilai < 90):
  print('Harus lebih baik lagi')
elif (nilai >= 60) and (nilai < 80):
  print('Perbanyak belajar')
elif (nilai >= 40) and (nilai < 60):
  print('Jangan keseringan main')
elif nilai < 40:
  print('Kebanyakan bolos...')
else:
  print('Maaf, format nilai tidak sesuai')