"""
ini adalah Tugas Besar Mata Kuliah Pengantar Rekayasa dan Desain PRD KU1202
Kelompok 4 yang membahas Equivalent Circuit Solver
Anggota Kelompok:
1. Febryola Kurnia Putri(16520050)
2. Raki Fajar Rizki Andrawijaya(16520060)
3. Tanya Nuhaisy Wulandari(16520080)
4. Joshi Ryu Setiady(16520230)
5. Syamira Rugayyah Alhaddad(16520250)
 """  
#LIBRARY YANG MEMBERIKAN WARNA PADA PROGRAM
from colorama import init #Library untuk memberikan warna pada program
init()
from colorama import Fore, Back, Style

print(Fore.CYAN +'')
print("""

███████╗ ██████╗ ██╗   ██╗██╗██╗   ██╗ █████╗ ██╗     ███████╗███╗   ██╗████████╗ 
██╔════╝██╔═══██╗██║   ██║██║██║   ██║██╔══██╗██║     ██╔════╝████╗  ██║╚══██╔══╝    
█████╗  ██║   ██║██║   ██║██║██║   ██║███████║██║     █████╗  ██╔██╗ ██║   ██║        
██╔══╝  ██║▄▄ ██║██║   ██║██║╚██╗ ██╔╝██╔══██║██║     ██╔══╝  ██║╚██╗██║   ██║       
███████╗╚██████╔╝╚██████╔╝██║ ╚████╔╝ ██║  ██║███████╗███████╗██║ ╚████║   ██║        
╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝        

                ██████╗██╗██████╗  ██████╗██╗   ██╗██╗████████╗ 
                ██╔════╝██║██╔══██╗██╔════╝██║   ██║██║╚══██╔══╝
                ██║     ██║██████╔╝██║     ██║   ██║██║   ██║   
                ██║     ██║██╔══██╗██║     ██║   ██║██║   ██║   
                ╚██████╗██║██║  ██║╚██████╗╚██████╔╝██║   ██║  
                ╚═════╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝  """)               
print(Style.RESET_ALL)#MERESET WARNA PROGRAM
nama = input("Masukan Nama Anda: ")
print()
print("\033[36mHALLO, "+str(nama))
print(Style.RESET_ALL)
print(Fore.BLACK+""+ Back.WHITE+"") #MEMBERI WARNA
print(" Selamat datang di program circuit equivalent pada program ini, kami akan ")
print("   membantu anda untuk menemukan nilai Rth, Vth, dan Ith dari rangkaian   ") 
print("             equivalent dengan menggunakan metode thevenin                ") 
print()
print("   Untuk itu, silakan pilih rangkaian yang anda butuhkan berikut terdapat ")
print("  5 jenis rangkaian equivalent, silakan masukkan nomor yang sesuai dengan ")
print("               gambar rangkaian yang anda butuhkan                        ") 
print(Style.RESET_ALL)#MERESET WARNA PROGRAM
print()
#FUNGSI UTAMA

def byebye(): # Fungsi yang mengeluarkan pesan bye bye jika program telah selesai
    print("""
                    
           ██████╗ ██╗   ██╗███████╗    ██████╗ ██╗   ██╗███████╗
           ██╔══██╗╚██╗ ██╔╝██╔════╝    ██╔══██╗╚██╗ ██╔╝██╔════╝
           ██████╔╝ ╚████╔╝ █████╗      ██████╔╝ ╚████╔╝ █████╗  
           ██╔══██╗  ╚██╔╝  ██╔══╝      ██╔══██╗  ╚██╔╝  ██╔══╝  
           ██████╔╝   ██║   ███████╗    ██████╔╝   ██║   ███████╗
           ╚═════╝    ╚═╝   ╚══════╝    ╚═════╝    ╚═╝   ╚══════╝                                                   
                    """)
    print(Style.RESET_ALL)

