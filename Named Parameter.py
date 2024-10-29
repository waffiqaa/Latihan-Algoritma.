#Berikut format dasar penggunaannya:
def x(var1, var2, var3):
  ## isi fungsi disini...
  ## isi fungsi disini...
 x(var3 = 100, var1 = 200, var2 = 300)
 
#Contoh Kode Program Python untuk Named Parameter
def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(5) )      # 25
print( pangkat(5,4) )    # 625
print( pangkat(6,6) )    # 46656

#Dengan memakai teknik named parameter, kita bisa menjalankan fungsi pangkat() sebagai berikut:
def pangkat(angka, pangkat = 2):
  hasil = 1
  for i in range(0,pangkat):
    hasil = hasil * angka
  return hasil;
 
print( pangkat(angka = 4,pangkat = 3) )      # 64
print( pangkat(pangkat = 2,angka = 9) )      # 81

#contoh lain, perhatikan fungsi akses_database() berikut ini:
def akses_database(address,username,password):
  print("====Database Connection====");
  print("server: ",address);
  print("username: ",username);
  print("password: ",password);
  print(".....connection success!");
   
akses_database("barudakwell","rizz","123456")

#Biasanya kita harus menghapal urutan setiap parameter.
#Namun dengan named parameter, urutan ini bisa suka-suka seperti contoh berikut:
def akses_database(address,username,password):
  print("====Database Connection====");
  print("server: ",address);
  print("username: ",username);
  print("password: ",password);
  print(".....connection success!");
   
akses_database(username="dhkvlr",password="bintang skibidi",address="128.123.0.2")