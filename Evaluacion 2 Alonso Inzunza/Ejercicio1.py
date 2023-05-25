# La clínica dental “El Diente de Oro” hizo un convenio con DUOC y le ha
#  ofrecido algunos tratamientos para sus trabajadores y su grupo familiar. 
#Los tratamientos serán descontados por planilla mensualmente por un periodo de 12 meses. Todos los tratamientos incluyen:  
# ✓ Limpieza y destartraje  ✓ Aplicación de sellante   ✓ Aplicación de fluor.  
#Adicionalmente, se presentan los siguientes descuentos, sobre el total a pagar:  
# ✓	Trabajador Auxiliar, se aplicará un descuesto del 15%  ✓ Trabajador Administrativo, 
# se aplica un descuento del 10%  ✓ Trabajador Docente, 5% descuento.  
#  




carillas_porcelana = 250.000
implantes_dentales = 475.000
ortodoncia_brackets = 800.000
trab_auxiliar = 15
trab_admin = 10
docente = 5
opc = 0
opcdental = 0
subtotal = 0
total = 0

print("="*30)
print("Bienvenido a ---> El Diente de Oro <---")
print("="*30)
opcdental=int(input("Especifique su area laboral\n 1.- Trabajador Auxiliar\n 2.- Trabajador Administrativo\n 3.- Trabajador Docente\n 4.- Otros\n 5.- Renunciar a Tratamiento\n 6.- Salir\n "))
while opcdental !=7:
    try:
       if opcdental == 1:
          print("Identificamos que usted es Trabajador Auxiliar de DUOC UC, por lo tanto tiene acceso a nuestros beneficios de forma automática!.")
          print("Se le ha agregado un 15 porciento de descuento")
          print("Se han modificado los precios:")
          print(input(" a.- Carillas de Porcelana: $212.500\n b.- Implantes Dentales: $453.750\n c.- Ortodoncia Brackets: $680.000\n "))
          if opc == "a":
            opc = opc+total
            print("Usted a seleccionado Carillas de Porcelana")
          elif opc == "b":
             opc = opc+total
             print("Usted a seleccionado Implantes Dentales")
          elif opc == "c":
             opc = opc+total
             print("Usted a seleccionado Ortodoncia Brackets")
          else:
            print("Opcion no válida")
            break
       elif opcdental == 2:
          print("Identificamos que usted es Trabajador Administrativo de DUOC UC, por lo tanto tiene acceso a nuestros beneficios de forma automática!.")
          print("Se le ha agregado un 15 porciento de descuento")
          print("Se han modificado los precios:")
          print(input(" 1.1- Carillas de Porcelana: $225.500\n 1.2- Implantes Dentales: $427.750\n 1.3- Ortodoncia Brackets: $720.000\n "))
          if opc == "a":
             opc = opc+total
             print("Usted a seleccionado Carillas de Porcelana")
          elif opc == "b":
             opc = opc+total
             print("Usted a selecciondao Implantes Dentales")
          elif opc == "c":
             opc = opc+total
             print("Usted a seleccionado Ortodoncia Brackets")
          else:
            print("Opcion no válida")
       elif opcdental == 3:
          print("Identificamos que usted es Trabajador Docente de DUOC UC, por lo tanto tiene acceso a nuestros beneficios de forma automática!.")
          print("Se le ha agregado un 15 porciento de descuento")
          print("Se han modificado los precios:")
          print(input("Carillas de Porcelana: $237.500\n Implantes Dentales: $451.250\n Ortodoncia Brackets: $760.000\n "))
          if opc == "a":
             opc = opc+total
             print("Usted a seleccionado Carillas de Porcelana")
          elif opc == "b":
             opc = opc+total
             print("Usted a selecciondao Implantes Dentales")
          elif opc == "c":
             opc = opc+total
             print("Usted a seleccionado Ortodoncia Brackets")
          else:
            print("Opcion no válida")
            break
       elif opcdental == 4:
          print("Usted no puede acceder a nuestros beneficios ya que no es trabajador de DUOC UC")
          print("No se han hecho modificaciones en los precios")
          print(input("Carillas de Porcelana: $250.000\n Implantes Dentales: $475.000\n Ortodoncia Brackets: $800.000\n "))
          if opc == "a":
             opc = opc+total
             print("Usted a seleccionado Carillas de Porcelana")
          elif opc == "b":
             opc = opc+total
             print("Usted a selecciondao Implantes Dentales")
          elif opc == "c":
             opc = opc+total
             print("Usted a seleccionado Ortodoncia Brackets")
          else:
            print("Opcion no válida")
            break
       elif opcdental == 5: 
          print("Cancelando tratamiento")
       elif opcdental == 6:
          print("Saliendo...")
       else: 
            print("Opción no válida")
    except:
        print("¡Opción es un Numero!")

