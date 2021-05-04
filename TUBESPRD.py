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
       \033[41mn1\033[0m____\033[36m(R1)\033[0m____.____\033[36m(R2)\033[0m____.\033[41mn-\033[0m      Keterangan:
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
    print("""
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
        |                |               |             (V1)= nilai tegangan sumber bebas 1
       (R1)              |              (R5)           (V2)= nilai tegangan sumber bebas 2
        |              (V2)              |             (V3)= nilai tegangan sumber bebas 3
        |________________|_______________|______.b

        """)


def program():
    print("""\033[92m=======================Silakan Pilih Menu di Bawah ini====================
**************************************************************************\033[0m""")
    print()
    print("=================Berikut Menu Yang Tersedia Pada Program Ini==============")
    print(Fore.BLACK+""+ Back.WHITE+"") #MEMBERI WARNA
    print("""1. Help (Petunjuk Sistem)
2. Simulasi Rangkaian    """) 
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

                 ______\033[36m(Rth)\033[0m_______.n+
                |
                |
              \033[93m(Vth)\033[0m
                |
                |__________________.n-

============================================================================
                """)
                print("""
==========Berikut hasil thevenin dari rangkaian equivalent di atas==========""")
                print()
                print("Nilai R theveninnya adalah", Rth, "ohm")
                print("Nilai V theveninnya adalah", Vth, "volt")
                print("Nilai I theveninnya adalah", Ith, "Ampere")
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

         ____(R1)____.____(R2)____.a      Keterangan:
        |            |                    R1 = nilai resistor 1
        |            |                    R2 = nilai resistor 2  
       <V>          (R3)                  R3 = nilai resistor 3
        |            |                    <v>= nilai tegangan sumber tidak bebas
        |____________|____________.b
                
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

             ____(R1)____<V>__________.a      Keterangan:
            |                   |             R1 = nilai resistor 1
            |                   |             R2 = nilai resistor 2
           (R2)                (R3)           R3 = nilai resistor 3
            |                   |             <v>= nilai tegangan sumber tidak 
            |___________________|_____.b           bebas
                
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

             ____(R1)____.____(R2)____     Keterangan:
            |            |            |    R1 = nilai resistor 1
            |            a            |    R2 = nilai resistor 2  
           (V)                       <V>   (V)= nilai tegangan sumber bebas
            |            b            |    <v>= nilai tegangan sumber tidak
            |____________|____________|          bebas

============================================================================
============================================================================""")
                print()
                R1=float(input("Masukan nilai resistor 1 (ohm)         : "))
                R2=float(input("Masukan nilai resistor 2 (ohm)         : "))
                V1=float(input("Masukan nilai voltase bebas (volt)     : "))
                V2=float(input("Masukan nilai voltase tidak bebas(volt): "))
                break
            elif (pilihan==5):
                print()
                print("""
=======================Berikut bentuk rangkaian yang akan anda selesaikan=====================
==============================================================================================

                 ________________(R2)___________________.a      Keterangan:
                |         |                |     |              R1 = nilai resistor 1
                |       (R3)            (R4)     |              R2 = nilai resistor 2  
               (V1)       |________________|    (V3)            R3 = nilai resistor 3 
                |                |               |              R4 = nilai resistor 4 
                |              (R5)              |              R5 = nilai resistor 5 
                |                |               |             (V1)= nilai tegangan sumber bebas 1
              (R1)               |              (R5)           (V2)= nilai tegangan sumber bebas 2
                |              (V2)              |             (V3)= nilai tegangan sumber bebas 3
                |________________|_______________|______.b
                
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


