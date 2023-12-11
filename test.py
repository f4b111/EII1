# kommentar

# importiert bibliotheken
# import math
# import random

a = True
b = False
c = True
d = True
v = True

# vorlage
term1 = (not a or not b) and (not a or b) and (a or not b)                  #1
term2 = (a and b) or (a and c) or (b and not c)                             #2
term3 = (a or b) and (not a or b) and (a or not b) and (not a or not b)     #3
term4 = a or (not b and not (a or b or c))                                  #4
term5 = (a and not b) or (a and not b and c)                                #5
term6 = (a or not (b and a)) and (c or (d or c))                            #6
term7 = (not (a and b) or not c) and (not a or v or not c)                  #7
term8 = not(not (a and b) or c) or (a and c)                                #8

# vereinfacht von mir

term9  = not a and not b
term10 = a and c or b and not c
term11 = False # ist die null
term12 = a or ( a and b and c)
term13 = a and not b
term14 = c or d
term15 = (not a or not b or not c) and (not a or v or not c)
term16 = a and (c or b)


print("\nVorlage\n")
print("1:", term1)
print("2:", term2)
print("3:", term3)
print("4:", term4)
print("5:", term5)
print("6:", term6)
print("7:", term7)
print("8:", term8)
print("\nMeine Vereinfachung")
print("1:", term9)
print("2:", term10)
print("3:", term11)
print("4:", term12)
print("5:", term13)
print("6:", term14)
print("7:", term15)
print("8:", term16)


