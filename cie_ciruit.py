from Gates import *
from cie_inputs import cie, inputs

cie_list=[]
if inputs == 1:
    a = cie[3] ; cie_list.append(a)
elif inputs == 2:
    a = cie[2] ; b = cie[3] ; cie_list.append(a) ; cie_list.append(b)
elif inputs == 3:
    a = cie[1] ; b = cie[2] ; c = cie[3] ; cie_list.append(a) ; cie_list.append(b) ; cie_list.append(c)
elif inputs == 4:
    a = cie[0] ; b = cie[1] ; c = cie[2] ; d = cie[3] ; cie_list.append(a) ; cie_list.append(b) ; cie_list.append(c) ; cie_list.append(d)
else: print('No of inputs has to be in range 1:4')
print(cie_list)
no_gates = int(input('How many gates? \n'))
print('Not=0\tAnd=1\tOr=2\tNand=3\tNor=4\tXor=5')
first_gate = int(input('Gate 1: '))
bracket = [int(input('first wire: ')), int(input('second wire: '))]
print('#####')
all_gates=[]
all_gates.append(first_gate)
m = bracket[0] - 1
n = bracket[1] - 1
if no_gates==1:
    p = []
    for i in range(0,8):
        if first_gate==0:
            p.append(not_gate(cie_list[m][i]))
        elif first_gate==1:
            p.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==2:
            p.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==3:
            p.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==4:
            p.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==5:
            p.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    
    x = p
    print('x = '+ str(x))
