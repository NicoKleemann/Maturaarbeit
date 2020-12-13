import pyecm
v=int(input('paste n to find p and q: '))
fact=list(pyecm.factors(v, False, True, 10, 1))
print("Factors")
print("-------")
for x in fact:
    print(str(int(x)))
