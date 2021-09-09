#temparature---------------

value=input("Enter the type F OR C or K ")
value=value.upper()
val=int(input("Enter the value"))

if (value=="F"):
    C = (5 /9)*(val-32)
    K =C + 273
    print("celusis{0},Kelvin{1}".format(C,K))

elif(value=="C"):
    F = 1.8*val + 32
    K =val + 273
    print("Farenheit{0},Kelvin{1}".format(F,K))
else:
    C = val-273
    F = 1.8 * C + 32
    print("Farenheit{0}F,celusis{1}C".format(F, C))