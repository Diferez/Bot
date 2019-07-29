import pymem
import pymem.process

i = int('E107D088', 16)
i = i +10
wow = pymem.Pymem("java.exe")
awd = pymem.process.module_from_name(wow.process_handle,"awt.dll")
dira = awd.lpBaseOfDll
base =  wow.process_base.lpBaseOfDll

print("aqui las dir")
print("awd = ", hex(dira), "base = ", hex(base))
dirb =wow.read_bytes( int('00111ED8',16)+dira,5)
dirb = int.from_bytes(dirb,byteorder='little')
dirc = wow.read_bytes(dirb+int('C0',16),4)
dirc = int.from_bytes(dirc,byteorder='little')
print("dirc = ", dirc, hex(dirc))
dird = wow.read_bytes(dirc+int('138',16),4)
dird = int.from_bytes(dird,byteorder='little')
print("dird = ", dird, hex(dird))

dird = wow.read_bytes(dird+int('64',16),4)
dird = int.from_bytes(dird,byteorder='little')

dird = wow.read_bytes(dird+int('14',16),4)
dird = int.from_bytes(dird,byteorder='little')

dird = wow.read_bytes(dird+int('484',16),4)
dird = int.from_bytes(dird,byteorder='little')
print("dird = ", dird,hex(dird))
#print("la diva ",wow.read_bytes(dirb,24))

# for x in range(0,100):
#     try:
#         print(str(x)+" = ", end ='')
#         con = wow.read_string(dird+x,200)
#         print(con)
#     except:
#         print("ups")

final = wow.read_string(dird+96,20)
final = final.split('}')[0]
final = final.split(' ')
name = final[0]
clase = final[1]
print("Nombre = ", name, "Clase = ", clase)