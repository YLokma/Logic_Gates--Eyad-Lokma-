from Gates import *
from cie_ciruit import all_gates

print('all gates used are: ' + str(all_gates))
all_gates.reverse()
if all_gates[0]==0 and len(all_gates)==1:
    print('A --►◦--> X')
elif all_gates[0]==1:
    if len(all_gates)==1:
        print(' A ---\ \n       :== D ---> X \n B ---/')