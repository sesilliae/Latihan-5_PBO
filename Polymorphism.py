class Kendaraan:
     def intro(self):
        print("Ada beberapa Jenis Kendaraan")
  
     def bahanbakar(self):
        print("Setiap kendaraan memakai bahan bakar yang berbeda-beda")
         
  
class Motor(Kendaraan):
     def bahanbakar(self):
        print("Bahan bakar yang dipakai oleh motor adalah bensin")
     
  
class Pesawat(Kendaraan):
     def bahanbakar(self):
        print("Bahan bakar yang dipakai oleh pesawat adalah aftur")
  
obj_Kendaraan = Kendaraan()
obj_Motor = Motor()
obj_Pesawat = Pesawat()
  
obj_Kendaraan.intro()
obj_Kendaraan.bahanbakar()
  
obj_Motor.intro()
obj_Motor.bahanbakar()
  
obj_Pesawat.intro()
obj_Pesawat.bahanbakar()