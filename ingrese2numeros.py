a=input("ingrese un numero ")
b=input("ingrese otro numero ")
print 'numeros ingresados ',a,b
op=1
while(op!=0):
    
    print '1-sumar'
    print '2-restar'
    print '3-dividir'
    print '4-multiplicar'
    
    op=input('ingrese la opcion que desea realizar: ')
    
    if(op==1):
        res=(a+b)
        print 'el resultado es: ',res
    if(op==2):
        res=(a-b)
        print 'el resultado es: ',res
    if(op==3):
        res=(a/b)
        print 'el resultado es: ',res
    if(op==4):
        res=(a*b)
        print 'el resultado es: ',res
        
    print '1-sumar'
    print '2-restar'
    print '3-dividir'
    print '4-multiplicar'
    op=input('ingrese la opcion que desea realizar: ')    
    