elif no_gates==2:
    p=[]
    for i in range(0,8):
        if first_gate==0:
            p.append(not_gate(cie_list[m][i]))
        elif first_gate==1:
            p.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==2:
            p.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==3:
            p.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==4:
            p.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==5:
            p.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('p ='+ str(p))
    cie_list.append(p)
    print(cie_list)
    second_gate = int(input('Gate 2: '))
    all_gates.append(second_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    q = []
    for i in range(0,8):
        if second_gate==0:
            q.append(not_gate(cie_list[m][i]))
        elif second_gate==1:
            q.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==2:
            q.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==3:
            q.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==4:
            q.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==5:
            q.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    x = q
    print('x = '+ str(x))
elif no_gates==3:
    p=[]
    for i in range(0,8):
        if first_gate==0:
            p.append(not_gate(cie_list[m][i]))
        elif first_gate==1:
            p.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==2:
            p.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==3:
            p.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==4:
            p.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==5:
            p.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('p ='+ str(p))
    cie_list.append(p)
    print(cie_list)
    second_gate = int(input('Gate 2: '))
    all_gates.append(second_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    q = []
    for i in range(0,8):
        if second_gate==0:
            q.append(not_gate(cie_list[m][i]))
        elif second_gate==1:
            q.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==2:
            q.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==3:
            q.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==4:
            q.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==5:
            q.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('q ='+ str(q))
    cie_list.append(q)
    print(cie_list)
    third_gate = int(input('Gate 3: '))
    all_gates.append(third_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    r = []
    for i in range(0,8):
        if third_gate==0:
            r.append(not_gate(cie_list[m][i]))
        elif third_gate==1:
            r.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==2:
            r.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==3:
            r.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==4:
            r.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==5:
            r.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    x = r
    print('x = '+ str(x))
elif no_gates==4:
    p=[]
    for i in range(0,8):
        if first_gate==0:
            p.append(not_gate(cie_list[m][i]))
        elif first_gate==1:
            p.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==2:
            p.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==3:
            p.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==4:
            p.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==5:
            p.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('p ='+ str(p))
    cie_list.append(p)
    print(cie_list)
    second_gate = int(input('Gate 2: '))
    all_gates.append(second_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    q = []
    for i in range(0,8):
        if second_gate==0:
            q.append(not_gate(cie_list[m][i]))
        elif second_gate==1:
            q.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==2:
            q.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==3:
            q.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==4:
            q.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==5:
            q.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('q ='+ str(q))
    cie_list.append(q)
    print(cie_list)
    third_gate = int(input('Gate 3: '))
    all_gates.append(third_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    r = []
    for i in range(0,8):
        if third_gate==0:
            r.append(not_gate(cie_list[m][i]))
        elif third_gate==1:
            r.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==2:
            r.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==3:
            r.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==4:
            r.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==5:
            r.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('r ='+ str(r))
    cie_list.append(r)
    print(cie_list)
    fourth_gate = int(input('Gate 4: '))
    all_gates.append(fourth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    s = []
    for i in range(0,8):
        if fourth_gate==0:
            s.append(not_gate(cie_list[m][i]))
        elif fourth_gate==1:
            s.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==2:
            s.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==3:
            s.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==4:
            s.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==5:
            s.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    x = s
    print('x = '+ str(x))
elif no_gates==5:
    p=[]
    for i in range(0,8):
        if first_gate==0:
            p.append(not_gate(cie_list[m][i]))
        elif first_gate==1:
            p.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==2:
            p.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==3:
            p.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==4:
            p.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==5:
            p.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('p ='+ str(p))
    cie_list.append(p)
    print(cie_list)
    second_gate = int(input('Gate 2: '))
    all_gates.append(second_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    q = []
    for i in range(0,8):
        if second_gate==0:
            q.append(not_gate(cie_list[m][i]))
        elif second_gate==1:
            q.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==2:
            q.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==3:
            q.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==4:
            q.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==5:
            q.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('q ='+ str(q))
    cie_list.append(q)
    print(cie_list)
    third_gate = int(input('Gate 3: '))
    all_gates.append(third_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    r = []
    for i in range(0,8):
        if third_gate==0:
            r.append(not_gate(cie_list[m][i]))
        elif third_gate==1:
            r.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==2:
            r.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==3:
            r.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==4:
            r.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==5:
            r.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('r ='+ str(r))
    cie_list.append(r)
    print(cie_list)
    fourth_gate = int(input('Gate 4: '))
    all_gates.append(fourth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    s = []
    for i in range(0,8):
        if fourth_gate==0:
            s.append(not_gate(cie_list[m][i]))
        elif fourth_gate==1:
            s.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==2:
            s.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==3:
            s.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==4:
            s.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==5:
            s.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('s ='+ str(s))
    cie_list.append(s)
    print(cie_list)
    fifth_gate = int(input('Gate 5: '))
    all_gates.append(fifth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    t = []
    for i in range(0,8):
        if fifth_gate==0:
            t.append(not_gate(cie_list[m][i]))
        elif fifth_gate==1:
            t.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==2:
            t.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==3:
            t.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==4:
            t.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==5:
            t.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    x = t
    print('x = '+ str(x))
elif no_gates==6:
    p=[]
    for i in range(0,8):
        if first_gate==0:
            p.append(not_gate(cie_list[m][i]))
        elif first_gate==1:
            p.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==2:
            p.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==3:
            p.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==4:
            p.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==5:
            p.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('p ='+ str(p))
    cie_list.append(p)
    print(cie_list)
    second_gate = int(input('Gate 2: '))
    all_gates.append(second_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    q = []
    for i in range(0,8):
        if second_gate==0:
            q.append(not_gate(cie_list[m][i]))
        elif second_gate==1:
            q.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==2:
            q.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==3:
            q.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==4:
            q.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==5:
            q.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('q ='+ str(q))
    cie_list.append(q)
    print(cie_list)
    third_gate = int(input('Gate 3: '))
    all_gates.append(third_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    r = []
    for i in range(0,8):
        if third_gate==0:
            r.append(not_gate(cie_list[m][i]))
        elif third_gate==1:
            r.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==2:
            r.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==3:
            r.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==4:
            r.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==5:
            r.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('r ='+ str(r))
    cie_list.append(r)
    print(cie_list)
    fourth_gate = int(input('Gate 4: '))
    all_gates.append(fourth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    s = []
    for i in range(0,8):
        if fourth_gate==0:
            s.append(not_gate(cie_list[m][i]))
        elif fourth_gate==1:
            s.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==2:
            s.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==3:
            s.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==4:
            s.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==5:
            s.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('s ='+ str(s))
    cie_list.append(s)
    print(cie_list)
    fifth_gate = int(input('Gate 5: '))
    all_gates.append(fifth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    t = []
    for i in range(0,8):
        if fifth_gate==0:
            t.append(not_gate(cie_list[m][i]))
        elif fifth_gate==1:
            t.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==2:
            t.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==3:
            t.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==4:
            t.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==5:
            t.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('t ='+ str(t))
    cie_list.append(t)
    print(cie_list)
    sixth_gate = int(input('Gate 6: '))
    all_gates.append(sixth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    u = []
    for i in range(0,8):
        if sixth_gate==0:
            u.append(not_gate(cie_list[m][i]))
        elif sixth_gate==1:
            u.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif sixth_gate==2:
            u.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif sixth_gate==3:
            u.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif sixth_gate==4:
            u.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif sixth_gate==5:
            u.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    x = u
    print('x = '+ str(x))
elif no_gates==7:
    p=[]
    for i in range(0,8):
        if first_gate==0:
            p.append(not_gate(cie_list[m][i]))
        elif first_gate==1:
            p.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==2:
            p.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==3:
            p.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==4:
            p.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif first_gate==5:
            p.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('p ='+ str(p))
    cie_list.append(p)
    print(cie_list)
    second_gate = int(input('Gate 2: '))
    all_gates.append(second_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    q = []
    for i in range(0,8):
        if second_gate==0:
            q.append(not_gate(cie_list[m][i]))
        elif second_gate==1:
            q.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==2:
            q.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==3:
            q.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==4:
            q.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif second_gate==5:
            q.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('q ='+ str(q))
    cie_list.append(q)
    print(cie_list)
    third_gate = int(input('Gate 3: '))
    all_gates.append(third_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    r = []
    for i in range(0,8):
        if third_gate==0:
            r.append(not_gate(cie_list[m][i]))
        elif third_gate==1:
            r.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==2:
            r.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==3:
            r.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==4:
            r.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif third_gate==5:
            r.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('r ='+ str(r))
    cie_list.append(r)
    print(cie_list)
    fourth_gate = int(input('Gate 4: '))
    all_gates.append(fourth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    s = []
    for i in range(0,8):
        if fourth_gate==0:
            s.append(not_gate(cie_list[m][i]))
        elif fourth_gate==1:
            s.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==2:
            s.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==3:
            s.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==4:
            s.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif fourth_gate==5:
            s.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('s ='+ str(s))
    cie_list.append(s)
    print(cie_list)
    fifth_gate = int(input('Gate 5: '))
    all_gates.append(fifth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    t = []
    for i in range(0,8):
        if fifth_gate==0:
            t.append(not_gate(cie_list[m][i]))
        elif fifth_gate==1:
            t.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==2:
            t.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==3:
            t.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==4:
            t.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif fifth_gate==5:
            t.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('t ='+ str(t))
    cie_list.append(t)
    print(cie_list)
    sixth_gate = int(input('Gate 6: '))
    all_gates.append(sixth_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    u = []
    for i in range(0,8):
        if sixth_gate==0:
            u.append(not_gate(cie_list[m][i]))
        elif sixth_gate==1:
            u.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif sixth_gate==2:
            u.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif sixth_gate==3:
            u.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif sixth_gate==4:
            u.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif sixth_gate==5:
            u.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    print('u ='+ str(u))
    cie_list.append(u)
    print(cie_list)
    seventh_gate = int(input('Gate 7: '))
    all_gates.append(seventh_gate)
    bracket = [int(input('first wire: ')), int(input('second wire: '))]
    m = bracket[0] - 1
    n = bracket[1] - 1
    v = []
    for i in range(0,8):
        if seventh_gate==0:
            v.append(not_gate(cie_list[m][i]))
        elif seventh_gate==1:
            v.append(and_gate(cie_list[m][i],cie_list[n][i]))
        elif seventh_gate==2:
            v.append(or_gate(cie_list[m][i],cie_list[n][i]))
        elif seventh_gate==3:
            v.append(nand_gate(cie_list[m][i],cie_list[n][i]))
        elif seventh_gate==4:
            v.append(nor_gate(cie_list[m][i],cie_list[n][i]))
        elif seventh_gate==5:
            v.append(xor_gate(cie_list[m][i],cie_list[n][i]))
        else:
            print('Insert an appropriate gate code')
            break
    x = v
    print('x = '+ str(x))
else: print('la ro7 4oflak computer tani ye3melha kefaya awi 690 line code :)')