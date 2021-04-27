#Kodingan buat TUBES PRD
#Baru inputnya doang gaess, belom kebayang implementasi rumus2nyaaa :nnnn

jumlah_node = int(input("Masukkan jumlah node pada rangkaian: "))
R = int(input("Masukkan jumlah resistor           : "))
V = int(input("Masukkan jumlah voltase            : "))
R1=[]
V1=[]
for r in range(R):
    R2=int(input("Masukkan nilai resistor ke-{} (ohm) : ".format(r+1)))
    R1.append(R2)
for resistor in R1:
    print("Array dari resistor adalah", R1)
    break

for v in range(V):
    V2=int(input("Masukkan nilai voltase ke-{} (volt) : ".format(v+1)))
    V1.append(V2)
for voltase in V1:
    print("Array dari voltase adalah", V1)
    break
