import pymem
import pymem.process


i = int('E0E4BD30', 16)
i = i-20
offset = 1959296


wow = pymem.Pymem("java.exe")
#con = wow.read_string(i,40)
base =  wow.process_base.lpBaseOfDll

#a = wow.write_string(i, "Hola")
#con2= wow.read_string(i+1,50)
some = wow
base = base 
i = i 
con = wow.read_bytes(i,4)
print(con)
con = wow.read_int(i)
print(con)

#add = pymem.process.base_address(wow.process_handle)
for x in range (0,2):
    
    try:
        con = wow.read_string(i+x*2,40)
        
        #con = wow.read_string(base+x*2,10)
        print(con, end ='')
    except:
        print("ups")

    
print('Process Base Address: {}'.format(some)+ " ")
print(wow)
print(some , " Some")
print(base)
print(hex(base))

#ILIANBTO
#TESTYOP

#E100A330 + 

#‭7FF713250000‬