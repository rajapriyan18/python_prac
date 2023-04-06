a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
c=input("Enter the operator:\n 1.Add \n 2.Sub \n 3.Mul \n 4.Div \n 5.Rem\n")
if(c=='Add' or c=='add'):
        print(a+b)
elif(c=='Sub' or c=='sub'):
        print(a-b)
elif(c=='Mul' or c=='mul'):
        print(a*b)
elif(c=='Div' or c=='div'):
        print(a/b)
elif(c=='Rem' or c=='rem'):
        print(a%b)
else:
        print("Invalid input")
    