def rangkaian(): #Fungsi yang memanggil rangkaian
    print(Fore.BLACK+""+Back.WHITE+"")
    print("""
1. Rangkaian equivalent pertama""")
    print(Style.RESET_ALL)
    print("""
       \033[41mn1\033[0m____\033[36m(R1)\033[0m____.____\033[36m(R2)\033[0m____.\033[41mn-\033[0m      \033[93mKeterangan:\033[0m
        |            |                     R1 = nilai resistor 1
        |            |                     R2 = nilai resistor 2
        |           \033[36m(R3)\033[0m                   R3 = nilai resistor 3
        |            |                     R4 = nilai resistor 4
       \033[93m(V)\033[0m           |                     (V)= nilai tegangan sumber bebas
        |            |
        |           \033[36m(R4)\033[0m
        |            |
        |____________|____________.\033[41mn+\033[0m  """)
        #Ga perlu diubah ya gaes yg udah aku edit please, di outputnya rapi kok
    print(Fore.BLACK+""+Back.WHITE+"")
    print("""
2. Rangkaian equivalent kedua""")
    print(Style.RESET_ALL)
    print("""
            
         ____\033[36m(R1)\033[0m____.____\033[36m(R2)\033[0m____.\033[41ma\033[0m      \033[93mKeterangan:\033[0m
        |            |                    R1 = nilai resistor 1
        |            |                    R2 = nilai resistor 2  
       \033[34m<V>\033[0m          \033[93m(R3)\033[0m                  R3 = nilai resistor 3
        |            |                    <v>= nilai tegangan sumber tidak bebas
        |____________|____________.\033[41mb\033[0m """)

    print(Fore.BLACK+""+Back.WHITE+"")
    print("""
3. Rangkaian equivalent ketiga""")
    print(Style.RESET_ALL)
    print("""
         ____\033[36m(R1)\033[0m____\033[34m<V>\033[0m__________.\033[41ma\033[0m      \033[93mKeterangan:\033[0m
        |                   |             R1 = nilai resistor 1
        |                   |             R2 = nilai resistor 2
       \033[36m(R2)\033[0m                \033[36m(R3)\033[0m           R3 = nilai resistor 3
        |                   |             <v>= nilai tegangan sumber tidak bebas
        |___________________|_____.\033[41mb\033[0m """)

    print(Fore.BLACK+""+Back.WHITE+"")
    print("""
4. Rangkaian equivalent keempat""")
    print(Style.RESET_ALL)
    print("""       
             + V0 -
         ____\033[36m(R1)\033[0m____.____\033[36m(R2)\033[0m____      \033[93mKeterangan:\033[0m
        |            |            |     R1 = nilai resistor 1
      + |            \033[41ma\033[0m            | +   R2 = nilai resistor 2  
       \033[93m(V)\033[0m                       \033[34m<V>\033[0m    (V)= nilai tegangan sumber bebas
      - |            \033[41mb\033[0m            | -   <v>= nilai tegangan sumber tidak
        |____________|____________|           bebas (dalam unit V0)
""")

    print(Fore.BLACK+""+Back.WHITE+"")
    print("""
5. Rangkaian equivalent kelima""")
    print(Style.RESET_ALL)
    print("""
         _______________\033[36m(R2)\033[0m____________________.\033[41ma\033[0m      \033[93mKeterangan:\033[0m
        |        |                |      |              R1 = nilai resistor 1
        |       \033[36m(R3)\033[0m            \033[36m(R4)\033[0m     |              R2 = nilai resistor 2  
       \033[93m(V1)\033[0m      |________________|     \033[93m(V3)\033[0m            R3 = nilai resistor 3 
        |                |               |              R4 = nilai resistor 4 
        |              \033[36m(R5)\033[0m              |              R5 = nilai resistor 5 
        |                |               |              R6 = nilai resistor 6
       \033[36m(R1)\033[0m              |              \033[36m(R6)\033[0m           (V1)= nilai tegangan sumber bebas 1
        |              \033[93m(V2)\033[0m              |             (V2)= nilai tegangan sumber bebas 2
        |________________|_______________|______.\033[41mb\033[0m     (V3)= nilai tegangan sumber bebas 3

        """)

def aboutus():
    print("""
\033[34m@@@@@@@@@@@@@@@@@@@@@@@\033[0m Ini adalah Program Kami \033[34m@@@@@@@@@@@@@@@@@@@@@@@@@@\033[0m
\033[34m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\033[0m

siapa kami?

Kelompok 4 PRD K24 2020/2021:
1. Febryola Kurnia Putri panggil aja \033[93mYOLA\033[0m
2. Raki Fajar Rizki Andrawijaya panggil aja \033[34mRAKI\033[0m
3. Tanya Nuhaisy Wulandari panggil aja \033[31mANYA\033[0m
4. Joshi Ryu Setiady panggil aja \033[92mJOSHI\033[0m
5. Syamira Rugayyah Alhaddad panggil aja \033[36mSYAMIRA\033[0m

\033[34m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\033[0m
\033[34m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\033[0m

    """)
