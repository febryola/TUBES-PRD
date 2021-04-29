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
  (V)           |____________.n+      (V)= nilai tegangan sumber bebas
   |            |
   |           (R4)
   |            |
   |____________|

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

    ______________(R2)____.________________.a      Keterangan:
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
        print(""" Berikut bentuk rangkaian yang akan anda selesaikan
    n1____(R1)____.____(R2)____.n-      Keterangan:
    |            |                     R1 = nilai resistor 1
    |            |                     R2 = nilai resistor 2
    |           (R3)                   R3 = nilai resistor 3
    |            |                     R4 = nilai resistor 4
    (V)          |____________.n+      (V)= nilai tegangan sumber bebas
    |            |
    |           (R4)
    |            |
    |____________|""")

    elif (pilihan==2):
        print(""" Berikut bentuk rangkaian yang akan anda selesaikan
    
     ____(R1)____.____(R2)____.a      Keterangan:
    |            |                    R1 = nilai resistor 1
    |            |                    R2 = nilai resistor 2  
    <V>          (R3)                  R3 = nilai resistor 3
    |            |                    <v>= nilai tegangan sumber tidak bebas
    |____________|____________.b
        """)

    elif (pilihan==3):

        print(""" Berikut bentuk rangkaian yang akan anda selesaikan
     ____(R1)____<V>__________.a      Keterangan:
    |                   |             R1 = nilai resistor 1
    |                   |             R2 = nilai resistor 2
    (R2)                (R3)           R3 = nilai resistor 3
    |                   |             <v>= nilai tegangan sumber tidak bebas
    |___________________|_____.b
        """)

    elif (pilihan==4):
        print(""" Berikut bentuk rangkaian yang akan anda selesaikan
        ____(R1)____.____(R2)____        Keterangan:
    |            |            |       R1 = nilai resistor 1
    |            a            |       R2 = nilai resistor 2  
    (V)                       <V>      (V)= nilai tegangan sumber bebas
    |            b            |       <v>= nilai tegangan sumber tidak bebas
    |____________|____________|
        """)

    elif (pilihan==5):
        print("""berikut bentuk rangkaian yang akan anda selesaikan
        
        ______________(R2)____.________________.a      Keterangan:
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
    else:
        print()
        print("Masukan tidak valid, silakan pilih dari 1-5 rangkaian")
        

jumlah_node = int(input("Masukkan jumlah node pada rangkaian: "))
R = int(input("Masukkan jumlah resistor           : "))
V = int(input("Masukkan jumlah voltase            : "))
print()
R1=[]
V1=[]
for r in range(R):
    R2=int(input("Masukkan nilai resistor ke-{} (ohm) : ".format(r+1)))
    R1.append(R2)
for resistor in R1:
    print("Array dari resistor adalah", R1)
    break
print()
for v in range(V):
    V2=int(input("Masukkan nilai voltase ke-{} (volt) : ".format(v+1)))
    V1.append(V2)
for voltase in V1:
    print("Array dari voltase adalah", V1)
    break

