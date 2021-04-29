#Kodingan buat TUBES PRD
#Baru inputnya doang gaess, belom kebayang implementasi rumus2nyaaa :nnnn


    # Diambil dari : https://patorjk.com/software/taag/#p=display&f=Big&t=Kantong%20Ajaib
print("""

  ______            _            _            _      _____ _                _ _   
 |  ____|          (_)          | |          | |    / ____(_)              (_) |  
 | |__   __ _ _   _ ___   ____ _| | ___ _ __ | |_  | |     _ _ __ ___ _   _ _| |_ 
 |  __| / _` | | | | \ \ / / _` | |/ _ \ '_ \| __| | |    | | '__/ __| | | | | __|
 | |___| (_| | |_| | |\ V / (_| | |  __/ | | | |_  | |____| | | | (__| |_| | | |_ 
 |______\__, |\__,_|_| \_/ \__,_|_|\___|_| |_|\__|  \_____|_|_|  \___|\__,_|_|\__|
           | |                                                                    
           |_|                                                               
""")

print("""
Selamat datang di program circuit equivalent pada program ini, 
kami akan membantu anda untuk menemukan nilai Rth, Vth, dan Ith 
dari rangkaian equivalent dengan menggunakan metode thevenin

Untuk itu, silakan pilih rangkaian yang anda butuhkan berikut
terdapat 5 jenis rangkaian equivalent, silakan masukkan nomor 
yang sesuai dengan gambar rangkaian yang anda butuhkan""") 

print("""
1. Rangkaian equivalent pertama

  n1____(R1)____.____(R2)____.n-      Keterangan:
   |            |                     R1 = nilai resistor 1
   |            |                     R2 = nilai resistor 2
   |           (R3)                   R3 = nilai resistor 3
   |            |                     R4 = nilai resistor 4
  (V)           |                     (V)= nilai tegangan sumber bebas
   |            |
   |           (R4)
   |            |
   |____________|____________.n+

2. Rangkaian equivalent kedua
   
    ____(R1)____.____(R2)____.a      Keterangan:
   |            |                    R1 = nilai resistor 1
   |            |                    R2 = nilai resistor 2  
  <V>          (R3)                  R3 = nilai resistor 3
   |            |                    <v>= nilai tegangan sumber tidak bebas
   |____________|____________.b
   
3. Rangkaian equivalent ketiga

    ____(R1)____<V>__________.a      Keterangan:
   |                   |             R1 = nilai resistor 1
   |                   |             R2 = nilai resistor 2
  (R2)                (R3)           R3 = nilai resistor 3
   |                   |             <v>= nilai tegangan sumber tidak bebas
   |___________________|_____.b


4. Rangkaian equivalent keempat
   
    ____(R1)____.____(R2)____        Keterangan:
   |            |            |       R1 = nilai resistor 1
   |            a            |       R2 = nilai resistor 2  
  (V)                       <V>      (V)= nilai tegangan sumber bebas
   |            b            |       <v>= nilai tegangan sumber tidak bebas
   |____________|____________|

5. Rangkaian equivalent kelima

    _______________(R2)____________________.a      Keterangan:
   |        |                |      |              R1 = nilai resistor 1
   |       (R3)            (R4)     |              R2 = nilai resistor 2  
  (V1)      |________________|     (V3)            R3 = nilai resistor 3 
   |                |               |              R4 = nilai resistor 4 
   |              (R5)              |              R5 = nilai resistor 5 
   |                |               |              (V1)= nilai tegangan sumber bebas 1
  (R1)              |              (R5)            (V2)= nilai tegangan sumber bebas 2
   |              (V2)              |              (V3)= nilai tegangan sumber bebas 3
   |________________|_______________|______.b


""")