def program():
    print("""\033[92m=======================Silakan Pilih Menu di Bawah ini====================
**************************************************************************\033[0m""")
    print()
    print("=================Berikut Menu Yang Tersedia Pada Program Ini==============")
    print(Fore.BLACK+""+ Back.WHITE+"") #MEMBERI WARNA
    print("""1. Help (Petunjuk Sistem);
2. Simulasi Rangkaian    ;
3. About Us              .""") 
    print(Style.RESET_ALL +Fore.WHITE+ "")#MERESET WARNA PROGRAM
    print("**************************************************************************")
    print("==========================================================================")

#PROGRAM UTAMA
    while True:
        print(Fore.RED+"")
        menu = int(input("Masukan nomor menu yang ingin dilakukan: "))
        print(Style.RESET_ALL)
        if menu==1:
            print("""
==================Berikut Petunjuk Penggunaan Sistem Ini==================
**************************************************************************

1. Sistem ini adalah sistem yang dibuat untuk para engineer yang ingin
   menyelesaikan permasalahan mengenai equivalent circuit
2. Pada sistem ini terdapat 5 jenis rangkaian equivalen
3. Anda tinggal memasukkan nilai resistor dan voltasenya 
4. Hasil akhir dari program ini adalah berupa nilai Rth,Vth,dan Ith
5. Setelah itu Program akan selesai

**************************************************************************
==========================================================================""")
            print()
            break
        elif menu==2:
            rangkaian()
            break
        elif menu==3:
            aboutus()
            break
        else:
            print("Silakan, Masukan Menu yang valid")

    lanjut = input("Apakah anda ingin melakukan simulasi rangkaian ini (Y/N): ")
    if lanjut=="Y" or lanjut=="y":
        rangkaian()
        
        while True:
            pilihan = int(input("Silakan Inputkan Nomor Rangkaian Yang Ingin Anda Selesaikan: "))
            if (pilihan==1):
                print()
                print(""" 
=============Berikut bentuk rangkaian yang akan anda selesaikan=============
============================================================================

       \033[41mn1\033[0m____\033[36m(R1)\033[0m____.____\033[36m(R2)\033[0m____.\033[41mn-\033[0m      Keterangan:
        |            |                     R1 = nilai resistor 1
        |            |                     R2 = nilai resistor 2
        |           \033[36m(R3)\033[0m                   R3 = nilai resistor 3
        |            |                     R4 = nilai resistor 4
       \033[93m(V)\033[0m           |                     (V)= nilai tegangan sumber bebas
        |            |
        |           \033[36m(R4)\033[0m
        |            |
        |____________|____________.\033[41mn+\033[0m  

============================================================================
============================================================================""")
                print()
                R1=float(input("Masukan nilai resistor 1 (ohm): "))
                R2=float(input("Masukan nilai resistor 2 (ohm): "))
                R3=float(input("Masukan nilai resistor 3 (ohm): "))
                R4=float(input("Masukan nilai resistor 4 (ohm): "))
                V=float(input("Masukan nilai voltase (volt)  : "))

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
==========Bentuk rangkaian theveninnya akan menjadi seperti berikut=========

                 ______\033[36m(Rth)\033[0m_______.\033[41mn+\033[0m
                |
                |
              \033[93m(Vth)\033[0m
                |
                |__________________.\033[41mn-\033[0m

============================================================================
                """)
                print("""
==========Berikut hasil thevenin dari rangkaian equivalent di atas==========""")
                print()
                print("Nilai \033[93mR theveninnya\033[0m adalah", Rth, "ohm")
                print("Nilai \033[36mV theveninnya\033[0m adalah", Vth, "volt")
                print("Nilai \033[91mI theveninnya\033[0m adalah", Ith, "Ampere")
                print()
                b=input("Apakah Anda ingin melanjutkan program equivalent circuit ini? (Y/N): ")
                if b=="Y" or b=="y":
                    print()
                    program() #Memanggil kembali program utama
                    break

                elif b=="N" or b=="n":
                    print("""
****************************************************************************
=========================PROGRAM ANDA TELAH SELESAI=========================""")
                    print(Fore.LIGHTYELLOW_EX+"") #memberikan warna kuning pada huruf byebye
                    byebye() #Mengeluarkan pesan bye bye ke sistem
                    break

            elif (pilihan==2):
                print()
                print(""" 
============Berikut bentuk rangkaian yang akan anda selesaikan==============
============================================================================

         ____\033[36m(R1)\033[0m____.____\033[36m(R2)\033[0m____.\033[41ma\033[0m      \033[93mKeterangan:\033[0m
        |            |                    R1 = nilai resistor 1
        |            |                    R2 = nilai resistor 2  
       \033[34m<V>\033[0m          \033[93m(R3)\033[0m                  R3 = nilai resistor 3
        |            |                    <v>= nilai tegangan sumber tidak bebas
        |____________|____________.\033[41mb\033[0m 
===========================================================================
===========================================================================""")
                print()
                R1=float(input("Masukan nilai resistor 1 (ohm): "))
                R2=float(input("Masukan nilai resistor 2 (ohm): "))
                R3=float(input("Masukan nilai resistor 3 (ohm): "))
                V=float(input("Masukan nilai voltase (volt)  : "))
                break

            elif (pilihan==3):
                print()
                print(""" 
==============Berikut bentuk rangkaian yang akan anda selesaikan============
============================================================================
         ____\033[36m(R1)\033[0m____\033[34m<V>\033[0m__________.\033[41ma\033[0m      \033[93mKeterangan:\033[0m
        |                   |             R1 = nilai resistor 1
        |                   |             R2 = nilai resistor 2
       \033[36m(R2)\033[0m                \033[36m(R3)\033[0m           R3 = nilai resistor 3
        |                   |             <v>= nilai tegangan sumber tidak bebas
        |___________________|_____.\033[41mb\033[0m
============================================================================
============================================================================""")
                print()
                R1=float(input("Masukan nilai resistor 1 (ohm): "))
                R2=float(input("Masukan nilai resistor 2 (ohm): "))
                R3=float(input("Masukan nilai resistor 3 (ohm): "))
                V=float(input("Masukan nilai voltase (volt)  : "))
                break

            elif (pilihan==4):
                print()
                print(""" 
==============Berikut bentuk rangkaian yang akan anda selesaikan============
============================================================================

                + V0 -
             ____\033[36m(R1)\033[0m____.____\033[36mm(R2)\033[0m____      \033[93mKeterangan:\033[0m
            |            |            |    R1 = nilai resistor 1
          + |            \033[41ma\033[0m            | +  R2 = nilai resistor 2  
           \033[93m(V)\033[0m                       \033[34m<V>\033[0m   (V)= nilai tegangan sumber bebas
          - |            \033[41mb\033[0m            | -  <v>= nilai tegangan sumber tidak
            |____________|____________|          bebas (dalam unit V0)

============================================================================
============================================================================""")
                print()
                R1=float(input("Masukan nilai resistor 1 (ohm)         : "))
                R2=float(input("Masukan nilai resistor 2 (ohm)         : "))
                V1=float(input("Masukan nilai voltase bebas (volt)     : "))
                Vd=float(input("Masukan nilai voltase tidak bebas (V0) : "))
                
                # Nilai Vth didapatkan dengan cara sebagai berikut
                # Mencari nilai I dengan menggunakan prinsip KVL Pada loop luar
                # -V1 + I * R1 + I * R2 + V2 = 0
                # substitusikan nilai V2 = Vd * R1 * I
                # -V1 + I * R1 + I * R2 + Vd * R1 * I = 0
                # -V1 + I * (R1 + R2 + Vd * R1) = 0
                # I = V1 / (R1 + R2 + Vd * R1)
                # Gunakan nilai I tersebut dalam KVL pada loop kiri
                # -V1 + (R1 * I) + Vth = 0
                # Vth = V1 - (R1 * I)
                I = V1 / (R1 + R2 + (Vd * R1))
                Vth = V1 - (R1 * I)

                # Untuk menentukan R theveninnya
                # Hilangkan sumber tegangan independen dan letakkan sumber tegangan uji bernilai 1V di ab
                V0 = -1 # besar V0 sama dengan besar sumber tegangan uji karena paralel
                Vd = 4 * V0
                Ia = -V0 / R1
                # Mencari Ib menggunakan KVL pada loop luar
                # -Ia * R1 + Ib * R2 + Vd = 0
                # substitusikan -Ia * R1 = V0
                # V0 + Ib * R2 + Vd = 0
                # Ib = (-V0 - Vd) / R2
                Ib = (-V0 - Vd) / R2
                # Cari besar arus yang dikeluarkan oleh sumber tegangan uji (I0)
                I0 = Ia + Ib
                # cari R thevenin menggunakan rumus Rth = 1 / I0
                Rth = 1/I0

                # Mencari Ith menggunakan rumus Ith = Vth / Rth
                Ith = Vth / Rth

                print("""
==========Bentuk rangkaian theveninnya akan menjadi seperti berikut=========

                 ______\033[36m(Rth)\033[0m_______.\033[41mn+\033[0m
                |
                |
              \033[93m(Vth)\033[0m
                |
                |__________________.\033[41mn-\033[0m

============================================================================
                """)
                print("""
==========Berikut hasil thevenin dari rangkaian equivalent di atas==========""")
                print()
                print("Nilai \033[93mR theveninnya\033[0m adalah", Rth, "ohm")
                print("Nilai \033[36mV theveninnya\033[0m adalah", Vth, "volt")
                print("Nilai \033[91mI theveninnya\033[0m adalah", Ith, "Ampere")
                print()
                b=input("Apakah Anda ingin melanjutkan program equivalent circuit ini? (Y/N): ")
                if b=="Y" or b=="y":
                    print()
                    program() #Memanggil kembali program utama
                    break

                elif b=="N" or b=="n":
                    print("""
****************************************************************************
=========================PROGRAM ANDA TELAH SELESAI=========================""")
                    print(Fore.LIGHTYELLOW_EX+"") #memberikan warna kuning pada huruf byebye
                    byebye() #Mengeluarkan pesan bye bye ke sistem
                    break
            elif (pilihan==5):
                print()
                print("""
=======================Berikut bentuk rangkaian yang akan anda selesaikan=====================
==============================================================================================

         _______________\033[36m(R2)\033[0m____________________.\033[41ma\033[0m      \033[93mKeterangan:\033[0m
        |        |                |      |              R1 = nilai resistor 1
        |       \033[36m(R3)\033[0m            \033[36m(R4)\033[0m     |              R2 = nilai resistor 2  
       \033[93m(V1)\033[0m      |________________|     \033[93m(V3)\033[0m            R3 = nilai resistor 3 
        |                |               |              R4 = nilai resistor 4 
        |              \033[36m(R5)\033[0m              |              R5 = nilai resistor 5 
        |                |               |              R6 = nilai resistor 6
       \033[36m(R1)\033[0m              |              \033[36m(R6)\033[0m           (V1)= nilai tegangan sumber bebas 1
        |              \033[93m(V2)\033[0m              |             (V2)= nilai tegangan sumber bebas 2
        |________________|_______________|______.\033[41mb\033[0m     (V3)= nilai tegangan sumber bebas 3
                
===============================================================================================
===============================================================================================""")
                print()
                R1=float(input("Masukan nilai resistor 1 (ohm)   : "))
                R2=float(input("Masukan nilai resistor 2 (ohm)   : "))
                R3=float(input("Masukan nilai resistor 3 (ohm)   : "))
                R4=float(input("Masukan nilai resistor 4 (ohm)   : "))
                R5=float(input("Masukan nilai resistor 5 (ohm)   : "))
                V1=float(input("Masukan nilai voltase 1 (volt)   : "))
                V2=float(input("Masukan nilai voltase 2 (volt)   : "))
                V3=float(input("Masukan nilai voltase 3 (volt)   : "))
                break

            else:
                print()
                print("Masukan tidak valid, silakan pilih dari 1-5 rangkaian")

    elif lanjut=="N" or lanjut=="n":
        print("""
================TERIMA KASIH TELAH MELAKUKAN SIMULASI INI=================
===================SILAKAN DICOBA KEMBALI DILAIN WAKTU====================""")
        print(Fore.CYAN+"")
        byebye() #Mencetak keluaran huruf byebye
        
menu = input("Apakah Anda ingin melanjutkan ke bagian menu (Y/N): ")
print()
if menu == "Y" or menu == "y":
#Memanggil Program  
    program()
elif menu =="N" or menu=="n":
    print("""
================TERIMA KASIH TELAH MELAKUKAN SIMULASI INI=================
===================SILAKAN DICOBA KEMBALI DILAIN WAKTU====================""")
    print(Fore.CYAN+"")
    byebye() #Mencetak keluaran huruf byebye


