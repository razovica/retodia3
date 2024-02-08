# Reto Dia 3
Cuenta = input ("Cantidad de usuarios Nuevos:  ")
Contador = 0 
Control1 = True
ok_correcto = True
registros = []
while ok_correcto:
   
    if Contador==int(Cuenta):
        ok_correcto=False
        print
        print ("    TERMINO CON EXITO")
        #registros=[str(Contador),Nombre, Apellido, Correo, Telefono]
        print ("Numero de Usuarios registrados:    " + str(Contador))
        break
    else:
        Contador= Contador + 1

    #Nombre
    while Control1:
        Nombre = input ("Nombre:  " + str(Contador) + "/" + Cuenta + ":   ")
        if len(Nombre) < 5 or len(Nombre) >= 50:
            print("Nombre menos de 5 y mas 50")
        else :   
            Control1= False

    # Apellido
    Control1= True        
    while Control1:
        Apellido = input ("Apellido:  "+ str(Contador) + "/" + Cuenta + ":   ")
        if len(Apellido) < 5 or len(Apellido) >= 50:
            print("Apellido menos de 5 y mas 50")
        else :   
            Control1= False

    # correo
    Control1= True   
    while Control1:
        Correo = input ("Correo:  "+ str(Contador) + "/" + Cuenta + ":   ")
        if len(Correo) < 5 or len(Correo) >= 50:
            print("Correo menos de 5 y mas 50")
        else :
            Control1= False

    # telefono
    Control1= True   
    while Control1:
        Telefono = input ("Telefono:  "+ str(Contador) + "/" + Cuenta + ":   ")
        if len(Telefono) !=10:
            print("Telefono 10 digitos")
        else :
            Control1= False
        
    
    Control1= True 
    print ( str(Contador) + "/" + Cuenta )
    registros.append[Contador]

    

else :
    ok_correcto= False           


# print ("Numero de Usuarios registrados:    ") + str (Contador)