while True:
    pilihan = int(input("Silakan Inputkan Nomor Rangkaian Yang Ingin Anda Selesaikan: "))
    if (pilihan==1):
        print()
        print(""" 
        ==========Berikut bentuk rangkaian yang akan anda selesaikan==========
        ======================================================================

       n1____(R1)____.____(R2)____.n+      Keterangan:
        |            |                     R1 = nilai resistor 1
        |            |                     R2 = nilai resistor 2
        |           (R3)                   R3 = nilai resistor 3
        |            |                     R4 = nilai resistor 4
        (V)          |                     (V)= nilai tegangan sumber bebas
        |            |
        |           (R4)
        |            |
        |____________|____________.n- 
        
        ======================================================================
        ======================================================================""")
        print()
        R1=int(input("Masukan nilai resistor 1 (ohm): "))
        R2=int(input("Masukan nilai resistor 2 (ohm): "))
        R3=int(input("Masukan nilai resistor 3 (ohm): "))
        R4=int(input("Masukan nilai resistor 4 (ohm): "))
        V=int(input("Masukan nilai voltase (volt)  : "))

        # Untuk Mencari Rth maka matikan sumber bebas sehingga didapatkan nilainya
        # Rth dapat ditentukan dengan menggunakan prinsip seri paralel
        # Pada rangkaian ini maka, R3 dan R4 diserikan menjadi R34
        # Hasil pada R34 diparalelkan dengan R1 menjadi R134
        # Hasil pada R234 diparalelkan dengan R2 menjadi R1234
        # Maka berikut penyelesaiannya
        R34 = R3 + R4
        R134 = (R1*R34)/(R1+R34)
        R1234 = R2 + R134
        Rth = R1234

        # Nilai Vth didapatkan dengan cara sebagai berikut
        # Gunakan prinsip KCL Pada setiap simpul
        # V1-Vground = V
        # i1 = i2 + i3
        # (V1 - V+)/R1 = i1
        # (V+ - Vg)/R34 = i3
        # Substitusi ke persamaan awal
        # i2 = 0 karena rangkaian terputus, Vg = 0 karena merupakan ground, sehingga persamaan menjadi
        # (V1 - V+)/R1 = (V+)/R34 
        # V1/R1 = V+((R1+R34)/(R1.R34))
        # pada rangkaian diketahui bahwa V+ = Vth
        # Vth = V1(R34/(R1+R34))
        
        Vth = V*(R34/(R1+R34))

        # Berikut persamaan untuk menentukan I theveninnya
        Ith = Vth/Rth
        print("""
        =======Bentuk rangkaian theveninnya akan menjadi seperti berikut======

         ______(Rth)_______.n+
        |
        |
      (Vth)
        |
        |__________________.n-

        =======================================================================
        """)
        print("""
        =======Berikut hasil thevenin dari rangkaian equivalent di atas========""")
        print()
        print("Nilai R theveninnya adalah", Rth, "ohm")
        print("Nilai V theveninnya adalah", Vth, "volt")
        print("Nilai I theveninnya adalah", Ith, "Ampere")
        print("""
        ***********************************************************************
        =======================PROGRAM ANDA TELAH SELESAI======================""")
        break

    elif (pilihan==2):
        print()
        print(""" 
        ==========Berikut bentuk rangkaian yang akan anda selesaikan===========
        =======================================================================

         ____(R1)____.____(R2)____.a      Keterangan:
        |            |                    R1 = nilai resistor 1
        |            |                    R2 = nilai resistor 2  
       <V>          (R3)                 R3 = nilai resistor 3
        |            |                    <v>= nilai tegangan sumber tidak bebas
        |____________|____________.b
        
        ======================================================================
        ======================================================================""")
        print()
        R1=int(input("Masukan nilai resistor 1 (ohm): "))
        R2=int(input("Masukan nilai resistor 2 (ohm): "))
        R3=int(input("Masukan nilai resistor 3 (ohm): "))
        V=int(input("Masukan nilai voltase (volt)  : "))
        break

    elif (pilihan==3):
        print()
        print(""" 
        ============Berikut bentuk rangkaian yang akan anda selesaikan==========
        ========================================================================

         ____(R1)____<V>__________.a      Keterangan:
        |                   |             R1 = nilai resistor 1
        |                   |             R2 = nilai resistor 2
       (R2)                (R3)           R3 = nilai resistor 3
        |                   |             <v>= nilai tegangan sumber tidak bebas
        |___________________|_____.b
         
        =========================================================================
        =========================================================================""")
        print()
        R1=int(input("Masukan nilai resistor 1 (ohm): "))
        R2=int(input("Masukan nilai resistor 2 (ohm): "))
        R3=int(input("Masukan nilai resistor 3 (ohm): "))
        V=int(input("Masukan nilai voltase (volt)  : "))
        break

    elif (pilihan==4):
        print()
        print(""" 
        ===========Berikut bentuk rangkaian yang akan anda selesaikan===========
        ========================================================================

         ____(R1)____.____(R2)____        Keterangan:
        |            |            |       R1 = nilai resistor 1
        |            a            |       R2 = nilai resistor 2  
       (V)                       <V>     (V)= nilai tegangan sumber bebas
        |            b            |       <v>= nilai tegangan sumber tidak bebas
        |____________|____________|

        ========================================================================
        ========================================================================""")
        print()
        R1=int(input("Masukan nilai resistor 1 (ohm)         : "))
        R2=int(input("Masukan nilai resistor 2 (ohm)         : "))
        V1=int(input("Masukan nilai voltase bebas (volt)     : "))
        V2=int(input("Masukan nilai voltase tidak bebas(volt): "))
        break
    elif (pilihan==5):
        print()
        print("""
        ==========Berikut bentuk rangkaian yang akan anda selesaikan============
        ========================================================================

         ________________(R2)___________________.a      Keterangan:
        |         |                |     |              R1 = nilai resistor 1
        |       (R3)            (R4)     |              R2 = nilai resistor 2  
       (V1)       |________________|    (V3)            R3 = nilai resistor 3 
        |                |               |              R4 = nilai resistor 4 
        |              (R5)              |              R5 = nilai resistor 5 
        |                |               |              (V1)= nilai tegangan sumber bebas 1
       (R1)              |              (R5)            (V2)= nilai tegangan sumber bebas 2
        |              (V2)              |              (V3)= nilai tegangan sumber bebas 3
        |________________|_______________|______.b
        
        ========================================================================
        ========================================================================""")
        print()
        R1=int(input("Masukan nilai resistor 1 (ohm)   : "))
        R2=int(input("Masukan nilai resistor 2 (ohm)   : "))
        R3=int(input("Masukan nilai resistor 3 (ohm)   : "))
        R4=int(input("Masukan nilai resistor 4 (ohm)   : "))
        R5=int(input("Masukan nilai resistor 5 (ohm)   : "))
        V1=int(input("Masukan nilai voltase 1 (volt)   : "))
        V2=int(input("Masukan nilai voltase 2 (volt)   : "))
        V3=int(input("Masukan nilai voltase 3 (volt)   : "))
        break

    else:
        print()
        print("Masukan tidak valid, silakan pilih dari 1-5 rangkaian")
        



