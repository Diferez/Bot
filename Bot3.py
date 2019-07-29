import pymem
import pymem.process

Entr = int('AA5C', 16)

wow = pymem.Pymem("java.exe")

base =  wow.process_base.lpBaseOfDll

Off = int('E13EBFF8', 16)

con = wow.read_string(base+Entr+Off-50,50)
con = pymem.memory
print(con)


    
