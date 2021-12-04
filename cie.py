# /usr/bin/python3
cie = []

inputs = 3

a = []
while inputs >= 3 and len(a) < 8:
    a.extend([0, 0, 0, 0, 1, 1, 1, 1])

b = []
while inputs >= 2 and len(b) < 8:
    b.extend([0, 0, 1, 1])

c = []
while inputs >= 1 and len(c) < 8:
    c.extend([0, 1])


def cie_list(input_no):
    cie.append(a)
    cie.append(b)
    cie.append(c)
    return cie
