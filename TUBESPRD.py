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


